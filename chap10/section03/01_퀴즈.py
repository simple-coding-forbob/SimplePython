import pandas as pd
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
df = pd.DataFrame(emp_data)

# DNO가 10 이상 20 이하인 사원 필터링
result = df.loc[df["DNO"].between(10, 20)]
print(result)

# HIREDATE 컬럼을 datetime 타입으로 변환
df["HIREDATE"] = pd.to_datetime(df["HIREDATE"])

# 1981년 1월 1일부터 1981년 12월 31일 사이 입사한 사원 필터링
result_hiredate = df.loc[df["HIREDATE"].between("1981-01-01", "1981-12-31")]
print(result_hiredate)
