import pandas as pd
from emp import emp_data

df = pd.DataFrame(emp_data)

# 조건: DNO가 10이 아닌 사원 선택
result = df.loc[~(df["DNO"] == 10)]

print(result)
