import pandas as pd
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
df = pd.DataFrame(emp_data)

# 급여 총합과 최고액 계산
total_salary = df["SALARY"].sum()
max_salary = df["SALARY"].max()

# 결과 출력
print(f"총액: {total_salary}")
print(f"최고액: {max_salary}")
