import pandas as pd
from emp import emp_data

df_emp = pd.DataFrame(emp_data)
print(df_emp)
print()
# 인덱스 보기
print(df_emp.index)
print()
# 컬럼들 보기
print(df_emp.columns)
print()
# (행,열) 처럼 보기
print(df_emp.loc[0,"ENO"])
print()
# index 배열, ENO 보기
print(df_emp.loc[df_emp.index,"ENO"])
print()

