from ...base.body import Body
from ...base.trail import Trail
from ...graphics.scatter import Scatter
from ...graphics.line import Line


class Earth(Body):
    
    def __init__(self, init_pos:list, init_vel:list, name="Earth", plot_size=20, colour="blue") -> None:
        super().__init__(name, 5.972e24, init_pos, init_vel, 
        scatter=Scatter(size=plot_size, colour=colour),
        trail=Trail((38/255, 185/255, 255/255, 0/255), 20), # light blue
        gpe_line=Line("red", 5), ke_line=Line("green", 5), tot_energy_line=Line("blue", 5)) 
    
## sphere
#class Earth(Body):
#    
#    def __init__(self, init_pos:list, init_vel:list, name="Earth", colour="blue") -> None:
#        super().__init__(name, 5.972e24, init_pos, init_vel, 
#        scatter=Scatter(radius=6378100, colour=colour),
#        trail=Trail("white"))
