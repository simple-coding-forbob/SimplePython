import pandas as pd
from dept import dept_data

df_dept = pd.DataFrame(dept_data)
print(df_dept)

# 넘파이 배열로 변환
arr = df_dept.to_numpy()  # 또는 df.values
print(arr)