import numpy as np
#create a 4x5 array of even numbers: 10, 12, 14, …
a = 10 + 2*np.arange(20).reshape(4,5)
print(a)
#extract third column
print(a[:,2])
#set the fourth row to 1,2,3,4,5
a[3] = [1,2,3,4,5]
print(a)