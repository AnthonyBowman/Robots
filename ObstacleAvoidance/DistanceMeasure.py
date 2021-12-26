# Measuring distance

import time
from gpiozero import DistanceSensor

# define gpio pins on the Pi
pinTrigger = 17
pinEcho = 18

sensor = DistanceSensor(echo=pinEcho, trigger=pinTrigger)
print ("Ultrasonic Measurement")

try:
	# repeat the indent block forever
	while True:
		print ("Distance: %.1f cm" % sensor.distance * 100)
		time.sleep(0.5)
		
# if you press ctrl+c, cleanup and stop
except KeyboardInterrupt:
	print ("Exiting")