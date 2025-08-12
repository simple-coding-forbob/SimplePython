import pandas as pd
from emp import emp_data

df = pd.DataFrame(emp_data)

# 문자열 -> datetime 변환
df["HIREDATE"] = pd.to_datetime(df["HIREDATE"])

# 날짜를 문자열 포맷으로 변환
df["HIREDATE_STR"] = df["HIREDATE"].dt.strftime("%Y-%m-%d %H:%M:%S")

print(df[["ENAME", "HIREDATE_STR"]])
