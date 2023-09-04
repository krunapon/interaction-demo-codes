import sys
from functools import reduce
x = int(sys.argv[1])
input_list = map(lambda x: x + 1, range(x))
print(f"With the argument as {x}, the input list is {list(input_list)}")
result = map(lambda x: reduce(lambda x,y: x * y, map(lambda x: x + 1, range(x))),
                              map(lambda x: x + 1, range(x)))
print(f"The factorial numbers are {list(result)}")

