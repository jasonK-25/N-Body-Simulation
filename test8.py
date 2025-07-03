from app.extended.system import SunEarthMoonRealistic
import copy

s1 = SunEarthMoonRealistic()
s2 = copy.deepcopy(s1)


s1.G = 1

print(s1.G == s2.G)

s1.eval_gravitation()
s1.update()
for i in range(len(s1.bodies)):
    print(s1.bodies[i].r == s2.bodies[i].r)
