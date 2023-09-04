from add import add as f_add
from sub import sub as f_sub
from mult import mult as f_mult
from div import div as f_div


class Calculator:
    def __init__(self):
        pass

    def add(self, i1: int, i2: int) -> int:
        try:
            result = f_add(i1, i2)
            return int(result)
        except ValueError:
            print("There is an error when attempting to add {} with {}".
            format(i1, i2))
            return None

    def sub(self, i1: int, i2: int) -> int:
        try:
            result = f_sub(i1, i2)
            return int(result)
        except ValueError:
            print("There is an error when attempting to sub {} with {}".
            format(i1, i2))
            return None

    def mult(self, i1: int, i2: int) -> int:
        try:
            result = f_mult(i1, i2)
            return int(result)
        except ValueError:
            print("There is an error when attempting to multiply {} with {}".
            format(i1, i2))
            return None

    def div(self, i1: int, i2: int):
        try:
            result = f_div(i1, i2)
            return result
        except TypeError:
            print("There is an error when attempting to divide {} by {}".
            format(i1, i2))
            return None


cal1 = Calculator()
n1 = 2
n2 = 3
n0 = 0
print("{} + {} = {}".format(n1, n2, cal1.add(n1,n2)))
print("{} + {} = {}".format("n1", "n2", cal1.add("n1","n2")))
print("{} - {} = {}".format(n1, n2, cal1.sub(n1,n2)))
print("{} * {} = {}".format(n1, n2, cal1.mult(n1,n2)))
print("{} / {} = {}".format(n1, n2, cal1.div(n1,n2)))
print("{} / {} = {}".format(n1, n0, cal1.div(n1,n0)))
print("{} / {} = {}".format("n1", "n2", cal1.div("n1","n2")))
