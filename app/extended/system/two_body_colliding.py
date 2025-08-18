from ...base.system import System
from ...base.body import Body
from ...extended.body import Earth
from ...graphics.base.scatter import Scatter
from ...graphics.base.trail import Trail
from ...graphics.utils import scalar


class TwoEarthCollision(System):
    TIMESTEP = 50
    G = 6.67e-11

    def __init__(self):
        bodies = [
            Earth([-4.2227e7 / 2, 0, 0], [0, 0, 0], name="Earth 1"),
            Earth([4.2227e7 / 2, 0, 0], [0, 0, 0], name="Earth 2"),
        ]
        bodies[0].plot.colour = [1, 0.7, 0, 1]
        super().__init__(name="2 body collision", bodies=bodies, timestep=self.TIMESTEP, plot_scale=scalar.M, G=self.G, focus=bodies[1])