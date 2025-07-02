from ...base.system import System
from ..body import Earth, Sun
from ...graphics import scalars

        
class SunEarthCircularApprox(System):

    TIMESTEP = 60 * 60 * 24
    G = 6.6743e-11

    def __init__(self) -> None:
        bodies = [
            Sun([0, 0, 0], [0, 0, 0]),
            Earth([1.496e11, 0, 0], [0, 29780, 0])
        ]
        super().__init__("Sun Earth", bodies, self.TIMESTEP, 0, scalars.AU, self.G)


class SunEarthRealistic(System):
    # 2025 Jan 04

    TIMESTEP = 60 * 60 * 24
    G = 6.6743e-11

    def __init__(self) -> None:
        bodies = [
            Sun([0, 0, 0], [0, 0, 0]),
            Earth([-3.441e10, 1.4302e11, -7.7097e6], [-2.9453e4, -7.0904e3, -4.5975e-1]) 
        ]
        super().__init__(name="Sun Earth", bodies=bodies, timestep=self.TIMESTEP, camera_centre=bodies[0], plot_scale=scalars.AU,G= self.G)
