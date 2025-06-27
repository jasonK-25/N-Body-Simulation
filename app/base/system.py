from .body import Body
from typing import List
import numpy as np


class System:

    def __init__(self, name:str, bodies:List[Body], timestep:float, camera_distance:float, G=6.6743e-11) -> None:
        self.name = name
        self.bodies = bodies
        self.dt = timestep
        self.G = G

        self.camera_distance = camera_distance

    def clean(self):
        for i in range(len(self.bodies)):
            self.bodies[i].a = np.array([0, 0, 0])
            self.bodies[i].force = np.array([0, 0, 0])
        
    def eval_G_force(self):
        self.clean()

        for i in range(len(self.bodies)):
            for j in range(i + 1, len(self.bodies)):
                
                body1 = self.bodies[i]                  
                body2 = self.bodies[j]

                r_12 = body2.r - body1.r
                r_12_mag = np.linalg.norm(r_12)

                F_12 = (self.G * body1.mass * body2.mass / r_12_mag**3) * r_12
                
                body1.force = body1.force + F_12
                body2.force = body2.force - F_12
                
    def update(self):

        self.eval_G_force()
        for i in range(len(self.bodies)):
            body = self.bodies[i]

            body.a = body.force / body.mass
            body.v = body.v + (body.a * self.dt)
            body.r = body.r + (body.v * self.dt)

            #body.r = body.r + (body.v * self.dt) + ((body.a * self.dt**2) / 2)
            #body.v = body.v + (body.a * self.dt)
            body.r_array.append(body.r)
            body.trail.append(body.r)

       
        
