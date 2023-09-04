class Rectangle:
     def __init__(self, width, height):
        self.width = width
        self.height = height

     def area(self):
         return self.width * self.height

     def display(self):
         print("{}: width = {} height = {} area = {}".format(type(self).__name__,
                                                             self.width, self.height,
                                                                    self.area()))

class Square(Rectangle):
     def __init__(self, side):
         super().__init__(side, side)
         self.side = side


     def area(self):
         return self.side * self.side


class Cube(Square):
      def area(self):
          face_area = self.side * self.side
          return face_area * 6

      def volume(self):
         face_area = self.side * self.side
         return face_area * self.side

      def display(self):
         print("{}: side = {} area = {}".format(type(self).__name__,
                                                             self.side,
                                                             self.area()))

rect1 = Rectangle(2,3)
rect1.display()
square1 = Square(2)
square1.display()
cube1 = Cube(3)
cube1.display()

