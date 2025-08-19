import pandas as pd
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
df = pd.DataFrame(emp_data)

# 대문자 변환
df["대문자"] = df["JOB"].str.upper()

# 소문자 변환
df["소문자"] = df["JOB"].str.lower()

# 첫 글자만 대문자 (INITCAP)
df["첫대문자"] = df["JOB"].str.title()

print(df[["대문자", "소문자", "첫대문자"]])
