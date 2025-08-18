from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from ....base.body import Body
from ..colour_button import ColourButton
import numpy as np


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
        self.plot_colour_button = ColourButton(255 * self.body.plot.colour)
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
        self.pos_labels = [QtWidgets.QLabel("x"), QtWidgets.QLabel("y"),  QtWidgets.QLabel("z")]
        self.pos_textboxes = [QtWidgets.QLineEdit(f"{self.body.pos[i]:.4e}") for i in range(3)]

        for i in range(3):
            self.pos_textboxes[i].setObjectName("smallLineEdit")
            self.layout().addWidget(self.pos_labels[i], 5 + i, 0)
            self.layout().addWidget(self.pos_textboxes[i], 5 + i, 1)

        # velocity
        self.vel_labels = [QtWidgets.QLabel("vx"), QtWidgets.QLabel("vy"),  QtWidgets.QLabel("vz")]
        self.vel_textboxes = [QtWidgets.QLineEdit(f"{self.body.vel[i]:.4e}") for i in range(3)]

        for i in range(3):
            self.vel_textboxes[i].setObjectName("smallLineEdit")
            self.layout().addWidget(self.vel_labels[i], 5 + i, 2)
            self.layout().addWidget(self.vel_textboxes[i], 5 + i, 3)

        self.apply_button = QtWidgets.QPushButton(text="Apply")
        self.apply_button.clicked.connect(self.apply)
        self.layout().addWidget(self.apply_button, 8, 3, 1, 1, alignment=Qt.AlignmentFlag.AlignRight)

    def get_new_colour(self) -> np.ndarray:
        colour = QtWidgets.QColorDialog().getColor()
        rgba_colour = np.array([colour.red(), colour.green(), colour.blue(), colour.alpha()]) 
        return rgba_colour

    def change_plot_colour(self) -> None:
        colour = self.get_new_colour()
        self.plot_colour_button.set_colour(colour)

    def change_trail_colour(self) -> None:
        colour = self.get_new_colour()
        self.trail_colour_button.set_colour(colour)

    def apply(self) -> None:
        # m
        self.body.mass = float(self.m_textbox.text())

        # plot colour
        self.body.plot.colour = self.plot_colour_button.colour / 255

        # trail colour
        self.body.trail.colour = self.trail_colour_button.colour / 255

        # trail width
        self.body.trail.width = float(self.trail_width_textbox.text())
        
        # position
        r = [float(self.pos_textboxes[i].text()) for i in range(3)]
        self.body.pos = np.array(r)

        # velocity
        v = [float(self.vel_textboxes[i].text()) for i in range(3)]
        self.body.vel = np.array(v)

    def update_r_v_texts(self) -> None:
        for i in range(3):
            self.pos_textboxes[i].setText(f"{self.body.pos[i]:.4e}")
            self.vel_textboxes[i].setText(f"{self.body.vel[i]:.4e}")
    
 