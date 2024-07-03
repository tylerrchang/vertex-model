class Cell:
    def __init__(self, vert_list):
        self.vert_obj_list = vert_list
        #self.__get_fake_poly()
    
    def __str__(self):
        return(f"Polygon with vertices: {self.vert_obj_list}")
    
    def __repr__(self):
        return self.__str__()

    def get_area(self):
        return self.__get_fake_poly().get_area()
    
    def get_perimeter(self):
        return self.__get_fake_poly().get_perimeter()