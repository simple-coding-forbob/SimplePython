import pandas as pd
from emp import emp_data

df_emp = pd.DataFrame(emp_data)
print(df_emp)

# 사원 직위 급여 피봇
pivot_emp_job = df_emp.pivot(index="ENAME", columns="JOB", values="SALARY")
print(pivot_emp_job)
