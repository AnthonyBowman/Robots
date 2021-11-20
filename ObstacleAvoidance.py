# Collision avoidance
import time 
from gpiozero import CamJamKitRobot, DistanceSensor

# define GPIO pins to use for the sensor distance
pintrigger = 17
pinecho = 18

robot = CamJamKitRobot()
sensor = DistanceSensor(echo=pinecho, trigger=pintrigger)

# distance variables
hownear = 15.0
reversetime = 1.0
turntime = 0.75

# set the relative speeds of the two motors
leftmotorspeed = 0.3
rightmotorspeed = 0.3

motorforward = (leftmotorspeed, rightmotorspeed)
motorbackward = (-leftmotorspeed, -rightmotorspeed)
motorleft = (leftmotorspeed, 0)
motorright = (0, rightmotorspeed)

# return true if the ultrasonic sensor sees an obstacle
def isnearobstacle(localhownear):
	distance = sensor.distance * 100
	print ("IsNearObstacle: " + str(distance))
	if distance < localhownear:
		return True
	else:
		return False
        
# move back a little, the turn right
def avoidobstacle():
    print ("Backwards")
    robot.value = motorbackward
    time.sleep(reversetime)
    robot.stop()
    
    #turn right
    print ("Right")
    robot.value = motorright
    time.sleep(turntime)
    robot.stop()
    
# code to control robot
try:
    while True:
        robot.value = motorforward
        distance = sensor.distance * 100
        print("distance=" + str(distance))
        time.sleep(0.1)
        if isnearobstacle(hownear):
            robot.stop()
            avoidobstacle()
  
# press ctrl+c to cleanup and stop
except KeyboardInterrupt:
    robot.stop()
            
        
        
        
        
		
