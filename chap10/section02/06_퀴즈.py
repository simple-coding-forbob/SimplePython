import pandas as pd
from dept import dept_data

dept_df = pd.DataFrame(dept_data)

# 조건: DNO가 20이 아닌 부서 필터링
result = dept_df.loc[dept_df["DNO"] != 20]

print(result)
