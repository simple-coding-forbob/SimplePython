import pandas as pd
from emp import emp_data

# 1) 사원명(ENAME)이 'ALLEN'인 사원 전체 정보 출력
df = pd.DataFrame(emp_data)

# ENAME이 'ALLEN'인 사원 전체 정보 조회
result_allen = df.loc[df["ENAME"] == "ALLEN"]

print(result_allen)

# 2) 직위(JOB)가 'CLERK'인 사원 전체 정보 출력
# JOB이 'CLERK'인 사원 전체 정보 조회
result_clerk = df.loc[df["JOB"] == "CLERK"]

print(result_clerk)

