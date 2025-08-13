import pandas as pd  # pandas 라이브러리 임포트 (데이터프레임 처리용)
from sklearn.neighbors import NearestNeighbors  # sklearn에서 k-NN 모델 클래스 임포트


def create_user_book_matrix(df):
    # pivot_table을 사용해 사용자-책 행렬 생성 (행: user_id, 열: book_id, 값: liked)
    # 평가하지 않은 항목은 0으로 채움 (fill_value=0)
    return df.pivot_table(index='user_id', columns='book_id', values='liked', fill_value=0)


def train_knn_model(user_book_matrix):
    # NearestNeighbors 모델 생성 (metric='cosine', brute-force 방식)
    model = NearestNeighbors(metric='cosine', algorithm='brute')
    # 사용자-책 행렬을 입력 데이터로 모델 학습
    model.fit(user_book_matrix)
    # 학습된 모델 반환
    return model


def find_similar_users(model, user_book_matrix, target_user_id, n_neighbors=3):
    # 대상 사용자의 좋아요 벡터를 1xN 배열 형태로 가져오기
    target_vector = user_book_matrix.loc[target_user_id].to_numpy().reshape(1, -1)

    # k-NN으로 가장 가까운 n_neighbors명의 인덱스만 반환 (거리 정보는 제외)
    # 결과 예) [[0 1 2]]
    indices = model.kneighbors(target_vector, n_neighbors=n_neighbors, return_distance=False)
    print(indices)

    # 인덱스 번호를 실제 사용자 ID로 변환하며, 자기 자신은 제외
    similar_users = [
        user_book_matrix.index[idx]  # 인덱스 번호 -> 사용자 ID 변환
        for idx in indices[0]  # 첫 번째(유일한) 결과 리스트 순회
        if user_book_matrix.index[idx] != target_user_id  # 자기 자신 제외
    ]
    # 비슷한 사용자 ID 리스트 반환
    return similar_users


def get_unliked_books(user_book_matrix, target_user_id):
    # 대상 사용자의 좋아요 여부 벡터 가져오기 (책별 0 또는 1)
    target_user_likes = user_book_matrix.loc[target_user_id]
    # 좋아요 안 한 책(0인 책)의 인덱스(책 ID) 리스트 추출
    unliked_books = target_user_likes[target_user_likes == 0].index.tolist()
    # 리스트 반환
    return unliked_books


def calculate_recommend_scores(user_book_matrix, similar_users, unliked_books):
    # 추천 점수를 저장할 딕셔너리 초기화
    recommend_scores = {}
    # 대상 사용자가 안 좋아요한 책들을 하나씩 처리
    for book in unliked_books:
        # 비슷한 사용자들이 해당 책에 좋아요(1)를 누른 횟수 합산
        score = user_book_matrix.loc[similar_users, book].sum()
        # 책 ID별 추천 점수 저장
        recommend_scores[book] = score
    # 점수 딕셔너리 반환
    return recommend_scores


def recommend_books(recommend_scores, books, top_n=2):
    # 추천 점수를 내림차순 정렬 (튜플의 두 번째 값, 즉 점수를 기준으로)
    sorted_recommendations = sorted(recommend_scores.items(), key=lambda x: x[1], reverse=True)
    # 상위 top_n개 결과만 잘라서 반환
    return sorted_recommendations[:top_n]


# === 메인 실행 흐름 ===

# 예시 데이터: 사용자-책 좋아요 기록
data = {
    'user_id': [1, 1, 1, 2, 2, 3, 3, 4],  # 사용자 ID
    'book_id': [101, 102, 103, 101, 103, 102, 104, 105],  # 책 ID
    'liked': [1, 1, 0, 1, 1, 1, 1, 1]  # 좋아요 여부 (1: 좋아요, 0: 아니요)
}

# 책 ID와 이름 매핑 딕셔너리 (결과 출력용)
books = {
    101: '파이썬 입문',
    102: '자바 완전정복',
    103: '데이터 과학 기초',
    104: '웹 개발 시작하기',
    105: '머신러닝 핵심'
}

# pandas DataFrame으로 변환
df = pd.DataFrame(data)

# 사용자-책 행렬 생성
user_book_matrix = create_user_book_matrix(df)

# k-NN 모델 학습
model = train_knn_model(user_book_matrix)

# 추천 대상 사용자 ID 지정
target_user_id = 1

# 대상 사용자와 비슷한 사용자 리스트 얻기
similar_users = find_similar_users(model, user_book_matrix, target_user_id)

# 대상 사용자가 좋아요 안 한 책 리스트 얻기
unliked_books = get_unliked_books(user_book_matrix, target_user_id)

# 비슷한 사용자들의 좋아요 합산 점수 계산
recommend_scores = calculate_recommend_scores(user_book_matrix, similar_users, unliked_books)

# 추천 점수 기준 상위 2개 책 선정
recommendations = recommend_books(recommend_scores, books, top_n=2)

# 추천 결과 출력
print(f"사용자 {target_user_id}에게 추천할 책 상위 2개:")
for book_id, score in recommendations:
    print(f"{books[book_id]}")
