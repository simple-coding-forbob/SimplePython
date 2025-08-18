import pandas as pd
from dept import dept_data
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
dept_df = pd.DataFrame(dept_data)
emp_df = pd.DataFrame(emp_data)

# 1. 'ACCOUNTING' 의 부서 번호(DNO) 조회
sales_dno_list = dept_df.loc[dept_df['DNAME'] == 'ACCOUNTING', 'DNO']

# 2. DNO가ACCOUNTING 인 사원의 ENAME, SALARY 조회
result = emp_df.loc[emp_df['DNO'].isin(sales_dno_list),['ENAME', 'SALARY']]

print(result)
