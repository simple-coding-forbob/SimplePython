import pandas as pd
from sklearn.neighbors import NearestNeighbors
from elasticsearch import Elasticsearch
from datetime import datetime

# === 1) Elasticsearch 연결 ===
es = Elasticsearch(
    ["http://localhost:9200"]  # 로컬 ES 서버 연결
)

# === 2) 원본 데이터 가져오기 ===
res = es.search(
    index="filedb-likes",  # 검색할 인덱스명
    body={
        "size": 10000,  # 최대 1만건 가져오기
        "_source": ["email", "file_title", "like_count"]  # 필요한 필드만 추출
    }
)

# === 3) DataFrame 변환 ===
data = []
for hit in res['hits']['hits']:  # 검색 결과 반복
    src = hit['_source']         # _source 안의 실제 데이터
    data.append({
        'id': hit['_id'],        # 문서 ID
        'email': src['email'],   # 사용자 이메일
        'file_title': src['file_title'],  # 파일 제목
        'like_count': src['like_count']   # 좋아요 수
    })

df = pd.DataFrame(data)  # Pandas DataFrame 생성

# 4) 사용자-책 행렬
mx = df.pivot_table(
    index='email',        # 행: 사용자
    columns='file_title', # 열: 파일 제목
    values='like_count',  # 값: 좋아요 수
    fill_value=0          # 없는 값은 0으로 채움
)

# 5) KNN 모델 학습
model = NearestNeighbors(metric='cosine', algorithm='brute')  # 코사인 유사도 기반 최근접 이웃
model.fit(mx.values)  # 사용자-책 행렬로 학습

# 6) Top-N 추천 함수
def rec_user(user_email, top_n=2):
    user_idx = mx.index.get_loc(user_email)            # 사용자 인덱스 번호 찾기
    tfeature = mx.to_numpy()[user_idx].reshape(1, -1)  # 해당 사용자의 벡터 (1행 n열)
    print("111", tfeature)

    # 유사 사용자 찾기
    dt, inx = model.kneighbors(tfeature, n_neighbors=2)
    similar_idx = [i for i in inx.flatten() if i != user_idx]  # 자기 자신 제외
    similar_users = [mx.index[i] for i in similar_idx]         # 유사 사용자 이메일

    # 내가 이미 좋아요한 타이틀
    my_likes = df.loc[df['email'] == user_email, 'file_title'].tolist()

    # 비슷한 사용자들이 좋아한 타이틀 합산
    rec_sum = (
        df[df['email'].isin(similar_users) & ~df['file_title'].isin(my_likes)]
          .groupby('file_title')['like_count'].sum()
    )

    # Top-N 선택
    top_rec = rec_sum.sort_values(ascending=False).head(top_n)
    return top_rec.index.tolist()  # 추천 제목 리스트 반환

# 7) 모든 사용자에 대해 추천 → Elasticsearch 저장
for user in mx.index:  # 모든 사용자 반복
    slist = rec_user(user, top_n=2)  # 추천 결과
    print(f"사용자 {user} 추천: {slist}")

    es.index(
        index="filedb-likes-suggested",  # 추천 결과 저장할 인덱스
        id=user,                         # 사용자 이메일을 문서 ID로 사용
        document={
            "email": user,
            "suggested": slist,          # 추천 목록
            "update_time": datetime.now() # 갱신 시간
        }
    )
