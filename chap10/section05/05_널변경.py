import pandas as pd
from emp import emp_data

df = pd.DataFrame(emp_data)

# NVL과 같은 기능: NaN 또는 None을 0으로 채우기
df["COMMISSION_NVL"] = df["COMMISSION"].fillna(0)

print(df[["COMMISSION", "COMMISSION_NVL"]])
