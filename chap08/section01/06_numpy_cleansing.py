import numpy as np

# 결측값이 있는 배열
arr = np.array([1, 2, None, 4], dtype=float)

# 결측값을 0으로 대체
arr_filled = np.nan_to_num(arr,nan=0)
print(arr_filled)

# 배열 생성
arr = np.array(['a', None, 'b'], dtype=object)

# None을 빈 문자열('')로 바꾸기
arr_filled = np.where(arr == None, '', arr)
print(arr_filled)