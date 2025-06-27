from ...base.body import Body
from ...base.trail import Trail
from ...graphics.scatter import Scatter


class Sun(Body):
    
    def __init__(self, init_pos:list, init_vel:list, plot_size=40, face_colour="orange") -> None:
        super().__init__("Sun", 1.9889e30, init_pos, init_vel, 
        scatter=Scatter(size=plot_size, face_colour=face_colour),
        trail=Trail((255/255, 182/255, 0, 1)))
    
## sphere
#class Sun(Body):
#    
#    def __init__(self, init_pos:list, init_vel:list, colour="orange") -> None:
#        super().__init__("Sun", 1.9889e30, init_pos, init_vel, 
#        scatter=Scatter(radius=6.957e8, colour=colour),
#        trail=Trail((255/255, 182/255, 0, 1)))
    