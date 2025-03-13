

from lib.position import Position

a = Position(0,0)
b = Position(0,1) # 1 0: 90,     0 1: 0

#print(a.headingTo(b))

import math
pi = math.pi

def PointsInCircum(r,n=100):
    return [(math.cos(2*pi/n*x)*r,math.sin(2*pi/n*x)*r) for x in range(0,n+1)]

s = [
    [0,0,0],
    [0,1,0],
    [1,0,90],
    [1,1,45],
    [0,-1,180],
    [-1,0,-90],
    [-1,-1,-135],
    [-1,1,-45],
    [1, -1,135]
]
u = PointsInCircum(1, 20)
i = 1
for b in u:
    t=[0,0]
    t[0] = round(b[0], 2)
    t[1] = round(b[1], 2)
    c = Position(t[0], t[1])
    print(str(i) + ":\t x:  " + str(t[0]) + "\t y: " + str(t[1]) + "  \t = " + str(a.headingTo(c)) + "\t Offset: " + str(a._targetDistrictOffset(c)) )#+ " \t" +("OK " if a.headingTo(c) == t[2] else "Soll " + str(t[2])) )
    i = i+1

"""
from joystick import JoyStick
from time import sleep


stick = JoyStick("A1")

while True:
    val1,val2 = stick.read()
    #print("Pin 1: " + str(val1))
    print("Pin 2: " + str(val2))
    if stick.isPressed:
        print("Pressed!")
    #print()
    sleep(0.2)
"""