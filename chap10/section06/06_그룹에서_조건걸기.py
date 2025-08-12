import pandas as pd
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
df = pd.DataFrame(emp_data)

# 부서별 최고 급여 계산
grouped = df.groupby("DNO")["SALARY"].max().reset_index()

# HAVING 조건 (최고 급여가 3000 이상인 부서만 필터링)
result = grouped[grouped["SALARY"] >= 3000]

print(result)
