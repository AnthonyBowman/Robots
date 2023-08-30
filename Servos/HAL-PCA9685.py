# HAL-PCA9685.py
# this moves the camera up,down and east, west
from smbus import SMBus
from PCA9685 import PWM
import time

# set up some constants
fPWM = 50 # default PWM value 
i2c_address = 0x40 # (standard) adapt to your module
servoEW = 0 # adapt to your wiring
servoUD = 1 # 
a = 8.5 # adapt to your servo
b = 2  # adapt to your servo

# set up function
def setup():
    global pwm
    bus = SMBus(1) # Raspberry Pi revision 2
    pwm = PWM(bus, i2c_address)
    pwm.setFreq(fPWM)

# move servos as needed
def moveEastWest(degrees):
    moveServoDegrees(servoEW, degrees)

def moveUpDown (degrees):
    moveServoDegrees(servoUD, degrees)

# Global variable to store the absolute position
absolutePosition = 0

def moveServoDegrees(servo, degrees):
    global absolutePosition
    newPosition = absolutePosition + degrees
    
    if -180 <= newPosition <= 180:
        absolutePosition = newPosition
        moveServoAbsolute(servo, absolutePosition)
    else:
        print("Degrees out of range!")

def moveServoAbsolute(servo, position):
    # Map absolute position to duty cycle
    duty = 2.5 + (position / 18)
    pwm.setDuty(servo, duty)
    time.sleep(1)  # You can adjust this sleep time as needed        
