from PyQt5 import QtWidgets
from ..utils import utils

class ColourButton(QtWidgets.QPushButton):

    def __init__(self, init_colour:list) -> None:
        super().__init__()
        self.colour = init_colour
        self.set_colour(init_colour)

    def set_colour(self, colour:list):
        self.setStyleSheet(f"""QPushButton {{
            background-color: rgba({colour[0]}, {colour[1]}, {colour[2]}, {colour[3]});
        }}""")
        self.colour = colour
        