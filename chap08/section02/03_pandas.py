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

# 새로운 열 '국적' 1,2행 모두 추가
df['국적'] = ['한국', '한국']
print(df)
print()

# '나이'가 25 이상인 행만 선택
print(df[df['나이'] >= 30])