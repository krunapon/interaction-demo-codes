import numpy as np;
oneCol = np.ones((5,))
zeroCols = np.zeros((5,2))
a = np.column_stack((oneCol,zeroCols))
print(a)