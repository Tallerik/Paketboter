import math
from lib.position import Position

# Initial Position to compare from
a = Position(0,0)

pi = math.pi
def points_in_circum(r, n=100):
    return [(math.cos(2*pi/n*x)*r,math.sin(2*pi/n*x)*r) for x in range(0,n+1)]

# Generates Points on a circle to check if returned heading is correct
u = points_in_circum(1, 20)
i = 1
for b in u:
    # Round Points to 2 decimals for easier readability
    t=[0,0]
    t[0] = round(b[0], 2)
    t[1] = round(b[1], 2)

    # Position to compare with (0, 0)
    c = Position(t[0], t[1])
    print(str(i) + ":\t x:  " + str(t[0]) + "\t y: " + str(t[1]) + "  \t = " + str(a.headingTo(c)) + "\t Offset: " + str(a._targetDistrictOffset(c)) )#+ " \t" +("OK " if a.headingTo(c) == t[2] else "Soll " + str(t[2])) )
    i = i+1
