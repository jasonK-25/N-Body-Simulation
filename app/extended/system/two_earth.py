from ...base.system import System
from ..body import Earth


class TwoEarth(System):

    TIMESTEP = 1
    G = 6.6743e-11

    def __init__(self) -> None:
        bodies = [
            Earth([-4.2227e7 / 2, 0, 0], [0, -3070 / 2, 0]),
            Earth([4.2227e7 / 2, 0, 0], [0, 3070 / 2, 0]),
        ]
        super().__init__("Two Earth", bodies, self.TIMESTEP, None, self.G)
