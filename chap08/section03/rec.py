import pandas as pd               # 데이터프레임 처리를 위한 pandas 임포트
from sklearn.neighbors import NearestNeighbors  # k-NN 기반 최근접 이웃 모델 임포트

# 사용자-책 좋아요 데이터 생성 (user_id, book_id, liked(좋아요:1, 아니면 0))
data = {
    'user_id': [1, 1, 1, 2, 2, 3, 3, 4],  # 사용자 ID
    'book_id': [101, 102, 103, 101, 103, 102, 104, 105],  # 책 ID
    'liked':   [1,   1,   0,   1,   1,   1,   1,   1]     # 좋아요 여부 (1=좋아요, 0=좋아요 아님)
}

df = pd.DataFrame(data)  # 위 데이터를 pandas DataFrame으로 변환

# 책 ID와 제목을 매핑한 딕셔너리 (추천 결과 출력용)
books = {
    101: '파이썬 입문',
    102: '자바 완전정복',
    103: '데이터 과학 기초',
    104: '웹 개발 시작하기',
    105: '머신러닝 핵심'
}

# 사용자-책 매트릭스 생성: 행은 사용자, 열은 책, 값은 liked (1 또는 0)
# 평가하지 않은 항목은 fill_value=0으로 채움
user_book_matrix = df.pivot_table(index='user_id', columns='book_id', values='liked', fill_value=0)

print("사용자-책 행렬:")
print(user_book_matrix)  # 매트릭스 출력

# k-NN 모델 생성, 코사인 거리를 유사도 계산에 사용, brute-force 알고리즘 사용
model = NearestNeighbors(metric='cosine', algorithm='brute')
model.fit(user_book_matrix)  # 사용자-책 매트릭스를 모델에 학습시키기

# 추천 대상 사용자 ID
target_user_id = 1

# 대상 사용자의 좋아요 벡터를 2차원 배열 형태로 추출 (모델 입력 형식에 맞춤)
# user_book_matrix.loc[target_user_id] : 사용자 행 1개 가져오기
# .values                              : 판다스 -> 넘파이로 변경(1차원)
# .reshape(1, -1)                      : 넘파이 1차원 -> 2차원변경(왜? model 함수는 2차원만 받아들임)
target_vector = user_book_matrix.loc[target_user_id].values.reshape(1, -1)

# 대상 사용자와 가장 비슷한 3명의 사용자 찾기 (본인 포함)
distances, indices = model.kneighbors(target_vector, n_neighbors=3)

print(f"\n사용자 {target_user_id}와 비슷한 사용자들:")
for i, (idx, dist) in enumerate(zip(indices[0], distances[0])):
    if user_book_matrix.index[idx] == target_user_id:
        continue  # 자기 자신은 제외
    print(f"{i}: 사용자 {user_book_matrix.index[idx]}, 거리: {dist:.3f}")

# 비슷한 사용자들의 ID 리스트 생성 (본인 제외)
similar_users = [user_book_matrix.index[idx] for idx in indices[0] if user_book_matrix.index[idx] != target_user_id]

# 대상 사용자가 아직 좋아요 누르지 않은 책(값이 0인 책) 필터링
target_user_likes = user_book_matrix.loc[target_user_id]
unliked_books = target_user_likes[target_user_likes == 0].index.tolist()

recommend_scores = {}  # 추천 점수를 담을 딕셔너리 초기화

for book in unliked_books:
    # 비슷한 사용자들이 좋아요 누른 횟수 합산 (해당 책 열의 값 합)
    score = user_book_matrix.loc[similar_users, book].sum()
    recommend_scores[book] = score  # 책 ID별 점수 저장

# 추천 점수를 기준으로 내림차순 정렬
recommendations = sorted(recommend_scores.items(), key=lambda x: x[1], reverse=True)

print("\n추천 책 목록:")
for book_id, score in recommendations:
    print(f"{books[book_id]} (추천 점수: {score})")
