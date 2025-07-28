import pandas as pd

# 딕셔너리로 데이터 생성
data = {
    '이름': ['홍길동', None],
    '나이': [None, 30],
}

# 데이터 프레임 생성
df = pd.DataFrame(data)

# 결측값을 0으로 대체
df_filled = df.fillna(0)
print(df_filled)

