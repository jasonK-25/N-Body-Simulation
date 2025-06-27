from app.extended.system import *
from app.graphics.canvas import Canvas
from app.graphics.control_panel import ControlPanel
from app.graphics.window import MainWindow
from vispy.app import use_app, Timer

system = SunEarthMoonRealistic()

if __name__ == "__main__":
    app = use_app("pyqt5")
    app.create()

    canvas = Canvas(system)
    win = MainWindow(canvas)
    
    timer = Timer(1/60, connect=canvas.update, start=True)
    #for _ in range(365):
    #    canvas.update(None)

    win.show()
    app.run()
