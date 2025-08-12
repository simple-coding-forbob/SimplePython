import pandas as pd

# 첫 번째 데이터프레임: 학생별 성적
df1 = pd.DataFrame({
    '국어': [90, 80, 70],
    '영어': [85, 75, 95]
}, index=['철수', '영희', '민수'])

# 두 번째 데이터프레임: 학생별 수학 성적
df2 = pd.DataFrame({
    '수학': [88, 92, 85]
}, index=['철수', '영희', '민수'])

print("df1:")
print(df1)

print("\ndf2:")
print(df2)

# 인덱스 기준으로 df2를 df1에 합치기 (기본 inner join)
joined_df = df1.join(df2)

print("\njoin 결과:")
print(joined_df)
