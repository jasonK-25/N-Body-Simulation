from ...base.system import System
from ..body import Earth, Moon

        
class EarthMoonCircularApprox(System):

    TIMESTEP = 60 * 60 
    G = 6.6743e-11

    def __init__(self) -> None:
        bodies = [
            Earth([0, 0, 0], [0, 0, 0]),
            Moon([3.844e8, 0, 0], [0, 1022, 0])
        ]
        super().__init__("Earth Moon", bodies, self.TIMESTEP, self.G)
