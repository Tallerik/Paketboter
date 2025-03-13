from lib.position import Position
from pitop.robotics import DriveController
from time import sleep

class Navigator:
    
    def __init__(self, x = 0.0, y = 0.0):
        self.current = Position(x,y)
        self.target = Position()
        self.action = Action.IDLE

        self.drive = DriveController(left_motor_port="M3", right_motor_port="M0")
        

    def goto(self, x,y):
        
        self.target = Position(x,y)
        self.action = Action.GOTO

        dis = self.current.distanceTo(self.target)
        turn = self.current.deltaHeadingTo(self.target)

        self.drive.rotate(angle=-turn, time_to_take=1)
        self.current.setHeadingTo(self.target) # Sets the heading of current to the new heading
        
        self.drive.forward(1, True, dis)

        self.target.heading = self.current.heading # Save the heading
        self.current = self.target # New current Position is now the old target Position 
        self.target = Position() # Reset target
        print(self.current.toString())
        self.action = Action.IDLE
        




class Action:
    IDLE = 0
    GOTO = 1