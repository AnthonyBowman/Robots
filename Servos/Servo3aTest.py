# Servo2.py
# Two servo motors driven by PCA9685 chip

from smbus import SMBus
from PCA9685 import PWM
import time

fPWM = 50
i2c_address = 0x40 # (standard) adapt to your module
servo0 = 0 # adapt to your wiring
servo1 = 1 #
servo2 = 2
servo3 = 3
a = 8.5 # adapt to your servo
b = 2  # adapt to your servo

def setup():
    global pwm
    bus = SMBus(1) # Raspberry Pi revision 2
    pwm = PWM(bus, i2c_address)
    pwm.setFreq(fPWM)

def setDirection(direction, channel):
    duty = a / 180 * direction + b
    pwm.setDuty(channel, duty)
    print ("channel = ", channel, " direction =", direction, "-> duty =", duty)
    time.sleep(1) # allow to settle

def look (direction, servo):
    dict = {'R':1, 'M':90, 'L':179};
    res=dict[direction]
    setDirection(res, servo)

print ("starting")
setup()
#setDirection(90, servo0)
#setDirection(51, servo1)
#setDirection(11, servo1)
#setDirection(-51, servo1)

# servo 3
look('M', servo3)
look('R', servo3)
look('M', servo3)
look('L', servo3)
look('M', servo3)

#setDirection(175, servo2)
for direction in range(20, 160, 10): #181
    setDirection(direction, servo2)
#direction = 21
#setDirection(21, servo0)
print ("done")


