import pandas as pd
from dept import dept_data
from emp import emp_data

dept_df = pd.DataFrame(dept_data)

# 조건: DNO == 30 AND DNAME == 'SALES'
result_dept = dept_df.loc[(dept_df["DNO"] == 30) & (dept_df["DNAME"] == "SALES")]

print(result_dept)

# 2) 급여(SALARY)가 1000 이상 1500 이하인 사원 조회
emp_df = pd.DataFrame(emp_data)

# 조건: SALARY >= 1000 AND SALARY <= 1500
result_salary = emp_df.loc[(emp_df["SALARY"] >= 1000) & (emp_df["SALARY"] <= 1500)]

print(result_salary)


