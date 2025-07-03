from vispy.scene.visuals import Line
import numpy as np


class Trail:

    def __init__(self, colour:np.ndarray, length=30, width=2) -> None:
        self.r_array = []
        self.colour = colour
        self.length = length
        self.width = width
        self.line = Line(color=colour, width=width)

    @property
    def visible(self) -> bool:
        return self.colour[-1] == 1
        
    def set_visible(self, is_visible:bool) -> None:
        if is_visible:
            self.colour[-1] = 1
        else:
            self.colour[-1] = 0

    def append(self, r) -> None:

        # limit trail length
        if len(self.r_array) >= self.length:
            self.r_array.pop(0)
            
        self.r_array.append(r)
