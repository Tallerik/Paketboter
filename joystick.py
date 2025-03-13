from pitop.pma.adc_base import ADCBase

class JoyStick:
    def __init__(self, port):
        self.x = AbstractJoyStick(port_name=port, pin_number=2)
        self.y = AbstractJoyStick(port_name=port, pin_number=1)

    @property
    def isPressed(self) -> bool:
        return self.y.value == 999

    """
    Returns values for both axis
    :return x,y
    """
    def read(self):
        return int(self.x.value), int(self.y.value)
    
    def _normalize(self, value):
        if value < 0:
            value = 0
        if value > 1:
            value = 1
        return value

    def read_normal(self):
        x,y = self.read()
        nx = (x-250) / 500
        ny = (y-250) / 500
        return self._normalize(nx), self._normalize(ny)


class AbstractJoyStick(ADCBase):
    def __init__(
        self, port_name, pin_number, name="joystick", number_of_samples=3
    ):
        if name == "joystick":
            name = "joystick_"+str(pin_number)
        
        ADCBase.__init__(
            self,
            port_name=port_name,
            pin_number=pin_number,
            name=name,
            number_of_samples=number_of_samples,
        )
 
    @property
    def value(self):
        return self.read()
 