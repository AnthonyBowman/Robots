import paho.mqtt.client as mqtt

# MQTT broker details
broker_address = "localhost"
broker_port = 1883
topic = "wifi/details"

# Path to wpa_supplicant.conf file
wpa_supplicant_file = "/etc/wpa_supplicant/wpa_supplicant.conf"


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic)


def on_message(client, userdata, msg):
    message = msg.payload.decode("utf-8")
    print("Received message: " + message)
    ssid, password = message.split(",")
    update_wpa_supplicant(ssid, password)


def update_wpa_supplicant(ssid, password):
    # Open the wpa_supplicant.conf file in append mode
    with open(wpa_supplicant_file, "a") as file:
        file.write(f'\nnetwork={{\n\tssid="{ssid}"\n\tpsk="{password}"\n}}\n')
        print("Wi-Fi network configuration added to wpa_supplicant.conf")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, broker_port, 60)

client.loop_forever()
