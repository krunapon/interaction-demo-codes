class Circle:
    """
    A class representing a circle.

    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius):
        """
        Initialize a Circle instance.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return 3.14159 * self.radius**2


print(__doc__)
print(Circle.__doc__)
print(Circle.__init__.__doc__)
print(Circle.area.__doc__)
