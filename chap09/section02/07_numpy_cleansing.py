import numpy as np

# 중복된 값이 있는 배열
arr = np.array([1, 2, 2])

# 중복 제거
unique_arr = np.unique(arr)
print(unique_arr)