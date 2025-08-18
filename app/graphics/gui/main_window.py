from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from vispy.app import Timer
from .control_panel.control_panel import ControlPanel
from ..canvas.simulation import SimulationCanvas

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, sim_canvas:SimulationCanvas, timer:Timer) -> None:

        self.timer = timer
        self.sim_canvas = sim_canvas
        super().__init__()

        # init central widget and layout
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(QtWidgets.QHBoxLayout())
        self.setCentralWidget(central_widget)
        self.setWindowTitle(self.sim_canvas.system.name)

        # init canvas
        central_widget.layout().addWidget(self.sim_canvas.canvas.native)

        # init control panel
        self.control_panel = ControlPanel(self.sim_canvas.system, self.timer)
        central_widget.layout().addWidget(self.control_panel, alignment=Qt.AlignmentFlag.AlignTop)

        