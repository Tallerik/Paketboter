from pitop import UltrasonicSensor
from navigator import Navigator, Action

class DistanceProtection:

def __init__(self, navigator: Navigator, port = "D3", max_dist = 0.2):
    self.distance_sensor = UltrasonicSensor(port, threshold_distance=max_dist)
    self.distance_sensor.when_in_range = in_range
    self.navigator = navigator

def in_range(self):
    if self.navigator.action == Action.GOTO:
        self.navigator.stop()
    print("In range")


# Set up functions to print when an object crosses 'threshold_distance'

#distance_sensor.when_out_of_range = lambda: print("out of range")
