from vispy.scene.visuals import Markers
import numpy as np


class Scatter(Markers):
    
    def __init__(self, size:int, colour:list) -> None:
        self.size = size
        self.colour = np.array(colour)
        
        super().__init__()