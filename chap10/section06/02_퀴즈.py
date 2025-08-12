import pandas as pd
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
df = pd.DataFrame(emp_data)

df["HIREDATE"] = pd.to_datetime(df["HIREDATE"])

# 가장 오래된 입사일 구하기
min_hiredate = df["HIREDATE"].min()

print(f"가장 오래된 입사일: {min_hiredate}")
