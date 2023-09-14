# add 10 to argument a, and return the result
x = lambda a : a + 10
print(x(5))
# lambda functions can take any number of arguments
x = lambda a, b : a * b
print(x(5, 6))
x = lambda a, b, c: a + b + c   
print(x(5, 6, 2))
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))
mytripler = myfunc(3)
print(mytripler(11))
