from ...base.system import System
from ..body import Sun, Earth, Moon
from ...graphics.utils import scalar


class SunEarthMoon(System):
    # 2025 Jan 04

    TIMESTEP = 60 * 60 * 24
    G = 6.6743e-11

    def __init__(self) -> None:
        bodies = [
            Sun([0, 0, 0], [0, 0, 0]),
            Earth([-3.441e10, 1.4302e11, -7.7097e6], [-2.9453e4, -7.0904e3, -4.5975e-1]),
            Moon([-3.4073e10, 1.4286e11, -2.1878e7], [-2.902e4, -6.1362e3, 8.3538e-2])
        ]
        super().__init__(name="Sun Earth Moon", bodies=bodies, timestep=self.TIMESTEP, plot_scale=scalar.AU, G=self.G, focus=bodies[1])
