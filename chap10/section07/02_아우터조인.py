import pandas as pd
from dept import dept_data
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
dept_df = pd.DataFrame(dept_data)
emp_df = pd.DataFrame(emp_data)

# 1. RIGHT OUTER JOIN (E.DNO = D.DNO)
merged_df = pd.merge(emp_df, dept_df, on='DNO', how='right')
print(merged_df)
# 2. LEFT OUTER JOIN (E.DNO = D.DNO)
merged_df2 = pd.merge(emp_df, dept_df, on='DNO', how='left')
print(merged_df2)
# 3. FULL OUTER JOIN (E.DNO = D.DNO)
merged_df3 = pd.merge(emp_df, dept_df, on='DNO', how='outer')
print(merged_df3)
