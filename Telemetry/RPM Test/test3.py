import smbus
import time
 
LED1 = 0x01
LED2 = 0x02
LED3 = 0x04
LED4 = 0x08
LED5 = 0x10
LED6 = 0x20
LED7 = 0x40
LED8 = 0x80
bus = smbus.SMBus(1)

#bus.write_byte(0x21, LED2)

while True:
	encoder = bus.read_byte_data(0x21, LED1)
	print encoder
	if encoder == 1:
		print("here 1")
		#bus.write_byte(0x21, LED2)
		bus.write_byte_data(0x21, LED2, 0x01)
		time.sleep(0.5)
	else:
		bus.write_byte(0x21, LED2)
		#bus.write_byte_data(0x21, LED2, 0x00)
		time.sleep(0.5)
	#bus.write_byte(0x20, LED3)
	#time.sleep(0.5)
	#bus.write_byte(0x20, LED4)
	#time.sleep(0.5)
