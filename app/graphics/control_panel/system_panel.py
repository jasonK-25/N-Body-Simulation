from ...base.system import System
from ...base.system import Body
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
import numpy as np
from .. import scalars
from ... import utils
from typing import List

class SystemPanel(QtWidgets.QWidget):

    def __init__(self, system:System, timer, parent=None) -> None:
        self.system = system
        self.timer = timer
        self.is_paused = False
        super().__init__()

        self.setObjectName("parentPanel")
        self.setLayout(QtWidgets.QGridLayout())
        
        # pause/resume (state) button
        self.state_button = QtWidgets.QPushButton(text="Pause")
        self.state_button.clicked.connect(self.toggle_state)
        self.layout().addWidget(self.state_button, 0, 0)
        
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
            lambda: self.widgets_visibility_toggle(self.custom_focus_labels + self.custom_focus_textboxes, 
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
            lambda: self.widgets_visibility_toggle([self.custom_plot_scale_textbox], 
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

    def toggle_state(self):
        if self.is_paused:
            self.state_button.setText("Pause")
            self.timer.start(1/60)
            self.is_paused
        else:
            self.timer.stop()
            self.state_button.setText("Resume")
        self.is_paused = not self.is_paused

    def widgets_visibility_toggle(self, widgets:List[QtWidgets], is_visiible:bool) -> None:
        for i in range(len(widgets)):
            widgets[i].setVisible(is_visiible)

    def apply(self) -> None:
        print("Applying new system parameters")
        
        # G
        self.system.G = float(self.G_textbox.text())

        # camera centre
        focus_text = self.focus_dropdown.currentText()
        if focus_text == "Custom":
            focus_pos = float(self.custom_focus_textboxes[i].text() for i in range(3))
            self.system.camera_centre = np.array(focus_pos)
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
