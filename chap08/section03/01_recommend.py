import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# 1. 데이터 준비
df = pd.DataFrame({
    'user': ['A', 'A', 'B', 'B', 'C', 'C', 'D'],
    'book': ['책1', '책2', '책2', '책3', '책1', '책3', '책2']
})

# 2. 유저-책 행렬 만들기
pivot = df.pivot_table(index='user', columns='book', aggfunc=lambda x: 1, fill_value=0)

# 3. 유저끼리 서로 비슷한 책을 좋아하는 정도를 나타낸 수 (cosine 유사도)
sim = cosine_similarity(pivot)
# 코딩 편의상 찾기 편하게 행렬을 만듬: 행, 열을 모두 유저로 표시
sim_df = pd.DataFrame(sim, index=pivot.index, columns=pivot.index)
print(sim_df)    # 디버깅

# 4. A 유저와 가장 유사한 유저 찾기: A를 제외하고 가장 숫자가 큰사람 찾기(유사한 사람)
# similar_users = sim_df['A'].drop('A').idxmax()
# A 제외하고 유사도 상위 2명 이름(index) 저장
similar_users = sim_df['A'].drop('A').sort_values(ascending=False).head(2).index

# 5. A가 본 책 목록
books_a = df[df['user'] == 'A']['book']

# 6. 추천: A가 안 본 책 중 가장 유사한 유저가 본 책
recommend = df[
    (df['user'].isin(similar_users)) &      # 유사한 유저가 본 책
    (~df['book'].isin(books_a))              # A가 안 본 책만
]['book'].drop_duplicates()

# 7. 추천 결과 출력
print(f"A와 가장 유사한 유저: {similar_users}")
print("A에게 추천할 책:", list(recommend))
