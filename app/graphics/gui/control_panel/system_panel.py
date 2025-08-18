from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from ....base.system import System
from ....base.body import Body
from vispy.app import Timer
from ...utils import scalar, utils
from typing import List

class SystemPanel(QtWidgets.QWidget):

    def __init__(self, system:System, timer:Timer) -> None:
        self.system = system
        self.timer = timer
        self.is_paused = False
        super().__init__()

        self.setObjectName("parentPanel")
        self.setLayout(QtWidgets.QGridLayout())

        # pause/resume (state) button
        self.state_button = QtWidgets.QPushButton("Pause")
        self.state_button.clicked.connect(self.toggle_state)
        self.layout().addWidget(self.state_button, 0, 0)

        # G
        self.layout().addWidget(QtWidgets.QLabel("G:"), 1, 0)
        self.G_textbox = QtWidgets.QLineEdit(str(self.system.G))
        self.layout().addWidget(self.G_textbox, 1, 1)

        # camera centre
        self.layout().addWidget(QtWidgets.QLabel("Focus"), 2, 0)
        self.focus_dropdown = QtWidgets.QComboBox()
        self.focus_dropdown.addItems([body.name for body in self.system.bodies] + ["Custom"])
        self.layout().addWidget(self.focus_dropdown, 2, 1)

        # custom focus
        self.custom_focus_labels = [QtWidgets.QLabel("Focus x:"), QtWidgets.QLabel("Focus y:"), QtWidgets.QLabel("Focus z:")]#
        self.custom_focus_textboxes = [QtWidgets.QLineEdit() for _ in range(3)]

        for i in range(3):
            custom_focus_label = self.custom_focus_labels[i]
            custom_focus_label.setVisible(False)
            
            custom_focus_textbox = self.custom_focus_textboxes[i]
            custom_focus_textbox.setVisible(False)

            self.layout().addWidget(custom_focus_label, 3 + i, 0)
            self.layout().addWidget(custom_focus_textbox, 3 + i, 1)   
        
        # hide custom focus fields if custom is not selected
        self.focus_dropdown.currentTextChanged.connect(
            lambda: self.widgets_visibility_toggle(self.custom_focus_labels + self.custom_focus_textboxes, 
                self.focus_dropdown.currentText() == "Custom"
            )
        )

        # set text on custom focus textboxes if needed
        if isinstance(self.system.focus, Body):
            self.focus_dropdown.setCurrentText(self.system.focus.name)
        else:
            self.focus_dropdown.setCurrentText("Custom")

            for i in range(3):
                self.custom_focus_labels[i].setVisible(True)

                custom_focus_textbox = self.custom_focus_textboxes[i]
                custom_focus_textbox.setText(str(self.system.focus[i]))
                custom_focus_textbox.setVisible(True)
        
        # plot scale
        self.layout().addWidget(QtWidgets.QLabel("Scale:"), 6, 0)
        self.plot_scale_dropdown = QtWidgets.QComboBox()
        self.plot_scale_dropdown.addItems(list(scalar.DISTANCE.keys()) + ["Custom"])
        self.layout().addWidget(self.plot_scale_dropdown, 6, 1)

        # custom plot scale textbox
        self.custom_plot_scale_textbox = QtWidgets.QLineEdit()
        self.custom_plot_scale_textbox.setVisible(False)
        self.layout().addWidget(self.custom_plot_scale_textbox, 7, 0)

        # set text on custom plot scale textbox if needed
        if self.system.plot_scale in list(scalar.DISTANCE.values()):
            self.plot_scale_dropdown.setCurrentText(utils.get_key_from_value(scalar.DISTANCE, self.system.plot_scale))
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

        # apply button
        self.apply_button = QtWidgets.QPushButton(text="Apply")
        self.layout().addWidget(self.apply_button, 9, 1, alignment=Qt.AlignmentFlag.AlignRight) 
        self.apply_button.clicked.connect(self.apply)

    def toggle_state(self):
        if self.is_paused:
            self.state_button.setText("Pause")
            self.timer.start(1/60)
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
            focus_pos = [float(self.custom_focus_textboxes[i].text()) for i in range(3)]
            self.system.focus = np.array(focus_pos)
        else:
            focus = self.system.bodies[self.focus_dropdown.currentIndex()]
            self.system.focus = focus

        # plot scale
        plot_scale_text = self.plot_scale_dropdown.currentText()
        if plot_scale_text == "Custom":
            self.system.plot_scale = float(self.custom_plot_scale_textbox.text())
        else:
            self.system.plot_scale = list(scalar.DISTANCE.values())[self.plot_scale_dropdown.currentIndex()]

        # trails
        trails_checked = self.trails_checkbox.isChecked()
        self.system.set_trails_visible(trails_checked)
       
        