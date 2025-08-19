import pandas as pd

# 딕셔너리로 데이터 생성
data = {
    '이름': ['홍길동', '장길산'],
    '나이': [None, 30],
}

# 데이터 프레임 생성
df = pd.DataFrame(data)
print(df)
print()

# 결측값이(None) 있는 행 삭제
df_cleaned = df.dropna()
print(df_cleaned)
print()
# 결측값이 있는 열 삭제
# axis=1 (세로)
# axis=0 (가로)
df_cleaned2 = df.dropna(axis=1)
print(df_cleaned2)

