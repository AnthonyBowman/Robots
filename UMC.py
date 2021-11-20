# Universal MQTT robot control
import paho.mqtt.client as mqtt
import time
import hal

MQTT_SERVER = "localhost"
MQTT_PATH = "CommandChannel"

# The test callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if (msg.retain != 1):
        do_commands (str(msg.payload))
    # more callbacks, etc
	        

# This routine decodes and runs the robot
def do_commands (payload):
    print ("in do commands")
    for command in payload:
   
        if command == "F":
            # move forward
            hal.forward ()
            
        if command == "B":
            # collisioncount = 0
            hal.backward()
            
        if command == "L":
            hal.left()
            
        if command == "R":
            hal.right()
            
        if command == "E":
            hal.cleanup()
            
# main body of the program although do commands is where it really
# all happens.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(MQTT_SERVER, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
