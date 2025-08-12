import pandas as pd
from emp import emp_data

df = pd.DataFrame(emp_data)

# 조건 조회: ENAME이 'SCOTT'인 사원 전체 정보 조회
result = df.loc[df["ENAME"] == "SCOTT"]

print(result)
