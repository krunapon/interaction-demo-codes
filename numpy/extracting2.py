import numpy as np
c = np.arange(12).reshape((3,4))
print(c)
print(c[1,2])
print(c[1])
print(c[:,2])
print(c[:2])
print(c[:2, :3])