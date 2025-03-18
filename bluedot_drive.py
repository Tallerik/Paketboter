from signal import pause
from threading import Lock
from lib.stoppable import Stoppable

from bluedot import BlueDot

from pitop import DriveController, ServoMotor


def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)
def berechne_winkel(winkel):
    # Offset von -90 anwenden
    neuer_winkel = winkel - 90
    
    # Den neuen Winkel im Bereich von -180 bis +180 halten
    if neuer_winkel < -180:
        neuer_winkel += 360
    elif neuer_winkel > 180:
        neuer_winkel -= 360
    return neuer_winkel
        

class BlueDotDrive(Stoppable):

    def __init__(self, left_motor = "M1", right_motor = "M0", servo = "S0", color = "#00B2A2", autostart = True):
        self.bd = BlueDot(rows=2, cols=1)
        self.bd[0,1].color = "#FF00FF"
        self.lock = Lock()
        self.block_forward = False

        self.servo = ServoMotor(servo)
        self.servo_angle = 0
        self.servo.target_angle = self.servo_angle

        self.drive = DriveController(left_motor_port=left_motor, right_motor_port=right_motor)

        if autostart:
            self.start()

    def run(self):
        self.bd[0,1].when_pressed = self.start
        self.bd[0,1].when_moved = self.move
        self.bd[0,1].when_released = self.stop_drive

        self.bd[0,0].when_pressed = self.start_cam
        self.bd[0,0].when_moved = self.move_cam

        pause()

    def move(self, pos):
        if self.lock.locked():
            return
        angle = berechne_winkel(pos.angle)
        
        if any(
            [
                angle > 0 and angle < 20,
                angle < 0 and angle > -20,
            ]
        ) and not self.block_forward:
            self.drive.forward(pos.distance, hold=True)
        elif angle > 0 and 20 <= angle <= 160:
            turn_radius = 0 if 70 < angle < 110 else pos.distance
            speed_factor = -pos.distance if angle > 110 else pos.distance
            if not self.block_forward or speed_factor <= 0:
                self.drive.right(speed_factor, turn_radius)
        elif angle < 0 and -160 <= angle <= -20:
            turn_radius = 0 if -110 < angle < -70 else pos.distance
            speed_factor = -pos.distance if angle < -110 else pos.distance
            if not self.block_forward or speed_factor <= 0:
                self.drive.left(speed_factor, turn_radius)
        elif any(
            [
                angle > 0 and angle > 160,
                angle < 0 and angle < -160,
            ]
        ):
            self.drive.backward(pos.distance, hold=True)


    def move_cam(self, pos):
        if pos.top:
            self.servo_angle = self.servo_angle + 10
        elif pos.bottom:
            self.servo_angle = self.servo_angle - 10
        elif pos.middle:
            self.servo_angle = 0
        self.servo_angle = clamp(self.servo_angle, -90, 90)
        self.servo.target_angle = self.servo_angle


    def start_cam(self, pos):
        self.move_cam(pos)

    def stop_drive(self):
        self.lock.acquire()
        self.drive.stop()

    def stop(self):
        self.stop_drive()
        self.lock.release()
        self.block_forward = True

    def unstop(self):
        self.block_forward = False


    def start(self, pos):
        if self.lock.locked():
            self.lock.release()
        self.move(pos)
