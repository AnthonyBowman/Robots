import paho.mqtt.client as mqtt
import time
from gpiozero import CamJamKitRobot

MQTT_SERVER = "localhost"
MQTT_PATH = "CommandChannel"
robot = CamJamKitRobot()

# The test callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    do_commands (str(msg.payload))
    # more callbacks, etc

# This routine decodes and runs the robot
def do_commands (payload):
    print ("in do commands")
    for command in payload:

        if command == "F":
            print ("command = " + command)
            robot.forward()
            time.sleep(1)
            robot.stop()
    
        if command == "f":
            robot.forward()
            time.sleep(2)
            robot.stop()
    
        if command == "B":
            robot.backward()
            time.sleep(1)
            robot.stop()

        if command == "L":
            robot.left()
            time.sleep(0.3)
            robot.stop()
        
        if command == "R":
            robot.right()
            time.sleep(0.3)
            robot.stop()
           
        if command == "X":
            process = False


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(MQTT_SERVER, 1883, 60)
 
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
