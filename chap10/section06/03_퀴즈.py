import pandas as pd
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터
df = pd.DataFrame(emp_data)

# 행 개수 구하기
count1 = len(df)

print(f"행 개수 (len): {count1}")
