# 좋아요/안좋아요 양자 택일 기반 추천: 코사인 유사도 추천
import pandas as pd
from sklearn.neighbors import NearestNeighbors

# 협업 필터링
# 샘플 데이터 생성 (forbob4 제외)
data={
    'email': [
        'forbob@naver.com', 'forbob@naver.com',
        'forbob2@naver.com', 'forbob2@naver.com'
    ],
    'file_title': [
        '제목1', '제목2',
        '제목2', '제목3'
    ],
    'like_count': [1, 1, 1, 1]  # 모두 1
}

# 0) 판다스딕셔너리 만들기
df = pd.DataFrame(data)
print(df)

# 1) 사용자-책 행렬 만들기
mx = df.pivot_table(index='email', columns='file_title', values='like_count', fill_value=0)
print(mx)
print()

# 2) KNN 모델 학습
model = NearestNeighbors(metric='cosine', algorithm='brute')
model.fit(mx.to_numpy())

# 3) 추천 대상 사용자 지정
temail = 'forbob@naver.com'
temail_idx = mx.index.get_loc(temail)                         # 인덱스이름으로 위치 얻기
np=mx.to_numpy()                                              # 넘파이 배열로 바꾸기
tfeature = np[temail_idx].reshape(1, -1)                      # (1행, n열)짜리 배열로 변환(유사 사용자 찾기 함수때문에 필요)

# 4) Top-N 유사 사용자 찾기
# indices.flatten() : 다차원 -> 1차원으로 변경
dt, inx     = model.kneighbors(tfeature, n_neighbors=2)       # 자기 자신 포함 인덱스번호가 리턴됨
similar_idx = [i for i in inx.flatten() if i != temail_idx]   # 자기 자신 제외
semail      = [mx.index[i] for i in similar_idx]              # 인덱스번호에 해당되는 유저명 가져오기

# 5) 비슷한 사용자들이 좋아한 타이틀 합산 점수 계산
# SELECT file_title, SUM(like_count)
# FROM mx
# WHERE email IN (비슷한 유저들)
#   AND file_title NOT IN (내가 이미 좋아요한 타이틀)
# GROUP BY file_title;
rec_sum = {}
# 2) 내가 이미 좋아요한 타이틀
my_likes = df.loc[df['email'] == temail, 'file_title'].tolist()

# 3) 비슷한 사용자들이 좋아한 타이틀 합산
rec_sum = (
    df[df['email'].isin(semail) & ~(df['file_title'].isin(my_likes))]
      .groupby('file_title')['like_count'].sum()
)
print(rec_sum)
print()
# 4) Series 정렬 + Top-N 선택
top_N = rec_sum.sort_values(ascending=False).head(2)

# 7) 결과 출력: 배열로 바꾸어서 보기: 나중에 db 에 넣기
print(top_N.index.to_list())
