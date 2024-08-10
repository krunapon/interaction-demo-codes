import numpy as np;
firstRow = -1 * np.ones((1,4))
secondRow = np.zeros((1,4)) 
thirdRow = 2 * np.ones((1,4))
result = np.row_stack((firstRow,secondRow,thirdRow))
print(result)