import pandas as pd

# 딕셔너리로 데이터 생성
data = {
    '이름': ['홍길동', None],
    '나이': [None, 30],
}

# 데이터 프레임 생성
df = pd.DataFrame(data)

# 결측값이 있는 행 삭제
df_cleaned = df.dropna()
# 결측값이 있는 열 삭제
df_cleaned = df.dropna(axis=1)
print(df_cleaned)

