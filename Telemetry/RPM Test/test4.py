import RPi.GPIO as GPIO
import time

import Queue
import threading

GPIO.setmode(GPIO.BCM)
speedpin=18
GPIO.setup(speedpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


queue = Queue.Queue()

def printQueue():
    while True:
        s = queue.get()
        print(s)

ta = threading.Thread(target=printQueue)
ta.start()

START = 0
WAIT_POS_EDGE = 1
WAIT_NEG_EDGE = 2

state = START

t0 = time.time()

while True:
    time.sleep(0.0005)
    i = GPIO.input(speedpin)
    if state == START:
        if i == 0:
            state = WAIT_POS_EDGE
            
    elif state == WAIT_POS_EDGE:
        if i == 1:
            t1 = time.time()
            queue.put( "{t:f}".format(t=(t1-t0)))
            t0 = t1
            state = WAIT_NEG_EDGE
    
    elif state == WAIT_NEG_EDGE:
        if i == 0:
            state = WAIT_POS_EDGE
    
