from PyQt5 import QtWidgets
from ....base.system import System
from .body_panel import BodyPanel

class BodiesPanel(QtWidgets.QWidget):

    def __init__(self, system:System) -> None:
        self.system = system
        super().__init__()
        self.setObjectName("parentPanel")
        self.setLayout(QtWidgets.QVBoxLayout())
        self.body_panels = []

        for i in range(len(self.system.bodies)):
            body_panel = BodyPanel(self.system.bodies[i])
            self.layout().addWidget(body_panel)
            self.body_panels.append(body_panel)

    def update_body_r_v_texts(self) -> None:
        for i in range(len(self.body_panels)):
            self.body_panels[i].update_r_v_texts()