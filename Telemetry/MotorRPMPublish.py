import RPi.GPIO as g
import paho.mqtt.client as mqtt
from time import sleep

g.setmode(g.BCM)

# Define the pins for each motor
motor_pins = {
    'lf': 18,  # Left Front
    'rf': 23,  # Right Front
    'lr': 24,  # Left Rear
    'rr': 25   # Right Rear
}

# Initialize a dictionary to store the revolution counts for each motor
rev_counts = {
    'lf': 0,
    'rf': 0,
    'lr': 0,
    'rr': 0
}

# Define the callback function for each motor
def increaserev(motor):
    global rev_counts
    rev_counts[motor] += 1

# Set up event detection for each motor
for motor, pin in motor_pins.items():
    g.setup(pin, g.IN)
    g.add_event_detect(pin, g.RISING, callback=lambda channel: increaserev(motor))

# Define the Mosquitto client
client = mqtt.Client()
client.connect("localhost", 1883)

# Continuously monitor and publish RPM for each motor
while True:
    sleep(1)
    for motor, rev_count in rev_counts.items():
        rpm = rev_count * 6 / 2
        topic = f"robot/motor/{motor}/rpm"
        message = str(rpm)
        client.publish(topic, message)
        print(f"Motor {motor.upper()} RPM: {rpm}")
        rev_counts[motor] = 0
