import pandas as pd
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
df = pd.DataFrame(emp_data)

# 부서별, 직급별 사원 수 구하기
count_by_dept_job = df.groupby(["DNO", "JOB"])["ENAME"].count().reset_index()

# 부서번호(DNO) 기준 오름차순 정렬
count_by_dept_job_sorted = count_by_dept_job.sort_values(by="DNO")

print(count_by_dept_job_sorted)
