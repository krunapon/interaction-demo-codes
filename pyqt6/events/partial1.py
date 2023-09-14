from functools import partial
# a normal function
def f(a, b, c, x):
    return a + 2*b + 3*c - x

# a partial function that calls f with
# a as 3, b as 1, and c and 4
g = partial(f, 3, 1, 4) 
print(g(5)) # 3 + 2*1 + 3*4 - 5 = 12