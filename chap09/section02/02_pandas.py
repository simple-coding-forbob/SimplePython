import pandas as pd

# 딕셔너리로 데이터 생성
data = {
    '이름': ['홍길동', '김철수'],
    '나이': [25, 30],
    '직업': ['학생', '직장인']
}

# 데이터 프레임 생성
df = pd.DataFrame(data)
print(df)
print()

# '나이' 열만 선택
print(df['나이'])
print()

# 첫 번째 행 선택
print(df.loc[0])
print()