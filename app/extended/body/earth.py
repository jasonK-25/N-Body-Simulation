from ...base.body import Body
from ...graphics.base.scatter import Scatter
from ...graphics.base.trail import Trail
import numpy as np


class Earth(Body):

    def __init__(self, init_pos:list, init_vel:list, plot_colour=[0, 0, 1, 1], plot_size=20, name="Earth") -> None:
        radius = 6.3781e6
        super().__init__(name, 5.972e24, radius, init_pos, init_vel,
        Scatter(size=20, colour=plot_colour),
        Trail(colour=np.array([1, 1, 1, 1])))

        
