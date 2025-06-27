import numpy as np
from ..graphics.scatter import Scatter
from ..graphics.line import Line
from .trail import Trail

class Body:

    def __init__(self, name:str, mass:float, init_pos:list, init_vel:list, scatter:Scatter, trail:Trail, gpe_line:Line, ke_line:Line, tot_energy_line:Line) -> None:
        
        # body property
        self.name = name
        self.mass = mass
        self.init_pos = np.array(init_pos)
        self.init_vel = np.array(init_vel)

        self.r = self.init_pos
        self.v = self.init_vel
        self.a = np.array([0, 0, 0])
        self.force = np.array([0, 0, 0])
        self.gpe = None
        self.ke = None

        # array
        self.r_array = [init_pos]
        self.gpe_array = []
        self.ke_array = []

        # GUI
        self.scatter = scatter
        self.trail = trail
        self.trail.append(init_pos)

        self.ke_line = ke_line
        self.gpe_line = gpe_line
        self.energy_line = tot_energy_line

