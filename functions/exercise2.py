import math
# 1. Create a function called hypotenuse, which takes two numbers as parameters and prints the square root of the sum of their squares.
# 2. Call this function with two floats.
# 3. Call this function with two integers.
# 4. Call this function with one integer and one float.

def hypotenuse(a, b):
    print("Sqrt({}^2 + {}^2) = {}".format(a, b, math.sqrt(a**2  + b**2)))
hypotenuse(3.0, 4.0)
hypotenuse(3, 4)
hypotenuse(3, 4.0)
