from elasticsearch import Elasticsearch
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix
from datetime import datetime

# === 1) Elasticsearch 연결 ===
es = Elasticsearch(
    ["https://localhost:9200"],
    basic_auth=("elastic", "=U5oxindf+JStU2U25mT"),
    verify_certs=False
)
INDEX_SRC = "gallery-likes"
INDEX_REC = "gallery-likes-suggested"

# === 2) 원본 데이터 가져오기 ===
res = es.search(
    index=INDEX_SRC,
    body={
        "size": 10000,
        "_source": ["email", "gallery_title", "like_count"]
    }
)

# === 3) DataFrame 변환 ===
data = []
for hit in res['hits']['hits']:
    src = hit['_source']
    data.append({
        'id': hit['_id'],
        'email': src['email'],
        'gallery_title': src['gallery_title'],
        'like_count': src['like_count']
    })

df = pd.DataFrame(data)

# === 4) 사용자-파일 행렬 생성 ===
matrix = df.pivot_table(index='email', columns='gallery_title', values='like_count', fill_value=0)

# === 5) Sparse Matrix 변환 ===
sparse_matrix = csr_matrix(matrix.values)

# === 6) KNN 모델 학습 ===
model = NearestNeighbors(metric='cosine', algorithm='brute')
model.fit(sparse_matrix)

# === 7) 사용자별 추천 계산 및 새로운 인덱스에 저장 ===
top_n = 2
for user in matrix.index:
    user_idx = matrix.index.get_loc(user)
    target_vector = sparse_matrix[user_idx]

    n_neighbors = min(4, len(matrix))  # 데이터 수보다 많으면 에러
    distances, indices = model.kneighbors(target_vector, n_neighbors=n_neighbors)

    similar_idx = [i for i in indices.flatten() if i != user_idx]
    similar_users = [matrix.index[i] for i in similar_idx]

    recommend_scores = {}
    for title in matrix.columns:
        if matrix.loc[user, title] == 0:
            score = matrix.loc[similar_users, title].sum() if similar_users else 0
            if score > 0:
                recommend_scores[title] = score

    # Top-N 추천 선택
    sorted_recs = sorted(recommend_scores.items(), key=lambda x: x[1], reverse=True)[:top_n]
    suggested_list = [title for title, _ in sorted_recs]

    # === 8) Elasticsearch 추천 인덱스에 업데이트/추가 ===
    if suggested_list:                           # 있을때만 es 에 넣기
        # 이미 존재하면 update, 없으면 새로 index
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
