from geometry.geometry import Geometry
from core.obj_reader import my_obj_reader
import random
import OpenGL.GL as GL

class Garfo(Geometry):

    def __init__(self):
        super().__init__()
        color_data = []
        self.position_data = my_obj_reader('garfo.obj')
        colors = [(0.5, 0.5, 0.5), (0.0, 0.7, 0.0)]  
        for vertex in self.position_data:
            if vertex[0] < 0 and vertex[2] > 0:
                color_data.extend(colors[0])
            else:
                color_data.extend((random.uniform(0.0, 1.0), random.uniform(0.0, 1.0), random.uniform(0.0, 1.0)))
        self.add_attribute("vec3", "vertexPosition", self.position_data)
        self.add_attribute("vec3", "vertexColor", color_data)
        self.count_vertices()

