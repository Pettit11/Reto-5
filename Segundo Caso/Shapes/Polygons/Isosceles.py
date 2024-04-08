from Shapes.point import Point

from Shapes.line import Line 

from Shapes.shape import Shape

from Triangle import triangle

class Isosceles(triangle):
    def __init__(self, side, base):
        super().__init__(side, side, base)



# Create points
point1 = Point(0, 0)
point2 = Point(3, 0)
point3 = Point(1.5, 3)

# Create lines using points
line1 = Line(point1, point2)
line2 = Line(point2, point3)
line3 = Line(point3, point1)

# Create points
point1 = Point(0, 0)
point2 = Point(3, 0)
point3 = Point(1.5, 4)  # Adjusted the coordinates to make it an isosceles triangle

# Create lines using points
line1 = Line(point1, point2)
line2 = Line(point2, point3)
line3 = Line(point3, point1)

# Create an isosceles triangle
isosceles_triangle = Isosceles(3, 4)  # Assuming the base is 4 and the sides are 3

# Calculate the area of the isosceles triangle
isosceles_area = isosceles_triangle.compute_area()
print("Area of the isosceles triangle:", isosceles_area)

# Calculate the perimeter of the isosceles triangle
isosceles_perimeter = isosceles_triangle.compute_perimeter()
print("Perimeter of the isosceles triangle:", isosceles_perimeter)