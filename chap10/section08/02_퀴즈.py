import pandas as pd
from emp import emp_data

df_emp = pd.DataFrame(emp_data)
print(df_emp)

# pivot_table: 부서(인덱스) 직무(필드) 급여(값), 집계(합)
pivot_emp = pd.pivot_table(
    df_emp,
    index="DNO",          # 행: 부서번호
    columns="JOB",        # 열: 직무
    values="SALARY",      # 값: 급여
    aggfunc="sum",       # 집계 함수: 합계
    fill_value=0          # NaN 대신 0
)

print(pivot_emp)