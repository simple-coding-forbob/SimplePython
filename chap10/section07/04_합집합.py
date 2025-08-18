import pandas as pd
from dept import dept_data
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
dept_df = pd.DataFrame(dept_data)
emp_df = pd.DataFrame(emp_data)

# 두 데이터프레임을 행 방향으로 합치기 (UNION ALL)
result = pd.concat([dept_df[['DNO']], emp_df[['DNO']]])

print(result)
