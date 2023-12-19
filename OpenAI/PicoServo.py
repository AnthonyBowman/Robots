from machine import Pin, PWM
import time

# Set the frequency of the PWM signals (in Hz)
frequency = 50

# Set the duty cycles for the minimum and maximum positions of the servo
min_duty_cycle = 0.5
max_duty_cycle = 2.5

# Set the duration of the servo pulse (in milliseconds)
pulse_duration = 20

# Calculate the pulse widths for the minimum and maximum positions of the servo
min_pulse_width = int(min_duty_cycle * frequency * pulse_duration / 1000)
max_pulse_width = int(max_duty_cycle * frequency * pulse_duration / 1000)

# Set the GPIO pin to use for the PWM signal
pwm_pin = Pin(12)

# Create a PWM object using the specified pin, frequency, and duty cycle
pwm = PWM(pwm_pin, frequency, min_pulse_width)

# Set the duty cycle to move the servo to the minimum position
pwm.duty(min_pulse_width)
time.sleep(1)

# Set the duty cycle to move the servo to the maximum position
pwm.duty(max_pulse_width)
time.sleep(1)

# Set the duty cycle to move the servo back to the minimum position
pwm.duty(min_pulse_width)
time.sleep(1)

# Stop the PWM signal
pwm.deinit()
