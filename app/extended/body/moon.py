from ...base.body import Body
from ...base.trail import Trail
from ...graphics.scatter import Scatter
from ...graphics.line import Line


class Moon(Body):
    
    def __init__(self, init_pos:list, init_vel:list, name="Moon", plot_size=10, colour="white") -> None:
        super().__init__(name, 7.348e22, init_pos, init_vel, 
        scatter=Scatter(size=plot_size, colour=colour),
        trail=Trail((1, 1, 1, 1)),
        gpe_line=Line("red", 5), ke_line=Line("green", 5), tot_energy_line=Line("blue", 5))

# sphere
#class Moon(Body):
#    
#    def __init__(self, init_pos:list, init_vel:list, name="Moon", colour="white") -> None:
#        super().__init__(name, 7.348e22, init_pos, init_vel, 
#        scatter=Scatter(radius=1738100, colour=colour),
#        trail=Trail("white"))

    