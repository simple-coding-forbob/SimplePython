import pandas as pd
from emp import emp_data

# 1️⃣ EMPLOYEE 데이터 (앞 8명 예시)
df = pd.DataFrame(emp_data)

# ENAME이 'S'로 시작하는 행 필터링
result = df.loc[df["ENAME"].str.startswith("S")]

print(result)


# ENAME에 'S'가 포함된 행 필터링 (대소문자 구분)
result = df.loc[df["ENAME"].str.contains("S")]

print(result)

# 두 번째 글자가 'A'인지 확인 (인덱스 1 위치 글자 비교)
result = df.loc[df["ENAME"].str[1] == 'A']

print(result)
