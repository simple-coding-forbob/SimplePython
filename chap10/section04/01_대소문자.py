import pandas as pd
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
df = pd.DataFrame(emp_data)

# 대문자 변환
df["ENAME_UPPER"] = df["ENAME"].str.upper()

# 소문자 변환
df["ENAME_LOWER"] = df["ENAME"].str.lower()

# 첫 글자만 대문자 (INITCAP)
df["ENAME_INITCAP"] = df["ENAME"].str.title()

print(df[["ENAME", "ENAME_UPPER", "ENAME_LOWER", "ENAME_INITCAP"]])
