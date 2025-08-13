import pandas as pd
from dept import dept_data
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
dept_df = pd.DataFrame(dept_data)
emp_df = pd.DataFrame(emp_data)

# 1. 'SALES' 부서 번호(DNO) 조회
sales_dno_list = dept_df.loc[dept_df['DNAME'] == 'SALES', 'DNO']

# 2. 사원 중 DNO가 SALES 부서에 포함된 ENAME 조회
result = emp_df.loc[emp_df['DNO'].isin(sales_dno_list), 'ENAME']

print(result)
