from app.extended.system import *
from app.graphics.canvases import SimulationCanvas
from app.graphics.control_panel import ControlPanel
from app.graphics.main_window import MainWindow
from vispy.app import use_app, Timer


if __name__ == "__main__":
    system = SunEarthMoonRealistic()

    app = use_app("pyqt5")
    app.create()

    sim_canvas = SimulationCanvas(system)
    main_win = MainWindow(sim_canvas)

    def update_all(timer_event):
        system.update()
        sim_canvas.update()

    timer = Timer(1/60, connect=update_all, start=True)
    main_win.show()
    app.run()
