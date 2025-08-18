from app.extended.system import SunEarthMoon, TwoEarthCollision
from vispy.app import use_app, Timer
from app.graphics.canvas.simulation import SimulationCanvas
from app.graphics.gui.main_window import MainWindow


if __name__ == "__main__":

    # init system
    #system = TwoEarthCollision()
    system = SunEarthMoon()
    #print(system.get_collision_groups())
    #exit()

    # create app
    app = use_app("pyqt5")
    app.create()

    # create canvas
    sim_canvas = SimulationCanvas(system)

    def update(timer_event=None) -> None:
        system.check_elastic_collision()
        system.update()
        sim_canvas.update()
        main_win.control_panel.bodies_panel.update_body_r_v_texts()

    # create timer
    timer = Timer(1/60, connect=update, start=True, iterations=-1)

    # create main window
    main_win = MainWindow(sim_canvas, timer)

    # start application
    timer.start()
    main_win.show()
    app.run()
    