import  numpy as np
a = np.random.uniform(-1, 1, size=(3,4))  
print(a)
np.random.seed(1)
a = np.random.uniform(size=5)  # 1st batch of numbers
print(a)
a = np.random.uniform(size=5)  # 2nd batch is different
print(a)
np.random.seed(1)
a = np.random.uniform(size=5)  # repeat the 1st batch
print(a)