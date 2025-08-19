import pandas as pd
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터
df = pd.DataFrame(emp_data)

# DNO가 10 또는 20인 행 필터링
result_in = df.loc[df["DNO"].isin([10, 20])]

print(result_in)

# DNO가 10 또는 20이 아닌 행 필터링
result_not_in = df.loc[~df["DNO"].isin([10, 20])]

print(result_not_in)
