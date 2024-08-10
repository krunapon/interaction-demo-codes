import numpy as np
a = np.array([1, 2, 7, 8])
i = np.array([True, False, True, False])
print(a)
print(a[i])
i = a > 5
print(a[i])
print(a[a > 5])