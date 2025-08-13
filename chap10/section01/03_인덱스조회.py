import pandas as pd

# 1️⃣ DEPARTMENT 데이터 예시
data = {
    "DNO": [10, 20, 30, 40],
    "DNAME": ["ACCOUNTING", "RESEARCH", "SALES", "OPERATIONS"],
    "LOC": ["NEW YORK", "DALLAS", "CHICAGO", "BOSTON"]
}

# 2️⃣ DataFrame 생성
df = pd.DataFrame(data)

# 3️⃣ 전체 조회
print(df)

# 인덱스 번호 조회
print(list(df.index))

# 인덱스 0번만 조회
print(df.index[0])
