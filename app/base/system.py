from typing import List
from .body import Body
import numpy as np
import math


class System:

    def __init__(self, name:str, bodies:List[Body], timestep:float, plot_scale:float, G:float, focus, trails_visible=True) -> None:

        # system property
        self.name = name
        self.bodies = bodies
        self.timestep = timestep
        self.G = G
        self.t_array = [0]

        # counter
        self.merge_body_counter = 0
        self.colliding_body_pair_index = []
        
        # GUI
        self.plot_scale = plot_scale
        self.focus = focus
        self.trails_visible = trails_visible
        self.set_trails_visible(self.trails_visible)

        # compute initial gravitation
        self.compute_gravitation()    

    def set_trails_visible(self, is_visiible) -> None:
        self.trails_visible = is_visiible

        for i in range(len(self.bodies)):
            self.bodies[i].trail.set_visible(self.trails_visible)
                
    def reset_body_temp_variables(self) -> None:
        for i in range(len(self.bodies)):
            self.bodies[i].acc = np.array([0, 0, 0])
            self.bodies[i].force = np.array([0, 0, 0])
            self.bodies[i].gpe = 0

    def check_elastic_collision(self) -> None:
        for i in range(len(self.bodies)):
            body1 = self.bodies[i]

            for j in range(i + 1, len(self.bodies)):
                body2 = self.bodies[j]

                r_12 = body2.pos - body1.pos
                r_12_mag = np.linalg.norm(r_12)

                # unflag pair after collision
                if r_12_mag > body1.radius + body2.radius and [i, j] in self.colliding_body_pair_index:
                    self.colliding_body_pair_index.remove([i, j])

                # check overlapping => collision
                if r_12_mag <= body1.radius + body2.radius:

                    # skip if body pair has already collided but overlapping due to timestep error
                    if [i, j] in self.colliding_body_pair_index:
                        continue

                    # resolve collision
                    self.colliding_body_pair_index.append([i, j])

                    r_12_hat = r_12 / r_12_mag

                    u1_parallel_abs = np.dot(body1.vel, r_12_hat) 
                    u2_parallel_abs = np.dot(body2.vel, r_12_hat)

                    u1_parallel = u1_parallel_abs * r_12_hat
                    u2_parallel = u2_parallel_abs * r_12_hat

                    u1_n = body1.vel - u1_parallel
                    u2_n = body2.vel - u2_parallel

                    v1_parallel_abs = (((body1.mass - body2.mass) * u1_parallel) + (2 * body2.mass * u2_parallel)) / (body1.mass + body2.mass)
                    v2_parallel_abs = (((body2.mass - body1.mass) * u2_parallel) + (2 * body1.mass * u1_parallel)) / (body1.mass + body2.mass)

                    v1_parallel = v1_parallel_abs * r_12_hat
                    v2_parallel = v2_parallel_abs * r_12_hat

                    v1 = v1_parallel + u1_n
                    v2 = v2_parallel + u2_n

                    body1.vel = v1
                    body2.vel = v2

    def compute_gravitation(self) -> None:
        self.reset_body_temp_variables()

        for i in range(len(self.bodies)):
            body1 = self.bodies[i]

            for j in range(i + 1, len(self.bodies)):
                body2 = self.bodies[j]

                r_12 = body2.pos - body1.pos
                r_12_mag = np.linalg.norm(r_12)
                r_12_hat = r_12 / r_12_mag
                
                F_12_mag = self.G * body1.mass * body2.mass / r_12_mag**2
                F_12 = F_12_mag * r_12_hat

                body1.force = body1.force + F_12
                body2.force = body2.force - F_12

                body1.gpe += -F_12_mag * r_12_mag
                body2.gpe += -F_12_mag * r_12_mag
        
        for i in range(len(self.bodies)):
            self.bodies[i].gpe_line.append(self.bodies[i].gpe)
            
    def update(self) -> None:

        # update pos, vel, acc
        for i in range(len(self.bodies)):
            body = self.bodies[i]

            # resolve temp variables
            body.acc = body.force / body.mass
            body.vel = body.vel + (body.acc * self.timestep)
            body.pos = body.pos + (body.vel * self.timestep)
            
            # update data list
            body.vel_list.append(body.vel)
            body.trail.append(body.pos)

        # update time array
        self.t_array.append(self.t_array[-1] + self.timestep)

        # prepare for next update
        self.compute_gravitation()