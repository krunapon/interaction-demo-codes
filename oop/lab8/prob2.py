import sys
sys.path.append("geometry")
import geometry.area as area
import geometry.shape as shape

circle1 = shape.Circle("blue", 3)
print("Circle with radius {} has area as {}".
      format(circle1.radius,
             round(area.get_circle_area(circle1.radius), 2)))

rect1 = shape.Rectangle("green", 3, 4)
print("Rectangle with width {} and height {} has area as {}".
      format(rect1.width, rect1.height,
             round(area.get_rectangle_area(rect1.width, rect1.height), 2)))





