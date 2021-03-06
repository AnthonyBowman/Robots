# Servo2.py
# Two servo motors driven by PCA9685 chip

from smbus import SMBus
from PCA9685 import PWM
import time

fPWM = 50
i2c_address = 0x40 # (standard) adapt to your module
servo0 = 0 # adapt to your wiring
servo1 = 1 # 
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
    print "channel = ", channel, " direction =", direction, "-> duty =", duty
    time.sleep(1) # allow to settle
   
print "starting"
setup()
setDirection(11, servo1)
setDirection(51, servo1)
#setDirection(11, servo1)
#setDirection(-51, servo1)

for direction in range(21, 121, 10): #181
    setDirection(direction, servo0)
direction = 21    
setDirection(21, servo0)    
print "done"
  

