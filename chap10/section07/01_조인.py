import pandas as pd
from dept import dept_data
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
dept_df = pd.DataFrame(dept_data)
emp_df = pd.DataFrame(emp_data)

# 1. INNER JOIN (EMPLOYEE.DNO = DEPARTMENT.DNO)
merged_df = pd.merge(emp_df, dept_df, on='DNO', how='inner')

# 2. 사원번호(ENO)가 7788인 행만 필터
result_df = merged_df[merged_df['ENO'] == 7788]

print(result_df)
