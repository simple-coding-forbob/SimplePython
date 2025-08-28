# 평점 기반 추천 : 피어슨 상관 계수
import pandas as pd

# 1) 샘플 데이터
data = {
    'email': [
        'forbob@naver.com', 'forbob@naver.com',
        'forbob2@naver.com', 'forbob2@naver.com'
    ],
    'file_title': [
        '제목1', '제목2',
        '제목2', '제목3'
    ],
    'like_count': [5, 3, 2, 3]
}

df = pd.DataFrame(data)

# 2) 사용자-아이템 행렬
mx = df.pivot_table(index='email', columns='file_title', values='like_count', fill_value=0)

# 3) 사용자 간 피어슨 상관계수
user_corr = mx.T.corr(method='pearson')

# 4) 추천 대상
target_user = 'forbob@naver.com'

# 5) 유사 사용자 선택
sim_users = user_corr.loc[target_user].drop(target_user)
sim_users = sim_users[sim_users > 0]

# 6) 아직 평가하지 않은 아이템 선택
my_likes = mx.loc[target_user]
unseen_items = my_likes[my_likes == 0].index.tolist()

# 7) 추천 점수 계산 (.dot() 사용): 행렬곱 사용: 아이템 * 추천점수(아이템별 추천점수 구하기)
rec_scores = mx.loc[sim_users.index, unseen_items].T.dot(sim_users)

# 8) Top-N 추천
top_N = 2
top_items = rec_scores.sort_values(ascending=False).head(top_N).index.tolist()

# 9) 결과 출력
print(f"{target_user}에게 추천할 Top-{top_N} 아이템: {top_items}")
