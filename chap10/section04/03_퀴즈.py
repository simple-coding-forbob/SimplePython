import pandas as pd
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
df = pd.DataFrame(emp_data)

# 'Oracle '과 JOB 문자열 붙이기
df["NEW_JOB"] = "Oracle " + df["JOB"]

print(df[["JOB", "NEW_JOB"]])
