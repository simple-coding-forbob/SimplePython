import pandas as pd
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
df = pd.DataFrame(emp_data)

# 부서별, 직급별 급여 합계 구하기
grouped = df.groupby(["DNO", "JOB"])["SALARY"].sum().reset_index() # .reset_index() : 그룹화 결과를 DataFrame 형태로 변환

# 부서번호(DNO) 기준 오름차순 정렬
grouped_sorted = grouped.sort_values(by="DNO")

print(grouped_sorted)
