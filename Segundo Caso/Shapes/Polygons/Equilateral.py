from Shapes.point import Point

from Shapes.line import Line 

from Shapes.shape import Shape

from Triangle import triangle

class Equilateral(triangle):
    def __init__(self, side):
        super().__init__(side, side, side)




# Create points
point1 = Point(0, 0)
point2 = Point(3, 0)
point3 = Point(1.5, 3)

# Create lines using points
line1 = Line(point1, point2)
line2 = Line(point2, point3)
line3 = Line(point3, point1)

# Create a triangle
Triangle = triangle(line1, line2, line3)

# Calculate the area of the triangle
area = triangle.compute_area()
print("Area of the triangle:", area)

# Calculate the perimeter of the triangle
perimeter = triangle.compute_perimeter()
print("Perimeter of the triangle:", perimeter)

# Create an equilateral triangle
equilateral_triangle = Equilateral(5)

# Calculate the area of the equilateral triangle
equilateral_area = equilateral_triangle.compute_area()
print("Area of the equilateral triangle:", equilateral_area)

# Calculate the perimeter of the equilateral triangle
equilateral_perimeter = equilateral_triangle.compute_perimeter()
print("Perimeter of the equilateral triangle:", equilateral_perimeter)