import geometry
class Ideal_Polygon:
    def __init__(self, vert):
        self.vertices = self.__compute_verts(vert)
        self.perimeter = self.__compute_perimeter()
        self.area = self.__compute_area()

    def __compute_verts(vert_list):
        pass