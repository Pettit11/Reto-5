from Shapes.point import Point

from Shapes.line import Line 

from Shapes.shape import Shape

from Rectangle import rectangle

class Square(rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

# Define points
point1 = Point(0, 0)
point2 = Point(4, 0)
point3 = Point(4, 4)
point4 = Point(0, 4)

# Create lines using points
line1 = Line(point1, point2)
line2 = Line(point2, point3)
line3 = Line(point3, point4)
line4 = Line(point4, point1)

# Create a square
square = Square(4)

# Calculate the area of the square
area = square.compute_area()
print("Area of the square:", area)

# Calculate the perimeter of the square
perimeter = square.compute_perimeter()
print("Perimeter of the square:", perimeter)