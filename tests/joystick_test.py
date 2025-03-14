from lib.joystick import JoyStick
from time import sleep

# Initialize JoyStick on Port A1
stick = JoyStick("A1")

while True:
    # Read Value
    val1,val2 = stick.read()
    
    print("Pin 1: " + str(val1))
    print("Pin 2: " + str(val2))
    if stick.is_pressed:
        print("Pressed!")
    #print()
    sleep(0.2)