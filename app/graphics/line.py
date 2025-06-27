from vispy.scene import visuals
import numpy as np

class Line(visuals.Line):

    def __init__(self, colour:str, width:int):
        self.colour = colour
        self._width = width

        super().__init__(color=self.colour, width=self._width)
        