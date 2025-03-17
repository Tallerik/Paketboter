from lib.remote_driving import RemoteDriving
from time import sleep


dr = RemoteDriving()


while True:
    dr.listen()
    sleep(0.1)