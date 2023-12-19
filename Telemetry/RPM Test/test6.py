import RPi.GPIO as g
from time import sleep
g.setmode(g.BCM)
rpmpin=18
g.setup(rpmpin, g.IN)
global revcount
revcount = 0
def increaserev(channel):
    global revcount
    revcount += 1
g.add_event_detect(rpmpin, g.RISING, callback=increaserev)
while True:
    sleep(1)
    print ("RPM is {0}".format(revcount*6/2))
    revcount = 0
