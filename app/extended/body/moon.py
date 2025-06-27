from ...base.body import Body
from ...base.trail import Trail
from ...graphics.scatter import Scatter


class Moon(Body):
    
    def __init__(self, init_pos:list, init_vel:list, name="Moon", plot_size=10, face_colour="white") -> None:
        super().__init__(name, 7.348e22, init_pos, init_vel, 
        scatter=Scatter(size=plot_size, face_colour=face_colour),
        trail=Trail((1, 1, 1, 1)))

# sphere
#class Moon(Body):
#    
#    def __init__(self, init_pos:list, init_vel:list, name="Moon", colour="white") -> None:
#        super().__init__(name, 7.348e22, init_pos, init_vel, 
#        scatter=Scatter(radius=1738100, colour=colour),
#        trail=Trail("white"))

    