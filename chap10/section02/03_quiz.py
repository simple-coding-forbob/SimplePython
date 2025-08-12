import pandas as pd
from emp import emp_data

df = pd.DataFrame(emp_data)

# 날짜 타입 변환
df["HIREDATE"] = pd.to_datetime(df["HIREDATE"])

# 조건: HIREDATE가 1987-01-01 이상인 사원 필터링
result = df.loc[df["HIREDATE"] >= "1987-01-01"]

print(result)
