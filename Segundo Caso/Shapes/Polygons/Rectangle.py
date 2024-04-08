
from point import Point

from line import Line 

from shape import Shape

class rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(is_regular=False)
        self.__width = width
        self.__height = height

    def compute_area(self):
        return self.__width * self.__height

    def compute_perimeter(self):
        return 2 * (self.__width + self.__height)

    def compute_inner_angles(self):
        if self.get_is_regular():
            return [90, 90, 90, 90]
        else:
            return None

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

# Create points
point1 = Point(0, 0)
point2 = Point(3, 4)

# Create lines using the points
line1 = Line(point1, point2)

# Create a rectangle
rectangle = rectangle(5, 3)

# Calculate the area of the rectangle
area = rectangle.compute_area()
print("Area of the rectangle:", area)

# Calculate the perimeter of the rectangle
perimeter = rectangle.compute_perimeter()
print("Perimeter of the rectangle:", perimeter)

# Get the inner angles of the rectangle
inner_angles = rectangle.compute_inner_angles()
print("Inner angles of the rectangle:", inner_angles)

# Change the dimensions of the rectangle
rectangle.set_width(8)
rectangle.set_height(4)

# Recalculate the area of the rectangle after changing the dimensions
area = rectangle.compute_area()
print("New area of the rectangle:", area)
