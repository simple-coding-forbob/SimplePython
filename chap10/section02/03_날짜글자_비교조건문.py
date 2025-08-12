import pandas as pd
from emp import emp_data

df = pd.DataFrame(emp_data)

# HIREDATE 컬럼을 날짜(datetime) 타입으로 변환
df["HIREDATE"] = pd.to_datetime(df["HIREDATE"])

# 조건: HIREDATE가 1981-01-01 이전 또는 같은 날짜인 행 선택
result = df.loc[df["HIREDATE"] <= "1981-01-01"]

print(result)
