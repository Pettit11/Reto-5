class Line:
    def __init__(self, start, end):
        self.__start = start
        self.__end = end

    def compute_length(self):
        return ((self.__end.get_x() - self.__start.get_x()) ** 2 + (self.__end.get_y() - self.__start.get_y()) ** 2) ** 0.5

    def get_start(self):
        return self.__start

    def get_end(self):
        return self.__end