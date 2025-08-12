import pandas as pd
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
df = pd.DataFrame(emp_data)

# 조건: COMMISSION이 300, 500, 1400 중 하나인 행 필터링
result = df.loc[df["COMMISSION"].isin([300, 500, 1400])]

print(result)

# COMMISSION이 300, 500, 1400이 아닌 값 필터링
# NaN 포함하려면 fillna 사용하거나 isna() 조건 추가 필요
result = df.loc[~df["COMMISSION"].isin([300, 500, 1400])]

print(result)
