from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QSize
from ..base.system import System
from ..base.body import Body
from ..import utils
import numpy as np
from . import scalars


class SystemPanel(QtWidgets.QWidget):

    def __init__(self, system:System, parent=None) -> None:
        self.system = system
        super().__init__()

        self.setObjectName("parentPanel")
        self.setLayout(QtWidgets.QGridLayout())
        
        
        # G
        self.layout().addWidget(QtWidgets.QLabel("G:"), 0, 0)
        self.G_textbox = QtWidgets.QLineEdit(str(self.system.G))
        self.layout().addWidget(self.G_textbox, 0, 1)

        # camera centre
        self.layout().addWidget(QtWidgets.QLabel("Focus:"), 1, 0)
        self.focus_dropdown = QtWidgets.QComboBox()
        self.focus_dropdown.addItems([body.name for body in self.system.bodies] + ["Custom"])
        self.layout().addWidget(self.focus_dropdown, 1, 1)

        # custom focus textbox
        self.custom_focus_textbox = QtWidgets.QLineEdit()
        self.custom_focus_textbox.setVisible(False)
        self.layout().addWidget(self.custom_focus_textbox, 2, 0)

        if self.system.camera_centre_body_index in range(len(self.system.bodies)):
            self.focus_dropdown.setCurrentIndex(self.system.camera_centre_body_index)
        else:
            self.focus_dropdown.setCurrentText("Custom")
            self.custom_focus_textbox.setText(str(self.system.camera_centre_pos_fixed))
            self.custom_focus_textbox.setVisible(True)

        # plot scale
        self.layout().addWidget(QtWidgets.QLabel("Scale:"), 3, 0)
        self.plot_scale_dropdown = QtWidgets.QComboBox()
        self.plot_scale_dropdown.addItems(["m", "km", "AU", "Custom"])
        self.layout().addWidget(self.plot_scale_dropdown, 3, 1)

        # custom plot scale textbox
        self.custom_plot_scale_textbox = QtWidgets.QLineEdit()
        self.custom_plot_scale_textbox.setVisible(False)
        self.layout().addWidget(self.custom_plot_scale_textbox, 4, 0)

        if self.system.plot_scale in list(scalars.DISTANCE.keys()):
            self.plot_scale_dropdown.setCurrentText(scalars.DISTANCE[self.system.plot_scale])
        else:
            self.custom_plot_scale_textbox.setText(str(self.system.plot_scale))
            self.custom_plot_scale_textbox.setVisible(True)
        
        # trail
        self.trails_checkbox = QtWidgets.QCheckBox("Trails")
        self.layout().addWidget(self.trails_checkbox, 5, 0)

        # velocity direction
        self.vel_checkbox = QtWidgets.QCheckBox("Velocity field")
        self.layout().addWidget(self.vel_checkbox, 5, 1)

        # apply button
        self.apply_button = QtWidgets.QPushButton(text="Apply")
        self.layout().addWidget(self.apply_button, 6, 1, alignment=Qt.AlignmentFlag.AlignRight)      

        
