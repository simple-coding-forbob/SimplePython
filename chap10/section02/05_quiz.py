import pandas as pd
from emp import emp_data

df = pd.DataFrame(emp_data)

# 조건: DNO가 20이거나 OR JOB이 'MANAGER'인 사원 필터링
result1 = df.loc[(df["DNO"] == 20) | (df["JOB"] == "MANAGER")]

print(result1)

# 조건: SALARY < 1000 OR SALARY > 1500
result2 = df.loc[(df["SALARY"] < 1000) | (df["SALARY"] > 1500)]

print(result2)
