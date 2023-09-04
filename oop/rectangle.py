class Rectangle:
     # Initializer / Instance Attributes
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def compute_area(self):
        return self.width * self.height

    def compute_reference(self):
        return 2 * (self.width + self.height)

    def description(self):
        print("This rectangle has width as {} and height as {}"
              .format(self.width, self.height))


rectangle1 = Rectangle(2,3)
rectangle1.description()
print("It has area as {} and circumference as {}".format(
        rectangle1.compute_area(), rectangle1.compute_reference()
))
