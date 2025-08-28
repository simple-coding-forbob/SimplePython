import pandas as pd
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
df = pd.DataFrame(emp_data)

# ENAME 문자열 길이 구하기
df["JOB_LENGTH"] = df["JOB"].str.len()

# ENAME, 길이 출력
print(df[["JOB", "JOB_LENGTH"]])
