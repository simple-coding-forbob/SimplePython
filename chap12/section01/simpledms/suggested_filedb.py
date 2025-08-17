from elasticsearch import Elasticsearch
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from datetime import datetime

# === 1) Elasticsearch 연결 ===
es = Elasticsearch(
    ["https://localhost:9200"],
    basic_auth=("elastic", "=U5oxindf+JStU2U25mT"),
    verify_certs=False
)
INDEX_SRC = "filedb-likes"
INDEX_REC = "filedb-likes-suggested"

# === 2) 원본 데이터 가져오기 ===
res = es.search(
    index=INDEX_SRC,
    body={
        "size": 10000,
        "_source": ["email", "file_title", "like_count"]
    }
)

# === 3) DataFrame 변환 ===
data = []
for hit in res['hits']['hits']:
    src = hit['_source']
    data.append({
        'id': hit['_id'],
        'email': src['email'],
        'file_title': src['file_title'],
        'like_count': src['like_count']
    })

df = pd.DataFrame(data)

# === 4) 사용자-파일 행렬 생성 ===
matrix = df.pivot_table(index='email', columns='file_title', values='like_count', fill_value=0)

# === 5) KNN 모델 학습 (희소행렬 제거) ===
model = NearestNeighbors(metric='cosine', algorithm='brute')
model.fit(matrix.values)  # csr_matrix 없이 바로 사용

# === 6) 사용자별 추천 계산 및 Elasticsearch 업데이트 ===
top_n = 2
for user in matrix.index:
    user_idx = matrix.index.get_loc(user)                                   # 추천 유저의 인덱스번호가 리턴됨
    target_vector = matrix.values[user_idx].reshape(1, -1)                  # 1행짜리 배열로 변환(유사 사용자 찾기 함수때문에 필요)

    distances, indices = model.kneighbors(target_vector, n_neighbors=2)      # 자기 자신 포함 인덱스번호가 리턴됨
    similar_idx = [i for i in indices.flatten() if i != user_idx]            # 자기 자신 제외
    similar_users = [matrix.index[i] for i in similar_idx]                   # 인덱스번호에 해당되는 유저명 가져오기

    # 7) 비슷한 사용자들이 좋아한 타이틀 합산 점수 계산
    recommend_scores = {}                                                     # 추천 결과 딕셔너리 준비
    for title in matrix.columns:
        if matrix.loc[user, title] == 0:                                      # 아직 안 본 책
            score = matrix.loc[similar_users, title].sum()                    # 유사사용자 좋아요수 총합
            recommend_scores[title] = score                                   # 총합을 딕셔너리에 저장

    # Top-N 추천 선택
    # recommend_scores.items() : 튜플로 변경 (키,값) 배열
    sorted_recs = sorted(recommend_scores.items(), key=lambda x: x[1], reverse=True)[:top_n] # 추천 결과 내림차순 정렬
    suggested_list = [title for title, _ in sorted_recs]

    # Elasticsearch DB 추천 인덱스에 업데이트/추가
    if suggested_list:
        es.index(
            index=INDEX_REC,
            id=user,  # 사용자 이메일을 고유 ID로
            document={
                "email": user,
                "suggested": suggested_list,
                "update_time": datetime.now()
            }
        )

    print(f"사용자 {user} 추천 완료: {suggested_list if suggested_list else '추천 없음'}")
