import pandas as pd
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
df = pd.DataFrame(emp_data)

# 문자열을 datetime 타입으로 변환
df["HIREDATE"] = pd.to_datetime(df["HIREDATE"])

# 가장 최근 입사일 구하기
max_hiredate = df["HIREDATE"].max()

print(f"가장 최근 입사일: {max_hiredate}")
