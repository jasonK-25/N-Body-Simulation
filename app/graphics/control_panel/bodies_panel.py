from PyQt5 import QtWidgets
from ...base.system import System
from .body_panel import BodyPanel

class BodiesPanel(QtWidgets.QWidget):

    def __init__(self, system:System) -> None:
        self.system = system
        super().__init__()
        self.setObjectName("parentPanel")
        self.setLayout(QtWidgets.QVBoxLayout())

        for i in range(len(self.system.bodies)):
            body_panel = BodyPanel(self.system.bodies[i])
            self.layout().addWidget(body_panel)