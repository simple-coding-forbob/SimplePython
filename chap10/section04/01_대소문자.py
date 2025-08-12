import pandas as pd
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
df = pd.DataFrame(emp_data)

# 대문자 변환
df["DNAME_UPPER"] = df["DNAME"].str.upper()

# 소문자 변환
df["DNAME_LOWER"] = df["DNAME"].str.lower()

# 첫 글자만 대문자 (INITCAP)
df["DNAME_INITCAP"] = df["DNAME"].str.title()

print(df[["DNAME_UPPER", "DNAME_LOWER", "DNAME_INITCAP"]])
