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

# 전체 행을 대상으로 오름 차순하기
df=df.sort_values(by='직업')
print(df)
print()


# 전체 행을 대상으로 내림 차순하기
df=df.sort_values(by='직업',ascending=False)
print(df)
print()

# 직업 열을 오름 차순으로 변경
# 결과 중 몇개만 보기: head(숫자)
users = df['직업'].sort_values().head(2)
print(users)
print()


# 직업 열을 내림 차순으로 변경
# ascending=False : 내림차순
users = df['직업'].sort_values(ascending=False).head(2)
print(users)
print()
