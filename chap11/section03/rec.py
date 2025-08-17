import pandas as pd
from sklearn.neighbors import NearestNeighbors

# 샘플 데이터 생성 (forbob4 제외)
df = pd.DataFrame({
    'email': [
        'forbob@naver.com', 'forbob@naver.com',
        'forbob2@naver.com', 'forbob2@naver.com'
    ],
    'file_title': [
        '제목1', '제목2',
        '제목2', '제목3'
    ],
    'like_count': [1, 1, 1, 1]  # 모두 1
})

# 1) 사용자-책 행렬 만들기
user_title_matrix = df.pivot_table(index='email', columns='file_title', values='like_count', fill_value=0)

# 2) KNN 모델 학습 (DataFrame.values 그대로 사용)
model = NearestNeighbors(metric='cosine', algorithm='brute')
model.fit(user_title_matrix.values)

# 3) 추천 대상 사용자 지정
target_user = 'forbob@naver.com'
user_idx = user_title_matrix.index.get_loc(target_user)  # 추천 유저의 인덱스번호가 리턴됨
target_vector = user_title_matrix.values[user_idx].reshape(1, -1)  # 1행짜리 배열로 변환(유사 사용자 찾기 함수때문에 필요)

# 4) Top-N 유사 사용자 찾기
# indices.flatten() : 다차원 -> 1차원으로 변경
distances, indices = model.kneighbors(target_vector, n_neighbors=2)     # 자기 자신 포함 인덱스번호가 리턴됨
similar_users_idx = [i for i in indices.flatten() if i != user_idx]     # 자기 자신 제외
similar_users = [user_title_matrix.index[i] for i in similar_users_idx] # 인덱스번호에 해당되는 유저명 가져오기

# 5) 비슷한 사용자들이 좋아한 타이틀 합산 점수 계산
recommend_scores = {}
for title in user_title_matrix.columns:
    if user_title_matrix.loc[target_user, title] == 0:  # 아직 안 본 책
        score = user_title_matrix.loc[similar_users, title].sum()
        recommend_scores[title] = score

# 6) Top-N 추천 책 선택
# recommend_scores.items() : 딕셔너리 값을 (키, 값) 튜플 형태로 바꿉니다.
# x[1] : (키, 값) 중 두번째 값을 선택합니다.
sorted_recommendations = sorted(recommend_scores.items(), key=lambda x: x[1], reverse=True)[:2]

# 7) 결과 출력
print(f"사용자 {target_user}에게 추천할 책:")
for book, score in sorted_recommendations:
    print(f"{book}")
