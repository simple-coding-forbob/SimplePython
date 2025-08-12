import pandas as pd
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
df = pd.DataFrame(emp_data)

# DNAME 문자열 길이 구하기
df["DNAME_LENGTH"] = df["DNAME"].str.len()

# 출력
print(df[["DNAME", "DNAME_LENGTH"]])
