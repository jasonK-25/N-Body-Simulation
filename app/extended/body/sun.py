from ...base.body import Body
from ...graphics.base.scatter import Scatter
from ...graphics.base.trail import Trail
import numpy as np

class Sun(Body):

    def __init__(self, init_pos:list, init_vel:list, plot_colour=[1, 0.7, 0, 1], plot_size=40) -> None:
        radius = 6.5991e8
        super().__init__("Sun", 1.9889e30, radius, init_pos, init_vel,
        Scatter(size=40, colour=plot_colour),
        Trail(colour=np.array([1, 1, 1, 1])))

        
