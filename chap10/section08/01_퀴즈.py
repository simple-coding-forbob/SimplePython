import pandas as pd
from emp import emp_data

df_emp = pd.DataFrame(emp_data)
print(df_emp)

# 넘파이 배열로 변환
arr = df_emp.to_numpy()  # 또는 df.values
print(arr)