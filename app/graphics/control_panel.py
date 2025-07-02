from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QSize
from ..base.system import System
from ..base.body import Body
from ..import utils
import numpy as np
from . import scalars
from typing import List

class SystemPanel(QtWidgets.QWidget):

    def __init__(self, system:System, timer, parent=None) -> None:
        self.system = system
        self.initial_system = None
        self.timer = timer
        self.is_paused = False
        super().__init__()

        self.setObjectName("parentPanel")
        self.setLayout(QtWidgets.QGridLayout())
        
        # pause/resume (state) button
        self.state_button = QtWidgets.QPushButton(text="Pause")
        self.state_button.clicked.connect(self.toggle_state)
        self.layout().addWidget(self.state_button, 0, 0)
        
        # reset button
        self.reset_button = QtWidgets.QPushButton(text="Reset")
        self.reset_button.clicked.connect(self.reset_system)
        self.layout().addWidget(self.reset_button, 0, 1)
        
        # G
        self.layout().addWidget(QtWidgets.QLabel("G:"), 1, 0)
        self.G_textbox = QtWidgets.QLineEdit(str(self.system.G))
        self.layout().addWidget(self.G_textbox, 1, 1)

        # camera centre
        self.layout().addWidget(QtWidgets.QLabel("Focus:"), 2, 0)
        self.focus_dropdown = QtWidgets.QComboBox()
        self.focus_dropdown.addItems([body.name for body in self.system.bodies] + ["Custom"])
        
        self.layout().addWidget(self.focus_dropdown, 2, 1)

        # custom focus
        self.custom_focus_labels = [QtWidgets.QLabel("Focus x:"), QtWidgets.QLabel("Focus y:"), QtWidgets.QLabel("Focus z:")]#
        self.custom_focus_textboxes = [QtWidgets.QLineEdit() for _ in range(3)]

        for i in range(3):
            custom_focus_labels = self.custom_focus_labels[i]
            custom_focus_labels.setVisible(False)
            
            custom_focus_textbox = self.custom_focus_textboxes[i]
            custom_focus_textbox.setVisible(False)

            self.layout().addWidget(custom_focus_labels, 3 + i, 0)
            self.layout().addWidget(custom_focus_textbox, 3 + i, 1)   

        self.focus_dropdown.currentTextChanged.connect(
            lambda: self.widgets_visibility_trigger(self.custom_focus_labels + self.custom_focus_textboxes, 
                self.focus_dropdown.currentText() == "Custom"
            )
        )

        # set text on custom focus textboxes if needed
        if isinstance(self.system.camera_centre, Body):
            self.focus_dropdown.setCurrentText(self.system.camera_centre.name)
        else:
            self.focus_dropdown.setCurrentText("Custom")

            for i in range(3):
                self.custom_focus_labels[i].setVisible(True)

                custom_focus_textbox = self.custom_focus_textboxes[i]
                custom_focus_textbox.setText(str(self.system.camera_centre[i]))
                custom_focus_textbox.setVisible(True)

        # plot scale
        self.layout().addWidget(QtWidgets.QLabel("Scale:"), 6, 0)
        self.plot_scale_dropdown = QtWidgets.QComboBox()
        self.plot_scale_dropdown.addItems(list(scalars.DISTANCE.keys()) + ["Custom"])
        self.layout().addWidget(self.plot_scale_dropdown, 6, 1)

        # custom plot scale textbox
        self.custom_plot_scale_textbox = QtWidgets.QLineEdit()
        self.custom_plot_scale_textbox.setVisible(False)
        self.layout().addWidget(self.custom_plot_scale_textbox, 7, 0)

        # set text on custom plot scale textbox if needed
        if self.system.plot_scale in list(scalars.DISTANCE.values()):
            self.plot_scale_dropdown.setCurrentText(utils.get_key_from_value(scalars.DISTANCE, self.system.plot_scale))
        else:
            self.custom_plot_scale_textbox.setText(str(self.system.plot_scale))
            self.custom_plot_scale_textbox.setVisible(True)

        self.plot_scale_dropdown.currentTextChanged.connect(
            lambda: self.widgets_visibility_trigger([self.custom_plot_scale_textbox], 
            self.plot_scale_dropdown.currentText() == "Custom"
            )
        )
        
        # trail
        self.trails_checkbox = QtWidgets.QCheckBox("Trails")
        self.trails_checkbox.setChecked(self.system.trails_visible)
        self.layout().addWidget(self.trails_checkbox, 8, 0)

        # velocity direction
        self.vel_checkbox = QtWidgets.QCheckBox("Velocity field")
        self.layout().addWidget(self.vel_checkbox, 8, 1)

        # apply button
        self.apply_button = QtWidgets.QPushButton(text="Apply")
        self.layout().addWidget(self.apply_button, 9, 1, alignment=Qt.AlignmentFlag.AlignRight) 
        self.apply_button.clicked.connect(self.apply)
    
    def reset_system(self):
        print(self.system == self.initial_system)
        self.system = self.initial_system
        
    def toggle_state(self):
        if self.is_paused:
            self.state_button.setText("Pause")
            self.timer.start(1/60)
            self.is_paused
        else:
            self.timer.stop()
            self.state_button.setText("Resume")
        self.is_paused = not self.is_paused

    def widgets_visibility_trigger(self, widgets:List[QtWidgets], is_visiible:bool) -> None:
        for i in range(len(widgets)):
            widgets[i].setVisible(is_visiible)

    def apply(self) -> None:
        print("System apply button clicked")
        
        # G
        self.system.G = float(self.G_textbox.text())

        # camera centre
        focus_text = self.focus_dropdown.currentText()
        if focus_text == "Custom":

            focus_x = float(self.custom_focus_textboxes[0].text())
            focus_y = float(self.custom_focus_textboxes[1].text())
            focus_z = float(self.custom_focus_textboxes[2].text())
            
            self.system.camera_centre = np.array([focus_x, focus_y, focus_z])
        else:
            focus = self.system.bodies[self.focus_dropdown.currentIndex()]
            self.system.camera_centre = focus

        # plot scale
        plot_scale_text = self.plot_scale_dropdown.currentText()
        if plot_scale_text == "Custom":
            self.system.plot_scale = float(self.custom_plot_scale_textbox.text())
        else:
            self.system.plot_scale = list(scalars.DISTANCE.values())[self.plot_scale_dropdown.currentIndex()]

        # trails
        trails_checked = self.trails_checkbox.isChecked()
        self.system.set_trails_visible(trails_checked)
       
        # vel direction
        vel_direction_checked = self.vel_checkbox.isChecked()
        if vel_direction_checked:
            pass
        else:
            pass

        
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

        # plot colour
        self.layout().addWidget(QtWidgets.QLabel("Plot Colour:"), 2, 0, 1, 2)
        self.plot_colour_button = QtWidgets.QPushButton(text=str(self.body.scatter.colour))
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
        self.r_labels = [QtWidgets.QLabel("x"), QtWidgets.QLabel("y"),  QtWidgets.QLabel("z")]
        self.r_textboxes = [QtWidgets.QLineEdit(f"{self.body.r[0]:.4e}"), QtWidgets.QLineEdit(f"{self.body.r[1]:.4e}"), QtWidgets.QLineEdit(f"{self.body.r[2]:.4e}")]
        
        for i in range(3):
            self.r_textboxes[i].setObjectName("smallLineEdit")
            self.layout().addWidget(self.r_labels[i], 5 + i, 0)
            self.layout().addWidget(self.r_textboxes[i], 5 + i, 1)

        # velocity
        self.v_labels = [QtWidgets.QLabel("vx"), QtWidgets.QLabel("vy"),  QtWidgets.QLabel("vz")]
        self.v_textboxes = [QtWidgets.QLineEdit(f"{self.body.v[0]:.4e}"), QtWidgets.QLineEdit(f"{self.body.v[1]:.4e}"), QtWidgets.QLineEdit(f"{self.body.v[2]:.4e}")]

        for i in range(3):
            self.v_textboxes[i].setObjectName("smallLineEdit")
            self.layout().addWidget(self.v_labels[i], 5 + i, 2)
            self.layout().addWidget(self.v_textboxes[i], 5 + i, 3)

        # apply button
        self.apply_button = QtWidgets.QPushButton(text="Apply")
        self.apply_button.clicked.connect(self.apply)
        self.layout().addWidget(self.apply_button, 8, 3, 1, 1, alignment=Qt.AlignmentFlag.AlignRight)

    def apply(self) -> None:
        # m
        self.body.mass = float(self.m_textbox.text())

        # plot colour
        plot_colour = self.plot_colour_button.text().replace(",", "").replace("[", "").replace("]", "").split(" ")
        self.body.scatter.colour = [float(item) for item in plot_colour]

        # trail colour
        trail_colour = self.trail_colour_button.text().replace(",", "").replace("[", "").replace("]", "").split(" ")
        self.body.trail.colour = [float(item) for item in plot_colour]

        # trail width
        self.body.trail.width = float(self.trail_width_textbox.text())
        
        # position
        x = float(self.r_textboxes[0].text())
        y = float(self.r_textboxes[1].text())
        z = float(self.r_textboxes[2].text())
        self.body.r = np.array([x, y, z])

        # velocity
        vx = float(self.v_textboxes[0].text())
        vy = float(self.v_textboxes[1].text())
        vz = float(self.v_textboxes[2].text())
        self.body.v = np.array([vx, vy, vz])


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

   