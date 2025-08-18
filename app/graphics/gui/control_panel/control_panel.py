from PyQt5 import QtWidgets
from ....base.system import System
from .system_panel import SystemPanel
from .bodies_panel import BodiesPanel
from vispy.app import Timer
from ...utils import utils


class ControlPanel(QtWidgets.QWidget):

    def __init__(self, system:System, timer:Timer):
        self.timer = timer
        self.system = system
        super().__init__()

        self.setObjectName("controlPanel")
        self.setLayout(QtWidgets.QVBoxLayout())
        self.setStyleSheet(utils.load_css("app/graphics/gui/stylesheets/control_panel.css"))

        # system panel label
        self.layout().addWidget(QtWidgets.QLabel("System Properties"))

        # system panel
        self.system_panel = SystemPanel(self.system, self.timer)
        self.layout().addWidget(self.system_panel)

        # bodies label
        self.layout().addWidget(QtWidgets.QLabel("Body Properties"))

        # bodies panel
        self.bodies_panel = BodiesPanel(self.system)

        # bodies scroll area
        self.bodies_scroll_area = QtWidgets.QScrollArea()
        self.bodies_scroll_area.setWidget(self.bodies_panel)
        self.bodies_scroll_area.setWidgetResizable(True)
        self.layout().addWidget(self.bodies_scroll_area)