from PyQt5 import QtWidgets
from ...base.system import System
from ... import utils
from .system_panel import SystemPanel
from .bodies_panel import BodiesPanel
    

class ControlPanel(QtWidgets.QWidget):

    def __init__(self, system:System, timer, parent=None):
        self.timer = timer
        self.system = system
        super().__init__(parent)
        
        self.setObjectName("controlPanel")
        self.setStyleSheet(utils.load_css("app/graphics/stylesheets/control_panel.css"))
        
        self.setLayout(QtWidgets.QVBoxLayout())

        # system panel label
        system_panel_label = QtWidgets.QLabel("System Properties")
        self.layout().addWidget(system_panel_label)

        # system panel
        self.system_panel = SystemPanel(self.system, self.timer)
        self.layout().addWidget(self.system_panel)

        # bodies label
        bodies_panel_label = QtWidgets.QLabel("Body Properties")
        self.layout().addWidget(bodies_panel_label)
        
        # bodies panel
        self.bodies_panel = BodiesPanel(self.system)
        
        # bodies scroll area
        bodies_scroll_area = self.build_bodies_scroll_area(self.bodies_panel)
        self.layout().addWidget(bodies_scroll_area)

    def build_bodies_scroll_area(self, widget:QtWidgets.QWidget) -> QtWidgets.QScrollArea:
        bodies_scroll_area = QtWidgets.QScrollArea()
        bodies_scroll_area.setWidget(widget)
        bodies_scroll_area.setWidgetResizable(True)
        return bodies_scroll_area

   