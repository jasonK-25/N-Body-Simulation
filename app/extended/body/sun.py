from ...base.body import Body
from ...graphics.trail import Trail
from ...graphics.scatter import Scatter
from ...graphics.line import Line


class Sun(Body):
    
    def __init__(self, init_pos:list, init_vel:list, plot_size=40, colour=[1, 0.7, 0, 1]) -> None:
        super().__init__("Sun", 1.9889e30, init_pos, init_vel, 
        scatter=Scatter(size=plot_size, colour=colour),
        trail=Trail([1, 1, 1, 1]),
        gpe_line=Line("red", 5), ke_line=Line("green", 5), tot_energy_line=Line("blue", 5))
    
## sphere
#class Sun(Body):
#    
#    def __init__(self, init_pos:list, init_vel:list, colour="orange") -> None:
#        super().__init__("Sun", 1.9889e30, init_pos, init_vel, 
#        scatter=Scatter(radius=6.957e8, colour=colour),
#        trail=Trail((255/255, 182/255, 0, 1)))
    