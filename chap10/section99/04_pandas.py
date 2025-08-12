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

# '직업' 열에서 '학생'을 '대학교 학생'으로 수정
df['직업'] = df['직업'].replace('학생', '대학생')
print(df)
print()

# '국적' 열 삭제
df = df.drop(columns=['직업'])
print(df)

