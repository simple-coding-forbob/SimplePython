import pandas as pd
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
df = pd.DataFrame(emp_data)

# 평균 급여 구하고 반올림
avg_salary_rounded = df["SALARY"].mean().round(0)

# 최솟값 구하기
min_salary = df["SALARY"].min()

print(f"반올림한 평균 급여: {avg_salary_rounded}")
print(f"최소 급여: {min_salary}")