class BodyPanel(QtWidgets.QGroupBox):

    def __init__(self, body:Body) -> None:
        self.body = body
        super().__init__()
        self.setObjectName("bodyPanel")
        self.setLayout(QtWidgets.QGridLayout())

        # body name label
        self.layout().addWidget(QtWidgets.QLabel(body.name), 0, 0, 1, 4, alignment=Qt.AlignmentFlag.AlignCenter)

        # m
        self.layout().addWidget(QtWidgets.QLabel("m:"), 1, 0, 1, 2)
        self.m_textbox = QtWidgets.QLineEdit(str(self.body.mass))
        self.layout().addWidget(self.m_textbox, 1, 2, 1, 2)

        # colour
        self.layout().addWidget(QtWidgets.QLabel("Plot Colour:"), 2, 0, 1, 2)
        self.plot_colour_button = QtWidgets.QPushButton(text=self.body.scatter.colour)
        self.layout().addWidget(self.plot_colour_button, 2, 2, 1, 2)

        # trail colour
        self.layout().addWidget(QtWidgets.QLabel("Trail Colour:"), 3, 0, 1, 2)
        self.trail_colour_button = QtWidgets.QPushButton(text=str(self.body.trail.colour))
        self.layout().addWidget(self.trail_colour_button, 3, 2, 1, 2)

        # trail width
        self.layout().addWidget(QtWidgets.QLabel("Trail Width:"), 4, 0, 1, 2)
        self.trail_width_textbox = QtWidgets.QLineEdit(str(self.body.trail.width))
        self.layout().addWidget(self.trail_width_textbox, 4, 2, 1, 2)

        # position
        self.x_textbox = QtWidgets.QLineEdit(f"{self.body.r[0]:.4e}")
        self.y_textbox = QtWidgets.QLineEdit(f"{self.body.r[1]:.4e}")
        self.z_textbox = QtWidgets.QLineEdit(f"{self.body.r[2]:.4e}")
        
        self.x_textbox.setObjectName("smallLineEdit")
        self.y_textbox.setObjectName("smallLineEdit")
        self.z_textbox.setObjectName("smallLineEdit")
        
        self.layout().addWidget(QtWidgets.QLabel("x"), 5, 0)
        self.layout().addWidget(QtWidgets.QLabel("y"), 6, 0)
        self.layout().addWidget(QtWidgets.QLabel("z"), 7, 0)
        self.layout().addWidget(self.x_textbox, 5, 1)
        self.layout().addWidget(self.y_textbox, 6, 1)
        self.layout().addWidget(self.z_textbox, 7, 1)

        # velocity
        self.vx_textbox = QtWidgets.QLineEdit(f"{self.body.v[0]:.4e}")
        self.vy_textbox = QtWidgets.QLineEdit(f"{self.body.v[1]:.4e}")
        self.vz_textbox = QtWidgets.QLineEdit(f"{self.body.v[2]:.4e}")

        self.vx_textbox.setObjectName("smallLineEdit")
        self.vy_textbox.setObjectName("smallLineEdit")
        self.vz_textbox.setObjectName("smallLineEdit")

        #self.x_textbox.setMaximumWidth(50)

        self.layout().addWidget(QtWidgets.QLabel("vx"), 5, 2)
        self.layout().addWidget(QtWidgets.QLabel("vy"), 6, 2)
        self.layout().addWidget(QtWidgets.QLabel("vz"), 7, 2)
        self.layout().addWidget(self.vx_textbox, 5, 3)
        self.layout().addWidget(self.vy_textbox, 6, 3)
        self.layout().addWidget(self.vz_textbox, 7, 3)

        # apply button
        self.apply_button = QtWidgets.QPushButton(text="Apply")
        self.layout().addWidget(self.apply_button, 8, 3, 1, 1, alignment=Qt.AlignmentFlag.AlignRight)

        
class BodiesPanel(QtWidgets.QWidget):

    def __init__(self, system:System) -> None:
        self.system = system
        super().__init__()
        self.setObjectName("parentPanel")
        self.setLayout(QtWidgets.QVBoxLayout())

        for i in range(len(self.system.bodies)):
            body_panel = BodyPanel(self.system.bodies[i])
            self.layout().addWidget(body_panel)
    

class ControlPanel(QtWidgets.QWidget):

    def __init__(self, system:System, parent=None):

        self.system = system
        super().__init__(parent)
        
        self.setObjectName("controlPanel")
        self.setStyleSheet(utils.load_css("app/graphics/stylesheets/control_panel.css"))
        
        self.setLayout(QtWidgets.QVBoxLayout())

        # system panel label
        system_panel_label = QtWidgets.QLabel("System Properties")
        self.layout().addWidget(system_panel_label)

        # system panel
        system_panel = SystemPanel(self.system)
        self.layout().addWidget(system_panel)

        # bodies label
        bodies_panel_label = QtWidgets.QLabel("Body Properties")
        self.layout().addWidget(bodies_panel_label)
        
        # bodies panel
        bodies_panel = BodiesPanel(self.system)
        
        # bodies scroll area
        bodies_scroll_area = self.build_bodies_scroll_area(bodies_panel)
        self.layout().addWidget(bodies_scroll_area)

    def build_bodies_scroll_area(self, widget:QtWidgets.QWidget) -> QtWidgets.QScrollArea:
        bodies_scroll_area = QtWidgets.QScrollArea()
        bodies_scroll_area.setWidget(widget)
        bodies_scroll_area.setWidgetResizable(True)
        return bodies_scroll_area

   