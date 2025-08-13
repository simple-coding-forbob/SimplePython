import pandas as pd
from dept import dept_data
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
dept_df = pd.DataFrame(dept_data)
emp_df = pd.DataFrame(emp_data)

# 1. DEPARTMENT에서 필요한 컬럼만 선택
dept_sel = dept_df[['DNO']]

# 2. EMPLOYEE에서 필요한 컬럼만 선택하고 컬럼명 맞추기 (DNAME → ENAME → DNAME으로 맞춤)
emp_sel = emp_df[['DNO']]

# 3. 두 데이터프레임을 행 방향으로 합치기 (UNION ALL)
# TODO: .reset_index(drop=True) : 인덱스번호 다시 매김
result = pd.concat([dept_sel, emp_sel]).drop_duplicates().reset_index(drop=True)

print(result)
