from lib.position import Position
from pitop.robotics import DriveController
from lib.stoppable import Stoppable
from time import sleep
from math import copysign, floor, radians

class Navigator(Stoppable):
    
    def __init__(self, left_motor = "M1", right_motor = "M0", speed_factor = 0.8, turn_factor = 0.3, start_x = 0.0, start_y = 0.0):
        self.initial = Position(start_x,start_y)
        self.current = Position(start_x, start_y)
        self.target = Position()

        self.action = Action.IDLE

        self.speed_factor = speed_factor
        self.turn_factor = turn_factor

        self.drive = DriveController(left_motor_port=left_motor, right_motor_port=right_motor)
        self.max_speed = self.drive.max_motor_speed
        

    def goto(self, x,y):
        self.target = Position(x,y)
        self.action = Action.GOTO

        # Calculate Distance and Heading
        dis = self.current.distanceTo(self.target)
        turn_angle = self.current.deltaHeadingTo(self.target)

        # Turn towards new 
        print("Angle: " + str(-turn_angle))
        print("Factor: " + str(self.turn_factor))
        print("MAX: " + str(self.drive.max_robot_angular_speed * self.turn_factor))
        print("rads: " + str(abs(radians(-turn_angle))))
        print("Time: " + str(abs(radians(-turn_angle)) / (self.drive.max_robot_angular_speed * self.turn_factor)))
        print("Sleep: " + str(self._calculate_turning_duration(turn_angle)))
        if turn_angle != 0:
            self.drive.rotate(angle=-turn_angle, max_speed_factor=self.turn_factor) # Turn
            sleep(self._calculate_turning_duration(turn_angle)) # Wait for the duration of the turn
            self.current.setHeadingTo(self.target) # Sets the heading of current to the new heading

        # Drive forward
        self.drive.forward(self.speed_factor, True, dis)
        sleep(self._calculate_driving_duration(dis)) # Wait for driving to complete

        # Done driving. Save settings and clean up
        self.target.heading = self.current.heading # Save the heading
        self.current = self.target # New current Position is now the old target Position 

        # Reset target position
        self.target = Position()
        # Done, reset action
        self.action = Action.IDLE

    def go_home(self):
        self.goto(self.initial.x, self.initial.y)

    # Inherited from Stoppable
    def stop(self):
        print("stop") #TODO: IMPLEMENT
    def unstop(self):
        pass

    def _calculate_driving_duration(self, distance):
        self.max_speed = self.drive.max_motor_speed # Maybe this can Change?
        target_speed = self.max_speed * self.speed_factor

        return distance / target_speed

    def _calculate_turning_duration(self, angle):
        angle = abs(radians(angle))
        rotation_speed = self.drive.max_robot_angular_speed * self.turn_factor
        return angle / rotation_speed


class Action:
    IDLE = 0
    GOTO = 1