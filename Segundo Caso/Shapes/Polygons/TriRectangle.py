from Shapes.point import Point

from Shapes.line import Line 

from Shapes.shape import Shape

from Triangle import triangle

class TriRectangle(triangle):
    def __init__(self, base, height):
        super().__init__(base, height, (base ** 2 + height ** 2) ** 0.5)

# Define points
point1 = Point(0, 0)
point2 = Point(4, 0)
point3 = Point(0, 3)

# Create lines using points
line1 = Line(point1, point2)
line2 = Line(point2, point3)
line3 = Line(point3, point1)

# Create a triangle with a right angle
triangle_right = TriRectangle(4, 3)

# Calculate the area of the triangle
area = triangle_right.compute_area()
print("Area of the triangle with a right angle:", area)

# Calculate the perimeter of the triangle
perimeter = triangle_right.compute_perimeter()
print("Perimeter of the triangle with a right angle:", perimeter)

# Calculate the inner angles of the triangle
inner_angles = triangle_right.compute_inner_angles()
print("Inner angles of the triangle with a right angle:", inner_angles)