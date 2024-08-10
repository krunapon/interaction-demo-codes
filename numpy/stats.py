import numpy as np
a = np.arange(12).reshape((3,4))
print(a)
print(a.sum())  # total sum
print(a.sum(axis=0))  # add rows, preserve columns
print(a.sum(axis=1))  # add columns, preserve rows
print(a.mean(axis=0))   
print(a.std(axis=0))  # standard deviation of 2nd column
print(a.var(axis=1))  #  varian of each row