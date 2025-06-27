from vispy.scene import SceneCanvas, PanZoomCamera
from ...base.body import Body
import numpy as np

class EnergyCanvas:

    def __init__(self, body:Body) -> None:
        self.body = body
        self.canvas = SceneCanvas()

        self.view = self.canvas.central_widget.add_view()
        self.view.camera = PanZoomCamera()
        self.view.camera.set_range()

        self.view.add(body.gpe_line)

    def update(self, time_array) -> None:
        self.body.gpe_line.set_data(np.column_stack((time_array, self.body.gpe_array)), self.body.gpe_line.colour, 5)
        self.view.camera.set_range()
