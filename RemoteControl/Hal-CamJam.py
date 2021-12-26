import time
from gpiozero import CamJamKitRobot
robot = CamJamKitRobot()

def forward():
    robot.forward()
    time.sleep(1)
    robot.stop()
    
def backward():
    robot.backward()
    time.sleep(1)
    robot.stop()
    
def left():
    robot.left()
    time.sleep(0.3)
    robot.stop()
    
def right():
    robot.right()
    time.sleep(0.3)
    robot.stop()   

# set up CamJam controller
# def setupCamJam():    