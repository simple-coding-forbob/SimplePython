import pandas as pd
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
df = pd.DataFrame(emp_data)

# ENAME에 'M' 문자가 포함된 행 필터링 (대소문자 구분)
result_contains_m = df.loc[df["ENAME"].str.contains("M")]

print(result_contains_m)

# ENAME 두 번째 글자(인덱스 1)가 'O'인 행 필터링
result_second_o = df.loc[df["ENAME"].str[1] == "O"]

print(result_second_o)
