import math

class Orbit(object):

    def circular_orbit(self, center, radius, speed, t):
        theta = math.fmod(t * speed, 3.14 * 2)
        c = math.cos(theta)
        s = math.sin(theta)
        return center[0] + radius * c, center[1] + radius * s

orbit = Orbit()
center = [0, 0]

for i in range(0,5):
    print(orbit.circular_orbit(center, 2, 2, i))
