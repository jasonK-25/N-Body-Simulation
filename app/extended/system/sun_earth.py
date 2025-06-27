from ...base.system import System
from ..body import Earth, Sun

        
class SunEarthCircularApprox(System):

    TIMESTEP = 60 * 60 * 24
    G = 6.6743e-11
    CAMERA_DISTANCE = 2e11

    def __init__(self) -> None:
        bodies = [
            Sun([0, 0, 0], [0, 0, 0]),
            Earth([1.496e11, 0, 0], [0, 29780, 0])
        ]
        super().__init__("Sun Earth", bodies, self.TIMESTEP, self.CAMERA_DISTANCE, self.G)


class SunEarthRealistic(System):
    # 2025 Jan 04

    TIMESTEP = 60 * 60 * 24
    G = 6.6743e-11
    CAMERA_DISTANCE = 2e11

    def __init__(self) -> None:
        bodies = [
            Sun([0, 0, 0], [0, 0, 0]),
            Earth([-3.441e10, 1.4302e11, -7.7097e6], [-2.9453e4, -7.0904e3, -4.5975e-1]) 
        ]
        super().__init__("Sun Earth", bodies, self.TIMESTEP, self.CAMERA_DISTANCE, self.G)
