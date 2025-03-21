from pitop import UltrasonicSensor
from lib.stoppable import Stoppable
from navigator import Navigator, Action

class DistanceProtection:

    def __init__(self, stopper: Stoppable, port = "D3", max_dist = 0.3):
        self.distance_sensor = UltrasonicSensor(port, threshold_distance=max_dist)
        self.distance_sensor.when_in_range = self.in_range
        self.distance_sensor.when_out_of_range = self.release
        self.stopper = stopper

    def in_range(self):
        if isinstance(self.stopper, Navigator):
            if self.stopper.action == Action.GOTO:
                self.stopper.stop()
        else:
            self.stopper.stop()
        print("In range")
    
    def release(self):
        self.stopper.unstop()
        print("Released")


# Set up functions to print when an object crosses 'threshold_distance'

#distance_sensor.when_out_of_range = lambda: print("out of range")
