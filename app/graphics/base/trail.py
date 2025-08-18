from .line import Line
import numpy as np


class Trail(Line):

    def __init__(self, colour:list, length=30, width=2) -> None:
        self.length = length
        self.__width = width

        super().__init__(colour=colour, width=width)

    @property
    def width(self) -> int:
        return self.__width
    
    @width.setter
    def width(self, width:int) -> None:
        self.__width = width 
    
    @property
    def visible(self) -> bool:
        return self.colour[-1] == 1
        
    def set_visible(self, is_visible:bool) -> None:
        if is_visible:
            self.colour[-1] = 1
        else:
            self.colour[-1] = 0

    def append(self, pos:np.ndarray) -> None:

        # limit trail length
        if self.length > 0 and len(self.data) >= self.length:
            self.data.pop(0)
        
        self.data.append(pos)