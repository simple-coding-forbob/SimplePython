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

# 조건: df[조건식] : 조건식이 true 인것만 화면에 나타남
print(df[df['직업']=='학생'])
print()

# 조건: df[조건식] : 조건식이 true 인것만 화면에 나타남
print(df[df['직업'].isin(['학생','직장인'])])