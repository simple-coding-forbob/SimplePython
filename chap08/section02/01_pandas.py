import pandas as pd

# 딕셔너리로 데이터 생성
data = {
    '이름': ['홍길동', '김철수'],
    '나이': [25, 30],
    '직업': ['학생', '직장인']
}

# 데이터 프레임 생성
df = pd.DataFrame(data)

# 출력
print(df)
print(df.head())  # 기본적으로 상위 5개 행 출력
print(df.info())  # 데이터 구조 보기