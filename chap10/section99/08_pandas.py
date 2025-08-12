import pandas as pd

# 예제 데이터프레임 생성
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data)

print("원본 데이터프레임:")
print(df)

# 행별 합계 구하기 (가로 합계)
row_sum = df.sum(axis=1)

print("\n각 행별 합계:")
print(row_sum)

