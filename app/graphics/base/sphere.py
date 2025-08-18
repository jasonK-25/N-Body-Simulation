from vispy.scene.visuals import Sphere as _Sphere
from vispy.visuals.transforms import STTransform
import numpy as np


class Sphere(_Sphere):

    def __init__(self, radius:float, colour:list) -> None:
        self.colour = colour
        super().__init__(radius, color=colour, shading=None)

    def move(self, pos:np.ndarray) -> None:
        self.transform = STTransform(translate=pos)
