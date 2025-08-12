import pandas as pd
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
df = pd.DataFrame(emp_data)

# 직급별 급여 합계 계산
grouped = df.groupby("JOB")["SALARY"].sum().reset_index()

# HAVING 조건 (급여 합계 5000 이상 필터링)
result = grouped[grouped["SALARY"] >= 5000]

print(result)
