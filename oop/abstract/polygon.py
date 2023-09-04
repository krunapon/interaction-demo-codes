# Python program showing 
# abstract base class work 
  
from abc import ABC, abstractmethod 


class Polygon(ABC): 
    @abstractmethod
    def __init__(self, name):
        self.name = name

    # abstract method
    @abstractmethod
    def __str__(self):
        pass


class Triangle(Polygon): 
    def __init__(self):
        super().__init__("Triangle")

    # overriding abstract method 
    def __str__(self):
       return f"{self.name} has 3 sides"


class Pentagon(Polygon): 
    def __init__(self):
        super().__init__("Triangle")

    # overriding abstract method 
    def __str__(self):
        return f"{self.name} has 5 sides"


class Hexagon(Polygon): 
    def __init__(self):
        super().__init__("Hexagon")

    # overriding abstract method 
    def __str__(self):
        return f"{self.name} has 6 sides"


class Quadrilateral(Polygon): 
    def __init__(self):
        super().__init__("Quadrilateral")

    # overriding abstract method 
    def __str__(self):
        return f"{self.name} has 4 sides"


# Driver code
if __name__ == "__main__":
    #polygon = Polygon()
    triangle = Triangle()
    quad = Quadrilateral()
    pentagon = Pentagon()
    hexagon = Hexagon()
    polygons = [triangle, quad, pentagon, hexagon]
    for shape in polygons:
        print(shape)
