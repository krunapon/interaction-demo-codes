import numpy as np
a = np.arange(12)
print(a)
print(a[:2])
print(a[::2])
print(a[5:11])
a[5:11] = -1
print(a)
print(a[[4,5,7]])