import pandas as pd
from dept import dept_data
from emp import emp_data

# 1️⃣ DEPARTMENT , EMPLOYEE 데이터
dept_df = pd.DataFrame(dept_data)
emp_df = pd.DataFrame(emp_data)

# 2️⃣ 조건 조회 (SALARY >= 1500) 후 ENAME, SALARY 컬럼만 선택
result = emp_df.loc[emp_df["SALARY"] >= 1500, ["ENAME", "SALARY"]]

# 3️⃣ 출력
print(result)
