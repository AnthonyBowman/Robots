import machine
from machine import Pin
from utime import sleep

pin = Pin("LED", Pin.OUT)

def blink_led():
    print("LED starts flashing...")
    while True:
        pin.toggle()
        sleep(1) # sleep 1sec

# I2C address of the Pico
address = 0x12

# Initialize the I2C bus
i2c = machine.I2C(0, scl=machine.Pin(5), sda=machine.Pin(4), freq=400000)

# Wait for a message
while True:
    try:
        data = i2c.readfrom(address, 1)
        if data[0] == ord('S'):
            # Start the program
            blink_led()
        elif data[0] == ord('X'):
            # Stop the program
            break
    except:
        pass

# Cleanup the I2C bus
#i2c.deinit()
