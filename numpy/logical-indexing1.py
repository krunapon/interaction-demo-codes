import numpy as np
a = np.random.randn(2,3)
print(a)
a[a < 0] = 0
print(a)
a[a > 0] = np.array([1, 2, 3])
print(a)