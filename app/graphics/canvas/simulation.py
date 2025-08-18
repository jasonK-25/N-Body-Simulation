from ...base.system import System
from vispy.scene import SceneCanvas, TurntableCamera
import numpy as np
from ...base.body import Body


class SimulationCanvas:

    def __init__(self, system:System) -> None:
        self.system = system
        self.canvas = SceneCanvas(keys="interactive")
        self.view = self.canvas.central_widget.add_view()
        self.view.camera = TurntableCamera()

        # add sphere and trail to canvas
        for i in range(len(self.system.bodies)):
            body = self.system.bodies[i]
            self.view.add(body.plot)
            self.view.add(body.trail)

        self.update()
        self.view.camera.set_range()

    def update(self) -> None:

        for i in range(len(self.system.bodies)):
            body = self.system.bodies[i]

            # plot body
            body.plot.set_data((body.pos / self.system.plot_scale).reshape(1, 3), size=body.plot.size, face_color=body.plot.colour)
            #body.sphere.move(body.pos / self.system.plot_scale)

            # plot trail
            trail_pos_array = np.vstack(body.trail.data)
            body.trail.set_data(np.stack(trail_pos_array / self.system.plot_scale), color=body.trail.colour, width=body.trail.width)

        # set focus (camera centre)
        if isinstance(self.system.focus, Body):
            self.view.camera.center = self.system.focus.pos / self.system.plot_scale
        elif isinstance(self.system.focus, np.ndarray):
            self.view.camera.centre = self.system.focus / self.system.plot_scale
        else:
            self.view.camera.centre = np.array([0, 0, 0])
