import pandas as pd
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
df = pd.DataFrame(emp_data)

# 문자열 붙이기 ('Oracle ' + DNAME)
df["NEW_DNAME"] = "Oracle " + df["DNAME"]

print(df[["DNAME", "NEW_DNAME"]])
