from Shapes.point import Point

from Shapes.line import Line 

from Shapes.shape import Shape

from Triangle import triangle


class Scalene(triangle):
    def __init__(self, side1, side2, side3):
        super().__init__(side1, side2, side3)

# Define points
point1 = Point(0, 0)
point2 = Point(4, 0)
point3 = Point(2, 3)

# Create lines using points
line1 = Line(point1, point2)
line2 = Line(point2, point3)
line3 = Line(point3, point1)

# Create a scalene triangle
scalene_triangle = Scalene(line1.compute_length(), line2.compute_length(), line3.compute_length())

# Calculate the area of the scalene triangle
area = scalene_triangle.compute_area()
print("Area of the scalene triangle:", area)

# Calculate the perimeter of the scalene triangle
perimeter = scalene_triangle.compute_perimeter()
print("Perimeter of the scalene triangle:", perimeter)