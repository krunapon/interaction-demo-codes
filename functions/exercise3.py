import math
# 1. Rewrite the hypotenuse function from exercise 2
# so that it returns a value instead of printing it.
# Add exception handling so that the function returns 
# None if it is called with parameters of the wrong type.
# 2. Call the function with two numbers, and print the result.
# 3. Call the function with two strings, and print the result.
# 4. Call the function with a number and a string, and print the result.

import math

def hypotenuse(x, y):
    try:
        return math.sqrt(x**2 + y**2)
    except TypeError:
        return None

print("hypotenuse({}, {}) is {}".format(3.0, 4.0, hypotenuse(3.0, 4.0)))
print("hypotenuse({}, {}) is {}".format("3", "4", hypotenuse("3", "4")))
print("hypotenuse({}, {}) is {}".format(3, "4.0", hypotenuse(3, "4.0")))

