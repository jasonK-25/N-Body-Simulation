from vispy.scene.visuals import Markers
from vispy import scene


class Scatter(Markers):

    def __init__(self, size:int, face_colour:str):
        self.size = size
        self.face_colour = face_colour

        super().__init__()
        
#class Scatter(Sphere):
#
#    def __init__(self, radius:int, colour:str):
#        self.radius = radius
#        self.colour = colour
#
#        super().__init__(color=self.colour, radius=self.radius, edge_color="white")
#        self.transform = scene.transforms.MatrixTransform()


