# This code will run a DC motor at half speed for 2 seconds, and then stop the motor. 
# You can adjust the pin_pwma.value to control the speed of the motor, 
# and use the pin_ain1 and pin_ain2 pins to control the direction of the motor.

import time
import board
import digitalio

# configure the TB6612FNG pins
pin_ain1 = digitalio.DigitalInOut(board.D12)
pin_ain2 = digitalio.DigitalInOut(board.D11)
pin_pwma = digitalio.DigitalInOut(board.D10)
pin_stby = digitalio.DigitalInOut(board.D9)

# set the pins as output
pin_ain1.direction = digitalio.Direction.OUTPUT
pin_ain2.direction = digitalio.Direction.OUTPUT
pin_pwma.direction = digitalio.Direction.OUTPUT
pin_stby.direction = digitalio.Direction.OUTPUT

# set the standby pin high to enable the motor controller
pin_stby.value = True

# set the motor speed to 50%
pin_pwma.value = 0.5

# run the motor forward
pin_ain1.value = True
pin_ain2.value = False

# run the motor for 2 seconds
time.sleep(2)

# stop the motor
pin_pwma.value = 0


### version using MicroPython
import time
import machine

# configure the TB6612FNG pins
pin_ain1 = machine.Pin(12, machine.Pin.OUT)
pin_ain2 = machine.Pin(11, machine.Pin.OUT)
pin_pwma = machine.PWM(machine.Pin(10), freq=1000)
pin_stby = machine.Pin(9, machine.Pin.OUT)

# set the standby pin high to enable the motor controller
pin_stby.value(1)

# set the motor speed to 50%
pin_pwma.duty(512)

# run the

