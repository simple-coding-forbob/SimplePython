import pandas as pd
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
df = pd.DataFrame(emp_data)

# 직급별 평균 급여 계산
avg_salary_by_job = df.groupby("JOB")["SALARY"].mean()

print(avg_salary_by_job)
