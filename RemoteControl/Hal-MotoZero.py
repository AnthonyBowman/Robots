from gpiozero import Motor, OutputDevice
import time

motorRR = Motor(24, 27)
motorRR_enable = OutputDevice(5, initial_value=1)
motorFR = Motor(6, 22)
motorFR_enable = OutputDevice(17, initial_value=1)
motorFL = Motor(23, 16)
motorFL_enable = OutputDevice(12, initial_value=1)
motorRL = Motor(13, 18)
motorRL_enable = OutputDevice(25, initial_value=1)

def forward():
    motorFR.forward() # half speed forwards
    motorFL.forward() # half speed forwards
    motorRL.forward() # half speed forwards
    motorRR.forward() # half speed forwards
    time.sleep(1)
    motorFR.stop()
    motorFL.stop()
    motorRL.stop()
    motorRR.stop()
    
def backward():
    motorFR.backward() # half speed forwards
    motorFL.backward() # half speed forwards
    motorRL.backward() # half speed forwards
    motorRR.backward() # half speed forwards
    time.sleep(1)
    motorFR.stop()
    motorFL.stop()
    motorRL.stop()
    motorRR.stop()
    
def left():
    motorFR.backward() # half speed forwards
    motorFL.forward() # half speed forwards
    motorRL.forward() # half speed forwards
    motorRR.backward() # half speed forwards
    time.sleep(1)
    motorFR.stop()
    motorFL.stop()
    motorRL.stop()
    motorRR.stop()
    
def right():  
    motorFR.forward() # half speed forwards
    motorFL.backward() # half speed forwards
    motorRL.backward() # half speed forwards
    motorRR.forward() # half speed forwards
    time.sleep(1)
    motorFR.stop()
    motorFL.stop()
    motorRL.stop()
    motorRR.stop()
    
# set up the MotorZero controller
#def setupMotorZero ():