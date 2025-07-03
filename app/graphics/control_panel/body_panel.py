from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from ...base.body import Body
import numpy as np
from ..colour_button import ColourButton


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
        self.plot_colour_button = ColourButton(255 * self.body.scatter.colour)
        self.plot_colour_button.clicked.connect(self.change_plot_colour)
        self.layout().addWidget(self.plot_colour_button, 2, 2, 1, 2)

        # trail colour
        self.layout().addWidget(QtWidgets.QLabel("Trail Colour:"), 3, 0, 1, 2)
        self.trail_colour_button = ColourButton(255 * self.body.trail.colour)
        self.trail_colour_button.clicked.connect(self.change_trail_colour)
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

    def get_new_colour(self) -> np.ndarray:
        colour = QtWidgets.QColorDialog().getColor()
        rgba_colour = np.array([colour.red(), colour.green(), colour.blue(), colour.alpha()]) 
        return rgba_colour

    def change_plot_colour(self) -> None:
        colour = self.get_new_colour()
        #self.body.scatter.colour = colour / 255
        self.plot_colour_button.set_colour(colour)

    def change_trail_colour(self) -> None:
        colour = self.get_new_colour()
        #self.body.trail.colour = colour / 255
        self.trail_colour_button.set_colour(colour)

    def apply(self) -> None:
        # m
        self.body.mass = float(self.m_textbox.text())

        # plot colour
        self.body.scatter.colour = self.plot_colour_button.colour / 255

        # trail colour
        self.body.trail.colour = self.trail_colour_button.colour / 255

        # trail width
        self.body.trail.width = float(self.trail_width_textbox.text())
        
        # position
        r = [float(self.r_textboxes[i].text()) for i in range(3)]
        self.body.r = np.array(r)

        # velocity
        v = [float(self.v_textboxes[i].text()) for i in range(3)]
        self.body.v = np.array(v)
