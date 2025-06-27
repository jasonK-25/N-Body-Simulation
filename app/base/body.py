import numpy as np
from ..graphics.scatter import Scatter
from .trail import Trail

class Body:

    def __init__(self, name:str, mass:float, init_pos:list, init_vel:list, scatter:Scatter=None, trail:Trail=None) -> None:
        self.name = name
        self.scatter = scatter
        self.trail = trail
        self.trail.append(init_pos)

        self.mass = mass
        self.init_pos = np.array(init_pos)
        self.init_vel = np.array(init_vel)

        self.r = self.init_pos
        self.v = self.init_vel
        self.a = np.array([0, 0, 0])
        self.force = np.array([0, 0, 0])
        
        self.r_array = [init_pos]
    