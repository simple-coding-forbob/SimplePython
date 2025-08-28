import pandas as pd
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
df = pd.DataFrame(emp_data)

# ENAME 첫 2글자 추출
df["FIRST_2_CHARS"] = df["JOB"].str[0:2]

print(df[["JOB", "FIRST_2_CHARS"]])
