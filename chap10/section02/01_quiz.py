import pandas as pd

# DEPARTMENT 데이터
dept_data = {
    "DNO": [10, 20, 30, 40],
    "DNAME": ["ACCOUNTING", "RESEARCH", "SALES", "OPERATIONS"],
    "LOC": ["NEW YORK", "DALLAS", "CHICAGO", "BOSTON"]
}
df_dept = pd.DataFrame(dept_data)

# EMPLOYEE 데이터 (8명)
emp_data = {
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
df_emp = pd.DataFrame(emp_data)

# 1) 부서테이블에서 DNO가 20보다 큰 부서만 표시
result1 = df_dept.loc[df_dept["DNO"] > 20, ["DNO", "DNAME", "LOC"]]
print(result1)

# 2) 사원테이블에서 DNO가 10인 사원 전체 출력
result2 = df_emp.loc[df_emp["DNO"] == 10]
print(result2)

# 3) 3) 사원테이블에서 월급이 5000인 사람 이름 출력
result3 = df_emp.loc[df_emp["SALARY"] == 5000, ["ENAME"]]
print(result3)

