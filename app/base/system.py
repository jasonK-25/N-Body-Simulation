from .body import Body
from typing import List
import numpy as np


class System:

    def __init__(self, name:str, bodies:List[Body], timestep:float, camera_distance:float, G=6.6743e-11) -> None:
        
        # system property
        self.name = name
        self.bodies = bodies
        self.dt = timestep
        self.G = G
        self.time = 0

        # array
        self.time_array = [0]

        # initial gravitation
        self.eval_gravitation()

    def cleanup(self):

        # reset temporary body variables
        for i in range(len(self.bodies)):
            self.bodies[i].a = np.array([0, 0, 0])
            self.bodies[i].force = np.array([0, 0, 0])
            self.bodies[i].ke = None
            self.bodies[i].gpe = None
        
    def eval_gravitation(self):
        self.cleanup()

        for i in range(len(self.bodies)):
            for j in range(i + 1, len(self.bodies)):
                body1 = self.bodies[i]      
                body2 = self.bodies[j]

                r_12 = body2.r - body1.r
                r_12_mag = np.linalg.norm(r_12)

                F_12_mag = self.G * body1.mass * body2.mass / r_12_mag**2 
                F_12 = F_12_mag / r_12_mag * r_12 
                
                body1.force = body1.force + F_12
                body2.force = body2.force - F_12

                gpe = -F_12_mag * r_12_mag
                body1.gpe = body1.gpe + gpe if body1.gpe != None else gpe
                body2.gpe = body2.gpe + gpe if body2.gpe != None else gpe

        # add gpe to array
        for i in range(len(self.bodies)):
            body = self.bodies[i]
            body.ke_array.append(body.ke)
            body.gpe_array.append(body.gpe)

    def update(self):
        
        # update r, v, a
        for i in range(len(self.bodies)):
            body = self.bodies[i]

            body.a = body.force / body.mass
            body.v = body.v + (body.a * self.dt)
            body.r = body.r + (body.v * self.dt)
            body.ke = 0.5 * body.mass * np.linalg.norm(body.v)**2

            #body.r = body.r + (body.v * self.dt) + ((body.a * self.dt**2) / 2)
            #body.v = body.v + (body.a * self.dt)

            # add r to array
            body.r_array.append(body.r)
            body.trail.append(body.r)

        # update system time
        self.time += self.dt
        self.time_array.append(self.time)

        # prepare for next update
        self.eval_gravitation()



       
        
