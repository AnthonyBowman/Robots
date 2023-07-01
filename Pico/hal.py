import machine
from machine import Pin, PWM

# Pin definitions for Motor Controller 1
LF_AIN1 = Pin(2, Pin.OUT)   # Left Front Motor input 1
LF_AIN2 = Pin(3, Pin.OUT)   # Left Front Motor input 2
LF_PWMA = PWM(Pin(4))       # Left Front Motor PWM

LR_AIN1 = Pin(5, Pin.OUT)   # Left Rear Motor input 1
LR_AIN2 = Pin(6, Pin.OUT)   # Left Rear Motor input 2
LR_PWMA = PWM(Pin(7))       # Left Rear Motor PWM

# Pin definitions for Motor Controller 2
RF_BIN1 = Pin(8, Pin.OUT)   # Right Front Motor input 1
RF_BIN2 = Pin(9, Pin.OUT)   # Right Front Motor input 2
RF_PWMB = PWM(Pin(10))      # Right Front Motor PWM

RR_BIN1 = Pin(11, Pin.OUT)  # Right Rear Motor input 1
RR_BIN2 = Pin(12, Pin.OUT)  # Right Rear Motor input 2
RR_PWMB = PWM(Pin(13))      # Right Rear Motor PWM

# Motor control functions
def motorLF_forward(speed):
    LF_AIN1.on()
    LF_AIN2.off()
    LF_PWMA.duty(speed)

def motorLF_backward(speed):
    LF_AIN1.off()
    LF_AIN2.on()
    LF_PWMA.duty(speed)

def motorLF_stop():
    LF_AIN1.off()
    LF_AIN2.off()
    LF_PWMA.duty(0)

def motorLR_forward(speed):
    LR_AIN1.on()
    LR_AIN2.off()
    LR_PWMA.duty(speed)

def motorLR_backward(speed):
    LR_AIN1.off()
    LR_AIN2.on()
    LR_PWMA.duty(speed)

def motorLR_stop():
    LR_AIN1.off()
    LR_AIN2.off()
    LR_PWMA.duty(0)

def motorRF_forward(speed):
    RF_BIN1.on()
    RF_BIN2.off()
    RF_PWMB.duty(speed)

def motorRF_backward(speed):
    RF_BIN1.off()
    RF_BIN2.on()
    RF_PWMB.duty(speed)

def motorRF_stop():
    RF_BIN1.off()
    RF_BIN2.off()
    RF_PWMB.duty(0)

def motorRR_forward(speed):
    RR_BIN1.on()
    RR_BIN2.off()
    RR_PWMB.duty(speed)

def motorRR_backward(speed):
    RR_BIN1.off()
    RR_BIN2.on()
    RR_PWMB.duty(speed)

def motorRR_stop():
    RR_BIN1.off()
    RR_BIN2.off()
    RR_PWMB.duty(0)

# Stop all motors
def stop_all():
    motorLF_stop()
    motorLR_stop()
    motorRF_stop()
    motorRR_stop()

# Move the robot in the specified direction at the given power level
def move(direction, power):
    if direction == "F":
        motorLF_forward(power)
        motorLR_forward(power)
        motorRF_forward(power)
        motorRR_forward(power)
    elif direction == "B":
        motorLF_backward(power)
        motorLR_backward(power)
        motorRF_backward(power)
        motorRR_backward(power)
    elif direction == "L":
        motorLF_backward(power)
        motorLR_forward(power)
        motorRF_forward(power)
        motorRR_backward(power)
    elif direction == "R":
        motorLF_forward(power)
        motorLR_backward(power)
        motorRF_backward(power)
        motorRR_forward(power)
    else:
        stop_all()


# Example usage
#move("forward", 50)   # Move forward at 50% speed
#move("backward", 70)  # Move backward at 70% speed
#move("left", 80)      # Turn left at 80% speed
#move("right", 60)     # Turn right at 60% speed
#stop_all()            # Stop all motors
