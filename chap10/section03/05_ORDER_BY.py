import pandas as pd
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
df = pd.DataFrame(emp_data)

# SALARY 오름차순 정렬 (기본값이 오름차순)
result_asc = df.sort_values(by="SALARY")

print(result_asc)

# SALARY 내림차순 정렬
result_desc = df.sort_values(by="SALARY", ascending=False)

print(result_desc)
