from lib.remote_driving import RemoteDriving
from lib.distance_protection import DistanceProtection
from navigator import Navigator
#from bluedot_drive import BlueDotDrive
from time import sleep


dr = RemoteDriving()
#nav = Navigator(turn_factor = 0.1, speed_factor=0.5)
#drive = BlueDotDrive(autostart=False)
prot = DistanceProtection(stopper = dr)

#drive.run()

while True:
    dr.listen()
    #nav.goto (0, 1)
    #nav.goto(1, 1)
    #nav.goto(1, 0.1)
    #nav.goto(0, 0)