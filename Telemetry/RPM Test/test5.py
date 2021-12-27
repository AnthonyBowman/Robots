import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
speedpin=18
GPIO.setup(speedpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
start = time.time()
duration = 0
vehiclespeed = 0

def speed(channel):
    global duration
    global vehiclespeed
    global end
    global start
    prevstate = 0
    while True:
	
        currentstate=GPIO.input(speedpin)
        
        if(prevstate != currentstate): #if there is change in input
         
           if(currentstate == 1):#if the input is high
                end = time.time()
                duration = end-start
                start = time.time()
                vehiclespeed = int((2*3.14/duration)*0.2)
               
               
        prevstate = currentstate#change previous state for next iteration

# add the event, runs "speed" when an event occurs        
GPIO.add_event_detect(speedpin, GPIO.BOTH, callback=speed)
try:
     
     while True:
         print('time elapse=', duration ,' speed=',vehiclespeed)
         time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
