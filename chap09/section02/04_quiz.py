import numpy as np

x = np.array([10, 20, 30, 40])

y = x.reshape(2,2)
print(y)

z = y.flatten()
print(z)