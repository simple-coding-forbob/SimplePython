import pandas as pd
from dept import dept_data
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
dept_df = pd.DataFrame(dept_data)
emp_df = pd.DataFrame(emp_data)

# 1. 조인 (E.DNO = D.DNO)
merged_df = pd.merge(dept_df, emp_df, on='DNO', how='inner')

# 2. 사원번호(ENO)가 7499인 행 필터
result_df = merged_df[merged_df['ENO'] == 7499]

# 3. 부서 컬럼만 출력 (dept_df에 있는 컬럼들만)
result_df = result_df[dept_df.columns]

print(result_df)
