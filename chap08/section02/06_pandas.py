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

# 피봇 테이블 만들기: 데이터를 특정 기준으로 다시 보여주는것, 다양한 형태로 보여줄 수 있습니다.
# 피봇 뜻: 1개를 고정하고 다른 것들을 바꾸는것
# TODO: 사용법: 변수 = 데이터프레임.pivot_table(데이터프레임변수, index, columns, aggFunc=(sum,mean,count, 람다식 등), fill_value=기본값)
df = pd.pivot_table(df, index='이름', columns='이름', aggfunc=lambda x:1, fill_value=0)
print(df)

