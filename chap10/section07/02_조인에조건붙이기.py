import pandas as pd
from dept import dept_data
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
dept_df = pd.DataFrame(dept_data)
emp_df = pd.DataFrame(emp_data)

# 1. INNER JOIN (E.DNO = D.DNO)
merged_df = pd.merge(emp_df, dept_df, on='DNO', how='inner')

# 2. ENO가 7499 또는 7900인 행 필터
result_df = merged_df[merged_df['ENO'].isin([7499, 7900])]

print(result_df)
