from vispy.scene.visuals import Line


class Trail:

    def __init__(self, colour:str, length=30, width=2) -> None:
        self.r_array = []
        self.colour = colour
        self.length = length
        self.width = width
        self.line = Line(color=colour, width=width)

    def append(self, r) -> None:

        # limit trail length
        if len(self.r_array) >= self.length:
            self.r_array.pop(0)
            
        self.r_array.append(r)
