import pandas as pd
from dept import dept_data
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
dept_df = pd.DataFrame(dept_data)
emp_df = pd.DataFrame(emp_data)

# 두 데이터프레임을 행 방향으로 합치기 (UNION)
# TODO: .reset_index(drop=True) : 인덱스번호 다시 매김
result = pd.concat([dept_df['DNO'], emp_df['DNO']]).drop_duplicates().reset_index(drop=True)

print(result)
