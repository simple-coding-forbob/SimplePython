import pandas as pd
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
df = pd.DataFrame(emp_data)

# ENAME 오름차순 정렬
result_asc = df.sort_values(by="ENAME")

print(result_asc)

# ENAME 내림차순 정렬
result_desc = df.sort_values(by="ENAME", ascending=False)

print(result_desc)
