import numpy as np
from ..graphics.base.scatter import Scatter
from ..graphics.base.trail import Trail
#from ..graphics.base.sphere import Sphere


class Body:

    def __init__(self, name:str, mass:float, radius:float, init_pos:list, init_vel:list, plot:Scatter, trail:Trail) -> None:

        # body property
        self.name = name
        self.mass = mass
        self.radius = radius
        self.init_pos = np.array(init_pos)
        self.init_vel = np.array(init_vel)

        # current status
        self.pos = self.init_pos
        self.vel = self.init_vel
        self.acc = np.array([0, 0, 0])
        self.force = np.array([0, 0, 0])
        self.gpe = 0
        self.in_collision = False


        # data lists
        self.vel_list = [self.init_vel]
        self.gpe_list = []
        
        # GUI
        self.plot = plot
        self.trail = trail
        self.trail.append(init_pos)  
        self.ke_line = Trail([1, 1, 1, 1], -1)  
        self.gpe_line = Trail([1, 1, 1, 1], -1)  

    def plot_energy(self, t_array):
        from matplotlib import pyplot as plt
        
        kes = [0.5 * self.mass * (vel**2) for vel in self.vels]
        plt.plot(t_array, kes, label="ke")
        plt.plot(t_array, self.gpes, label="gpe")
        plt.plot(t_array, [kes[i] + self.gpes[i] for i in range(len(t_array))], label="total")

        plt.legend()
        plt.show()