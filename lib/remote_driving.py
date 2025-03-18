from pitop import EncoderMotor, ForwardDirection
from pitop import ServoMotor, ServoMotorSetting
import socket

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)


class RemoteDriving:

    def __init__(self, left_motor = "M1", right_motor = "M0"):
        self.left = EncoderMotor(
            port_name=left_motor,
            forward_direction=ForwardDirection.CLOCKWISE,
        )
        self.right = EncoderMotor(
            port_name=right_motor,
            forward_direction=ForwardDirection.COUNTER_CLOCKWISE,
        )

        self.servo = ServoMotor("S0")
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('', 12000))

    
    def listen(self):
        data, addr = self.socket.recvfrom(1024)
        self._process(data)
    
    def _process(self, data):
        params = data.decode("utf-8").strip().split(";")
        print(params)

        speed_multiplier = float(params[0]) - 0.5
        direction_multiplier = float(params[1]) - 0.5

        speed_left = speed_multiplier + self._get_direction_multiplier(direction_multiplier, False)
        speed_right = speed_multiplier + self._get_direction_multiplier(direction_multiplier, True)
        
        speed_left = clamp(speed_left * 2, -1, 1)
        speed_right = clamp(speed_right * 2, -1, 1)

        print('Speed: ' + str(speed_multiplier) + '\nDir: ' + str(direction_multiplier) + '\nLeft: ' + str(speed_left) + '\nRight: ' + str(speed_right))
        
        self.left.set_power(speed_left)
        self.right.set_power(speed_right)

        self.servo.target_angle = translate(float(params[2]), 0, 1, -90, 90)

    def _get_direction_multiplier(self, value: float, is_right: bool):
        statement = (value > 0.5) if is_right else (value < 0.5)
        if (value == 0.5):
            return 0
        else:
            return value if statement else -1 * value
