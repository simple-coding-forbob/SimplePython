import numpy as np

a = np.array([10, 20])
b = np.array([1, 2])

# 배열끼리 사칙연산
print("덧셈:", a + b)      # [11 22]
print("뺄셈:", a - b)      # [ 9 18]
print("곱셈:", a * b)      # [10 40]
print("나눗셈:", a / b)    # [10. 10.]

# 배열과 숫자끼리 연산: 브로드캐스팅 연산
print("각 요소에 +1:", a + 1)   # [11 21]