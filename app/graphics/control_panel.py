from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QSize
from ..base.system import System
from ..base.body import Body
from ..import utils
import numpy as np


class ControlPanel(QtWidgets.QWidget):
    
    def build_system_grp_box(self) -> QtWidgets.QGroupBox:
        
        # system group box
        system_grp_box = QtWidgets.QGroupBox(title="System Properties")
        system_grp_box.setObjectName("parentGroupBox")
        system_grp_box_layout = QtWidgets.QGridLayout()
        system_grp_box.setLayout(system_grp_box_layout)

        # G
        G_value_textbox = QtWidgets.QTextEdit(str(self.system.G))
        system_grp_box_layout.addWidget(QtWidgets.QLabel("G:"), 0, 0)
        system_grp_box_layout.addWidget(G_value_textbox, 0, 1)

        # camera centre
        camera_centre_dropdown = QtWidgets.QComboBox()
        camera_centre_dropdown.addItems([body.name for body in self.system.bodies] + ["Custom"])
        system_grp_box_layout.addWidget(QtWidgets.QLabel("Focus:"))
        system_grp_box_layout.addWidget(camera_centre_dropdown, 1, 1)
        
        # custom camera centre coordinate textbox
        custom_camera_centre_textbox = QtWidgets.QTextEdit()
        custom_camera_centre_textbox.setVisible(False)
        system_grp_box_layout.addWidget(custom_camera_centre_textbox, 2, 1)

        if self.system.camera_centre_body_index in range(len(self.system.bodies)):
            camera_centre_dropdown.setCurrentIndex(self.system.camera_centre_body_index)
        else:
            custom_camera_centre_textbox.setVisible(True)

        # system apply button
        system_apply_button = QtWidgets.QPushButton(text="Apply")
        system_apply_button.setObjectName("applyButton")
        system_grp_box_layout.addWidget(system_apply_button, 3, 1, alignment=Qt.AlignmentFlag.AlignRight)
        
        return system_grp_box

    def build_bodies_grp_box(self) -> QtWidgets.QGroupBox:
        bodies_grp_box = QtWidgets.QGroupBox("Body Properties")
        bodies_grp_box.setObjectName("parentGroupBox")
        bodies_grp_box_layout = QtWidgets.QVBoxLayout()
        bodies_grp_box.setLayout(bodies_grp_box_layout)

        return bodies_grp_box

    def build_bodies_scroll_area(self, widget:QtWidgets.QWidget) -> QtWidgets.QScrollArea:
        bodies_scroll_area = QtWidgets.QScrollArea()
        bodies_scroll_area.setWidget(widget)
        bodies_scroll_area.setWidgetResizable(True)
        return bodies_scroll_area

    def build_body_grp_box(self, body:Body) -> QtWidgets.QGroupBox:

        # body group box
        body_grp_box = QtWidgets.QGroupBox(body.name)
        body_grp_box.setObjectName("daughterGroupBox")
        body_grp_box_layout = QtWidgets.QGridLayout()
        body_grp_box.setLayout(body_grp_box_layout)

        # body mass
        body_mass_value_textbox = QtWidgets.QTextEdit(str(body.mass))
        body_grp_box_layout.addWidget(QtWidgets.QLabel("m: "), 0, 0)
        body_grp_box_layout.addWidget(body_mass_value_textbox, 0, 1)

        # plot colour
        body_colour_button = QtWidgets.QPushButton(text=body.scatter.colour)
        body_grp_box_layout.addWidget(QtWidgets.QLabel("Colour:"), 1, 0)
        body_grp_box_layout.addWidget(body_colour_button, 1, 1)

        # body apply button
        body_apply_button = QtWidgets.QPushButton(text="Apply")
        body_apply_button.setObjectName("applyButton")
        body_grp_box_layout.addWidget(body_apply_button, 2, 1, alignment=Qt.AlignmentFlag.AlignRight)

        return body_grp_box


    def __init__(self, system:System, parent=None):
        self.system = system
        super().__init__(parent)
        #self.setMaximumWidth(450)
        
        self.setObjectName("controlPanel")
        self.setStyleSheet(utils.load_css("app/graphics/stylesheets/control_panel/global.css"))

        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        # system group box
        system_grp_box = self.build_system_grp_box()
        layout.addWidget(system_grp_box)

        # bodies group box
        bodies_grp_box = self.build_bodies_grp_box()

        # init body mass widgets
        for i in range(len(system.bodies)):
            
            # body group box
            body_grp_box = self.build_body_grp_box(system.bodies[i])

            # add body groupbox to parent 
            bodies_grp_box.layout().addWidget(body_grp_box)

        bodies_scroll_area = self.build_bodies_scroll_area(bodies_grp_box)
        layout.addWidget(bodies_scroll_area)
        