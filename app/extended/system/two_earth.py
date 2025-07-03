from ...base.system import System
from ..body import Earth
from ...graphics import scalars
import numpy as np


class TwoEarth(System):

    TIMESTEP = 60
    G = 6.6743e-11

    def __init__(self) -> None:
        bodies = [
            Earth([-4.2227e7 / 2, 0, 0], [0, -3070 / 2, 0], name="Earth 1"),
            Earth([4.2227e7 / 2, 0, 0], [0, 3070 / 2, 0], name="Earth 2"),
        ]
        bodies[0].scatter.colour = np.array([1, 0.7, 0, 1])
        super().__init__(name="Two Earth", bodies=bodies, timestep=self.TIMESTEP, camera_centre=np.array([0, 0, 0]), plot_scale=scalars.M, G=self.G)
