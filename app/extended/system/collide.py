from ...base.system import System
from ...base.body import Body
from ...graphics.base.scatter import Scatter
from ...graphics.base.trail import Trail
from ...graphics.utils import scalar


class Collide(System):
    G = 6.67e-11

    def __init__(self):
        bodies = [
            Body("body 1", 100, 100, [200, 0, 0], [0, 0, 0], Scatter(20, [1, 0.7, 1, 1]), Trail([1, 1, 1, 1])),
            Body("body 0", 100, 100, [0, 0, 0], [0, 0, 0], Scatter(20, [1, 1, 1, 1]), Trail([1, 1, 1, 1])),
            Body("body 4", 100, 100, [1100, 0, 0], [0, 0, 0], Scatter(20, [1, 0.7, 1, 1]), Trail([1, 1, 1, 1])),
            Body("body 2", 100, 100, [400, 0, 0], [0, 0, 0], Scatter(20, [1, 0.7, 1, 1]), Trail([1, 1, 1, 1])),
            Body("body 3", 100, 100, [600, 0, 0], [0, 0, 0], Scatter(20, [1, 1, 1, 1]), Trail([1, 1, 1, 1])),
            Body("body 5", 100, 100, [1300, 0, 0], [0, 0, 0], Scatter(20, [1, 0.7, 1, 1]), Trail([1, 1, 1, 1]))
        ]
        super().__init__("2 body collision", bodies, 10, scalar.M, self.G, [0, 0, 0])