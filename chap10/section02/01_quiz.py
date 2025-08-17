import pandas as pd
from dept import dept_data
from emp import emp_data

# 1️⃣ DEPARTMENT , EMPLOYEE 데이터
df_dept = pd.DataFrame(dept_data)
df_emp = pd.DataFrame(emp_data)

# 1) 부서테이블에서 DNO가 20보다 큰 부서만 표시
result1 = df_dept.loc[df_dept["DNO"] > 20, ["DNO", "DNAME", "LOC"]]
print(result1)

# 2) 사원테이블에서 DNO가 10인 사원 전체 출력
result2 = df_emp.loc[df_emp["DNO"] == 10]
print(result2)

# 3) 3) 사원테이블에서 월급이 5000인 사람 이름 출력
result3 = df_emp.loc[df_emp["SALARY"] == 5000, ["ENAME"]]
print(result3)

