class Shape:
    def __init__(self, is_regular: bool):
        self.__is_regular = is_regular
        self.__vertices = []
        self.__edges = []
        self.__inner_angles = []

    def add_vertices(self, point):
        self.__vertices.append(point)

    def add_edges(self, line):
        self.__edges.append(line)

    def add_inner_angles(self, angles):
        self.__inner_angles = angles

    def compute_area(self):
        pass

    def compute_perimeter(self):
        pass

    def compute_inner_angles(self):
        pass

    def get_is_regular(self):
        return self.__is_regular

    def set_is_regular(self, is_regular):
        self.__is_regular = is_regular

    def get_vertices(self):
        return self.__vertices

    def get_edges(self):
        return self.__edges

    def get_inner_angles(self):
        return self.__inner_angles