import pandas as pd
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
df = pd.DataFrame(emp_data)

# SALARY가 1000 이상 1500 이하인 행 필터링 (BETWEEN 포함 범위)
result = df.loc[df["SALARY"].between(1000, 1500)]

print(result)

# SALARY가 1000 이상 1500 이하가 아닌 사원 필터링 (NOT BETWEEN)
result = df.loc[~df["SALARY"].between(1000, 1500)]

print(result)
