import pandas as pd
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
df = pd.DataFrame(emp_data)

# COMMISSION이 NULL (NaN) 인 행 필터링
result_null = df.loc[df["COMMISSION"].isna()]

print(result_null)

# COMMISSION이 NULL이 아닌 행 필터링
result_not_null = df.loc[df["COMMISSION"].notna()]

print(result_not_null)
