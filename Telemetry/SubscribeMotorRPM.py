import paho.mqtt.client as mqtt

# Define the Mosquitto client
client = mqtt.Client()
client.connect("localhost", 1883)

# Define the callback function to print RPM values
def on_message(client, userdata, message):
    print(f"{message.topic}: {message.payload.decode()} RPM")

# Subscribe to the topics for each motor
for motor in ['lf', 'rf', 'lr', 'rr']:
    topic = f"robot/motor/{motor}/rpm"
    client.subscribe(topic)
    print(f"Subscribed to {topic}")

# Start the loop to listen for messages
client.on_message = on_message
client.loop_forever()
