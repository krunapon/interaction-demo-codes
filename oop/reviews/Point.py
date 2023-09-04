import math
from functools import total_ordering
@total_ordering
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # display x and y instead of address
        return f'Point(x={self.x}, y={self.y})'

    @property
    def distance(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def __lt__(self, other):
        # p1 < p2 calls p1.__lt__(p2)
        return self.distance < other.distance

    def __eq__(self, other):
        # p1 == p2 calls p1.__eq__(p2)
        return self.distance == other.distance
print(sorted([
    Point(0, 1), Point(3, 0), Point(1, 0), Point(2, 0)
]))
