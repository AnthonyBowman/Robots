import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
#GPIO.setup(23, GPIO.OUT)
#GPIO.setup(24, GPIO.OUT)
print("Lights on")
GPIO.output(18, GPIO.HIGH)
time.sleep(2.5)
GPIO.output(18, GPIO.LOW)
#GPIO.output(23, GPIO.HIGH)
#GPIO.output(24, GPIO.HIGH)
