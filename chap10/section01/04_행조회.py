import pandas as pd

# === 1️⃣ DEPARTMENT 데이터 ===
data = {
    "DNO": [10, 20, 30, 40],
    "DNAME": ["ACCOUNTING", "RESEARCH", "SALES", "OPERATIONS"],
    "LOC": ["NEW YORK", "DALLAS", "CHICAGO", "BOSTON"]
}

df = pd.DataFrame(data)
print("전체 데이터:")
print(df)
print("\n")

# === 2️⃣ 인덱스로 행 조회 ===
# 0번째 행 조회
print("0번째 행 조회 (loc 사용):")
print(df.loc[0])
print("\n")

# 여러 행 조회 (0~1행)
print("0~1번째 행 조회 (loc 사용):")
print(df.loc[0:1])
print("\n")

# === 4️⃣ index 값 확인 ===
print("첫 번째 인덱스 라벨:")
print(df.index[0])
print("\n")

# === 5️⃣ 여러 행과 컬럼 선택 ===
# 0~2행, DNAME 컬럼만
print("0:1행, DNAME 컬럼만 조회:")
print(df.loc[0:1, 'DNAME'])
