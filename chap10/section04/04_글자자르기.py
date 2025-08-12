import pandas as pd
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
df = pd.DataFrame(emp_data)

# DNAME에서 첫 2글자 추출 (인덱스 0부터 2 미만)
df["FIRST_2_CHARS"] = df["DNAME"].str[0:2]

print(df[["DNAME", "FIRST_2_CHARS"]])
