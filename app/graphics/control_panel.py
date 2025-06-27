from PyQt5 import QtWidgets
from ..base.system import System


class ControlPanel(QtWidgets.QWidget):

    def __init__(self, system:System, parent=None):
        super().__init__(parent)
        self.setFixedWidth(250)
        layout = QtWidgets.QVBoxLayout()

        # G 
        G_grp_box = QtWidgets.QGroupBox(title="G")
        G_grp_box_layout = QtWidgets.QHBoxLayout()
        G_grp_box.setLayout(G_grp_box_layout)
        G_grp_box.setObjectName("GGroupBox")
        G_grp_box.setStyleSheet("""
            QGroupBox {
                border: 2px solid black;
                border-radius: 5px;
                padding: 0px;
            }
            QGroupBox::title {
                subcontrol-position: top left;  
                background-color: transparent;  
                color: black;
            }
        """)

        G_value_label = QtWidgets.QLabel(str(system.G))
        G_grp_box_layout.addWidget(G_value_label)

        layout.addWidget(G_grp_box)

        self.data_labels = {}

        # init body mass widgets
        for i in range(len(system.bodies)):
            
            # body panel
            body_grp_box = QtWidgets.QGroupBox(system.bodies[i].name)
            body_grp_box_layout = QtWidgets.QVBoxLayout()
            body_grp_box.setLayout(body_grp_box_layout)
            body_grp_box.setObjectName("bodyGroupBox")

            body_grp_box.setStyleSheet("""
                QGroupBox  {
                    border: 2px solid black;
                    border-radius: 5px;
                    padding: 0px;
                }
                QGroupBox::title {
                    subcontrol-position: top left;  
                    background-color: transparent;  
                    color: black;
                }
            """)

            # body mass
            body_mass_panel = QtWidgets.QWidget()
            body_mass_layout = QtWidgets.QHBoxLayout()
            body_mass_panel.setLayout(body_mass_layout)

            body_mass_label = QtWidgets.QLabel("m")
            body_mass_value_label = QtWidgets.QLabel(str(system.bodies[i].mass))

            body_mass_layout.addWidget(body_mass_label)
            body_mass_layout.addWidget(body_mass_value_label)

            body_grp_box_layout.addWidget(body_mass_panel)

            self.data_labels[system.bodies[i].name] = body_mass_label

            layout.addWidget(body_grp_box)

        self.setLayout(layout)