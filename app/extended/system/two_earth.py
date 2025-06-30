from ...base.system import System
from ..body import Earth
from ...graphics import scalars
import numpy as np


class TwoEarth(System):

    TIMESTEP = 60
    G = 6.6743e-11

    def __init__(self) -> None:
        bodies = [
            Earth([-4.2227e7 / 2, 0, 0], [0, -3070 / 2, 0]),
            Earth([4.2227e7 / 2, 0, 0], [0, 3070 / 2, 0]),
        ]
        super().__init__("Two Earth", bodies, self.TIMESTEP, None, scalars.M, self.G, np.array([0, 0, 0]))
