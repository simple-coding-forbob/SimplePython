import pandas as pd

# 딕셔너리로 데이터 생성
data = {
    '이름': ['홍길동', '홍길동', '장길산'],
    '나이': [30, 30, 25],
}

# 데이터 프레임 생성
df = pd.DataFrame(data)

# 중복된 행 삭제
df_unique = df.drop_duplicates()
print(df_unique)
