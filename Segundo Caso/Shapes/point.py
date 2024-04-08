class Point:
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y

    def move(self, new_x, new_y):
        self.__x = new_x
        self.__y = new_y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y