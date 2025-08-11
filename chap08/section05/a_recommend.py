import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# 1) 데이터 준비
df = pd.DataFrame({
    'user': ['A', 'A', 'B', 'B', 'C', 'C', 'D'],
    'book': ['책1', '책2', '책2', '책3', '책1', '책3', '책2'],
    'like_count': [5, 3, 4, 2, 1, 5, 3]  # 좋아요 수 추가
})

# 2) 유저-책 행렬 만들기
pivot = df.pivot_table(index='user', columns='book', values='like_count', aggfunc='sum', fill_value=0)

# 3) 유저끼리 서로 비슷한 책을 좋아하는 정도를 나타낸 수 (cosine 유사도)
sim = cosine_similarity(pivot)
# 코딩 편의상 찾기 편하게 행렬을 만듬: 행, 열을 모두 유저로 표시
sim_df = pd.DataFrame(sim, index=pivot.index, columns=pivot.index)
print(sim_df)    # 디버깅용

def recommend(user):
    # 4) A 유저와 가장 유사한 유저 찾기: A를 제외하고 가장 숫자가 큰사람 찾기(유사한 사람)
    similar_users = sim_df[user].drop(user).sort_values(ascending=False).head(2).index

    # 5) A가 본 책 목록
    books_a = df[df['user'] == user]['book']

    # 6) 추천: A가 안 본 책 중 가장 유사한 유저가 본 책
    recommend_books = df[
        (df['user'].isin(similar_users)) &      # 유사한 유저가 본 책
        (~df['book'].isin(books_a))              # A가 안 본 책만
    ].drop_duplicates(subset=['book'])  # 중복 책 제외

    # 7) 추천 책을 좋아요 수에 따라 내림차순 정렬 (좋아요 수가 높은 책을 우선 추천)
    recommend_books = recommend_books.sort_values(by='like_count', ascending=False)

    # 8) 추천 결과 출력
    recommended_books = list(recommend_books['book'])
    print(f"{user}에게 추천할 책:", recommended_books)

    return recommended_books

# 9) 예시: A 유저에게 추천할 책 찾기
recommend('A')
