from vispy.scene import SceneCanvas, TurntableCamera, PanZoomCamera, FlyCamera, ArcballCamera
from ..base.system import System
import time
import numpy as np


class Canvas():

    def __init__(self, system:System) -> None:
        self.system = system
        self.canvas = SceneCanvas(keys="interactive")

        self.view = self.canvas.central_widget.add_view()
        #self.view.camera = "turntable"
        self.view.camera = TurntableCamera()
        
        for i in range(len(self.system.bodies)):
            body = self.system.bodies[i]

            body.scatter.parent = self.view.scene
            #body.scatter.transform.translate(body.r.reshape(1, 3))
            body.scatter.set_data(body.r.reshape(1, 3), size=body.scatter.size, face_color=body.scatter.face_colour)

            body.trail.line.parent = self.view.scene
            body.trail.line.set_data(np.stack(body.trail.r_array),  color=body.trail.colour, width=body.trail.width)
            
        self.view.camera.set_range()
        self.view.camera.center = (0, 0, 0)

    def update(self, timer_event) -> None:
        
        #start_counter = time.perf_counter()
        self.system.update()

        for i in range(len(self.system.bodies)):
            body = self.system.bodies[i]
            body.scatter.set_data(body.r.reshape(1, 3), size=body.scatter.size, face_color=body.scatter.face_colour)
            #body.scatter.transform.translate(body.r.reshape(1, 3))
            #body.scatter.update()
            body.trail.line.set_data(np.stack(body.trail.r_array), color=body.trail.colour, width=body.trail.width) 
        
        #self.view.camera.set_range()

        #end_counter = time.perf_counter()
        #print(end_counter - start_counter)
