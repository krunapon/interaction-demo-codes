import math

class Numbers:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def display(self):
        print("x = {} and y = {}".format(self.x, self.y))

    @classmethod
    def get_factors(cls, a):
        if a % 2 == 0:
            return cls(a/2, a/2)
        else:
            return cls(math.floor(a/2), math.floor(a/2) + 1)

    @staticmethod
    def is_valid_divisor(num):
        if num:
            return True
        else:
            return False

print(Numbers(3,5).add())
Numbers.get_factors(6).display()
Numbers.get_factors(8).display()
print(Numbers.is_valid_divisor(2))
print(Numbers.is_valid_divisor(0))
