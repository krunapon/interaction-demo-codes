class Shape2D:
    def area(self):
        raise NotImplementedError()


class Shape3D:
    def volume(self):
        raise NotImplementedError()


class Square(Shape2D):
    def __init__(self, width):
        self.width = width

    def area(self):
       return self.width ** 2


square1 = Square(2)
print("Square(2) is {}".format(square1.area()))
shape1 = Shape2D()

