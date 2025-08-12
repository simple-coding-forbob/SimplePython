import pandas as pd
from emp import emp_data

df = pd.DataFrame(emp_data)

# 조건: DNO가 10이거나 OR JOB이 'MANAGER'인 사원 필터링
result = df.loc[(df["DNO"] == 10) | (df["JOB"] == "MANAGER")]

print(result)
