import paho.mqtt.client as mqtt
import pywifi

# MQTT broker details
broker_address = "localhost"
broker_port = 1883
topic = "wifi/ssids"

def list_available_ssids(interface):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[interface]
    iface.scan()
    ssids = [network.ssid for network in iface.scan_results() if network.ssid]
    return ssids

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    ssids = list_available_ssids(interface=0)  # Replace with the index of the desired interface
    client.publish(topic, ",".join(ssids))

client = mqtt.Client()
client.on_connect = on_connect

client.connect(broker_address, broker_port, 60)
client.loop_forever
