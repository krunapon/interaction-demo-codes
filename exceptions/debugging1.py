import math
def hypotenuse(x, y):
    print("x is %f and y is %f" % (x, y))
    x_2 = x**2
    print(x_2)
    y_2 = y**2
    print(y_2)
    z_2 = x_2 + y_2
    print(z_2)
    z = math.sqrt(z_2)
    print(z)
    return z
hypotenuse(3, 4)
