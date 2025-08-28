import pandas as pd
from dept import dept_data

# 1️⃣ DEPARTMENT 데이터
df = pd.DataFrame(dept_data)

# 행 개수 구하기
count1 = len(df)
count1 = df.count() # None 이 있으면 None 은 빼고 셉니다.

print(f"행 개수 (len): {count1}")
