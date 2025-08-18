import numpy as np

x = np.array([1, 2, 3, 4])

y = x.reshape(1,4)
print(y)

z = y.flatten()
print(z)