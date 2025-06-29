from vispy.scene import SceneCanvas, TurntableCamera
from vispy import scene, color
from ...base.system import System
import numpy as np
from .. import scalars
from ...base.body import Body


class SimulationCanvas:

    def __init__(self, system:System) -> None:
        self.system = system
        self.scalar = 10 * scalars.AU
        self.canvas = SceneCanvas(keys="interactive")

        self.view = self.canvas.central_widget.add_view()
        self.view.camera = TurntableCamera()
        #self.view.camera = PanZoomCamera()

        for i in range(len(self.system.bodies)):
            body = self.system.bodies[i]

            body.scatter.parent = self.view.scene
            #body.scatter.transform.translate(body.r.reshape(1, 3))
            body.scatter.set_data((body.r / self.scalar).reshape(1, 3), size=body.scatter.size, face_color=body.scatter.colour)

            body.trail.line.parent = self.view.scene
            trail_r_array = np.vstack(body.trail.r_array)
            body.trail.line.set_data(np.stack(trail_r_array / self.scalar),  color=body.trail.colour, width=body.trail.width)
            
        self.view.camera.set_range()
        self.view.camera.center = (0, 0, 0)

    def update(self) -> None:
        
        for i in range(len(self.system.bodies)):
            body = self.system.bodies[i]
            body.scatter.set_data((body.r / self.scalar).reshape(1, 3), size=body.scatter.size, face_color=body.scatter.colour)
            #body.scatter.transform.translate(body.r.reshape(1, 3))
            #body.scatter.update()

            trail_r_array = np.vstack(body.trail.r_array)
            body.trail.line.set_data(np.stack(trail_r_array / self.scalar), color=body.trail.colour, width=body.trail.width) 
            
            if self.system.camera_centre_body_index in range(len(self.system.bodies)):
                self.view.camera.center = self.system.bodies[self.system.camera_centre_body_index].r / self.scalar
            else:
                self.view.camera.center = np.array([0, 0, 0])