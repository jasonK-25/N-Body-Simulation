from app.extended.system import *
from app.graphics.canvases import SimulationCanvas
from app.graphics.control_panel import ControlPanel
from app.graphics.main_window import MainWindow
from vispy.app import use_app, Timer


if __name__ == "__main__":

    # initialise system
    system = TwoEarth()

    # create app
    app = use_app("pyqt5")
    app.create()
    
    sim_canvas = SimulationCanvas(system)

    def update_all(timer_event):
        system.update()
        sim_canvas.update()

    timer = Timer(1/60, connect=update_all, start=True, iterations=-1)
    main_win = MainWindow(sim_canvas, timer)    

    main_win.show()
    app.run()
