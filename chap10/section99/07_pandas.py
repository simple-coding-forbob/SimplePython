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

# 열별 합계 구하기 (세로 합계)
col_sum = df.sum(axis=0)  # axis=0이 기본값이라 생략해도 됨

print("\n각 열별 합계:")
print(col_sum)
