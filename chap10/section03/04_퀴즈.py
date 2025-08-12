import pandas as pd
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
df = pd.DataFrame(emp_data)

# MANAGER가 NULL (NaN) 인 행 필터링
result = df.loc[df["MANAGER"].isna()]

print(result)
