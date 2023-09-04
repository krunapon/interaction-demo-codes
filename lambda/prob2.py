import sys
from functools import reduce
def factorial(x):
  list = map(lambda x: x + 1, range(x))
  result = reduce(lambda x,y: x * y, list)
  return result

num = int(sys.argv[1])
print(f"Factorial of ({num}) is {factorial(num)}")

