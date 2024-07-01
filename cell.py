class Cell:
    def __init__(self, vert_list, polygon):
        self.polygon = polygon
        self.vert_obj_list = vert_list
    
    def __str__(self):
        return(f"Polygon with vertices: {self.vert_obj_list}")
    
    def __repr__(self):
        return self.__str__()