import pandas as pd

# 1️⃣ EMPLOYEE 데이터 (앞 8명만)
data = {
    "ENO": [7369, 7499, 7521, 7566, 7654, 7698, 7782, 7788],
    "ENAME": ["SMITH", "ALLEN", "WARD", "JONES", "MARTIN", "BLAKE", "CLARK", "SCOTT"],
    "JOB": ["CLERK", "SALESMAN", "SALESMAN", "MANAGER", "SALESMAN", "MANAGER", "MANAGER", "ANALYST"],
    "MANAGER": [7902, 7698, 7698, 7839, 7698, 7839, 7839, 7566],
    "HIREDATE": [
        "1980-12-17", "1981-02-20", "1981-02-22", "1981-04-02",
        "1981-09-28", "1981-05-01", "1981-06-09", "1987-07-13"
    ],
    "SALARY": [800, 1600, 1250, 2975, 1250, 2850, 2450, 3000],
    "COMMISSION": [None, 300, 500, None, 1400, None, None, None],
    "DNO": [20, 30, 30, 20, 30, 30, 10, 20]
}

# 2️⃣ DataFrame 생성
df = pd.DataFrame(data)

# 3️⃣ 전체 조회
print(df)

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
# 0~2행, ENAME 컬럼만
print("0행, ENAME 컬럼만 조회:")
print(df.loc[0, 'ENAME'])
