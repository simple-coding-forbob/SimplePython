import pandas as pd

# 1️⃣ DEPARTMENT 데이터 예시
data = {
    "DNO": [10, 20, 30, 40],
    "DNAME": ["ACCOUNTING", "RESEARCH", "SALES", "OPERATIONS"],
    "LOC": ["NEW YORK", "DALLAS", "CHICAGO", "BOSTON"]
}

# 2️⃣ DataFrame 생성
df = pd.DataFrame(data)

# 3️⃣ 부서명 컬럼만 조회
print(df["DNAME"])        # 시리즈 형태(1차원 배열, 컬럼명없음)
print(df[["DNAME"]])      # 데이터프레임 형태(2차원 배열, 컬럼명있음)
print(df[["DNAME", "LOC"]])