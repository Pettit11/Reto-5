from math import atan2, degrees, pi

from Shapes.line import Line 

from line import Line 

from shape import Shape

class triangle(Shape):
    def __init__(self, side1, side2, side3):
        super().__init__(is_regular=None)
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3