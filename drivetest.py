from pitop import LED
from navigator import Navigator
from time import sleep

led1 = LED("D3")
led2 = LED("D6")
led3 = LED("D7")
led4 = LED("D0")


led1.on()
led2.on()
led3.blink(background=True, on_time=0.2, off_time=0.2)
led4.blink(background=True, on_time=0.2, off_time=0.2)

nav = Navigator()

nav.goto(0, 1)
sleep(5)
nav.goto(1, 1)
sleep(5)
nav.goto(1, 0)
sleep(5)
nav.goto(0, 0)
while True:
    sleep(1)
