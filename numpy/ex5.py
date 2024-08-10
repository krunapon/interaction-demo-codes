import numpy as np
#Generate a matrix with two rows and three columns, filled with random numbers between 1 and 100 (inclusive).
a = np.random.randint(1, 101, (2, 3))
print(a)
#Calculate the mean of the entire matrix.
print(a.mean())
#Calculate the mean of each row.
print(a.mean(axis=1))   # axis=1 means row
#Determine which row has the highest average value.
print(a.mean(axis=1).argmax())
