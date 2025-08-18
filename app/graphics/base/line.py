from vispy.scene.visuals import Line as _Line
import numpy as np


class Line(_Line):

    def __init__(self, colour:list, width=2) -> None:
        self.data = []
        self.colour = np.array(colour)
        self._width = width
        super().__init__(color=self.colour, width=self.width)

    @property
    def visible(self) -> bool:
        return self.colour[3] > 0