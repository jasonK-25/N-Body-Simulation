from vispy.scene.visuals import Markers


class Scatter(Markers):

    def __init__(self, size:int, colour:str):
        self.size = size
        self.colour = colour

        super().__init__()
        
#class Scatter(Sphere):
#
#    def __init__(self, radius:int, colour:str):
#        self.radius = radius
#        self.colour = colour
#
#        super().__init__(color=self.colour, radius=self.radius, edge_color="white")
#        self.transform = scene.transforms.MatrixTransform()


