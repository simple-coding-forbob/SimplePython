import pandas as pd

# 예제 데이터프레임 생성
data = {
    '과목': ['수학', '영어', '수학', '영어', '과학', '과학'],
    '학생': ['철수', '철수', '영희', '영희', '철수', '영희'],
    '점수': [90, 80, 85, 70, 95, 88]
}
df = pd.DataFrame(data)

print("원본 데이터:")
print(df)

# 과목별 평균 점수 구하기
grouped = df.groupby('과목')['점수'].mean()

print("\n과목별 평균 점수:")
print(grouped)

# 학생별 총 점수 구하기
grouped2 = df.groupby('학생')['점수'].sum()

print("\n학생별 총 점수:")
print(grouped2)
