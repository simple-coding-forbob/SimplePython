import pandas as pd
from sklearn.neighbors import NearestNeighbors
from elasticsearch import Elasticsearch
from datetime import datetime

# === 1) Elasticsearch 연결 ===
es = Elasticsearch(
    ["http://localhost:9200"]
    # basic_auth=("계정", "암호"),
    # verify_certs=False
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

# 4) 사용자-책 행렬
mx = df.pivot_table(index='email', columns='gallery_title', values='like_count', fill_value=0)

# 5) KNN 모델 학습
model = NearestNeighbors(metric='cosine', algorithm='brute')
model.fit(mx.values)

# 6) Top-N 추천 함수
def rec_user(user_email, top_n=2):
    user_idx = mx.index.get_loc(user_email)
    tfeature = mx.to_numpy()[user_idx].reshape(1, -1)

    # 유사 사용자 찾기
    dt, inx = model.kneighbors(tfeature, n_neighbors=mx.shape[0])
    similar_idx = [i for i in inx.flatten() if i != user_idx]
    similar_users = [mx.index[i] for i in similar_idx]

    # 내가 이미 좋아요한 타이틀
    my_likes = df.loc[df['email'] == user_email, 'gallery_title'].tolist()

    # 비슷한 사용자들이 좋아한 타이틀 합산
    rec_sum = (
        df[df['email'].isin(similar_users) & ~df['gallery_title'].isin(my_likes)]
          .groupby('gallery_title')['like_count'].sum()
    )

    # Top-N 선택
    top_rec = rec_sum.sort_values(ascending=False).head(top_n)
    return top_rec.index.tolist()  # 추천 제목 리스트 반환

# 7) 모든 사용자에 대해 추천 → Elasticsearch 저장
for user in mx.index:
    slist = rec_user(user, top_n=2)
    print(f"사용자 {user} 추천: {slist}")

    es.index(
        index=INDEX_REC,
        id=user,  # 사용자 이메일을 고유 ID로
        document={
            "email": user,
            "suggested": slist,
            "update_time": datetime.now()
        }
    )
