from lib.remote_driving import RemoteDriving
from lib.distance_protection import DistanceProtection
#from bluedot_drive import BlueDotDrive
from time import sleep


dr = RemoteDriving()

#drive = BlueDotDrive(autostart=False)
prot = DistanceProtection(stopper = dr)

#drive.run()

while True:
    dr.listen()