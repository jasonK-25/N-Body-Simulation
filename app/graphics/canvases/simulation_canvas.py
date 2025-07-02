from vispy.scene import SceneCanvas, TurntableCamera
from vispy import scene, color
from ...base.system import System
import numpy as np
from ...base.body import Body


class SimulationCanvas:

    def __init__(self, system:System) -> None:
        self.system = system
        self.canvas = SceneCanvas(keys="interactive")

        self.view = self.canvas.central_widget.add_view()
        self.view.camera = TurntableCamera()

        # place scatters and trails on canvas
        for i in range(len(self.system.bodies)):
            body = self.system.bodies[i]

            body.scatter.parent = self.view.scene
            body.trail.line.parent = self.view.scene

        self.update()
        self.view.camera.set_range()
            
    def update(self) -> None:
        
        for i in range(len(self.system.bodies)):
            body = self.system.bodies[i]

            # plot body
            body.scatter.set_data((body.r / self.system.plot_scale).reshape(1, 3), size=body.scatter.size, face_color=body.scatter.colour)
            #body.scatter.transform.translate(body.r.reshape(1, 3))
            #body.scatter.update()

            # plot trail
            trail_r_array = np.vstack(body.trail.r_array)
            body.trail.line.set_data(np.stack(trail_r_array / self.system.plot_scale), color=body.trail.colour, width=body.trail.width) 
            
            # set camera centre
            if isinstance(self.system.camera_centre, Body):
                self.view.camera.center = self.system.camera_centre.r / self.system.plot_scale
            else:
                self.view.camera.center = self.system.camera_centre / self.system.plot_scale
