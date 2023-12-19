import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import paho.mqtt.client as mqtt

# MQTT broker details
broker_address = "localhost"
broker_port = 1883
topic = "wifi/ssids"

class MQTTSubscriberApp(App):
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        client.subscribe(topic)

    def on_message(self, client, userdata, msg):
        ssids = msg.payload.decode().split(",")
        print("Received SSIDs:", ssids)
        self.display_ssids(ssids)

    def display_ssids(self, ssids):
        self.root.clear_widgets()

        layout = BoxLayout(orientation="vertical")

        title_label = Label(text="Available SSIDs:")
        layout.add_widget(title_label)

        for ssid in ssids:
            ssid_label = Label(text=ssid)
            layout.add_widget(ssid_label)

        refresh_button = Button(text="Refresh", on_release=self.refresh_ssids)
        layout.add_widget(refresh_button)

        self.root.add_widget(layout)

    def refresh_ssids(self, instance):
        self.root.clear_widgets()
        loading_label = Label(text="Loading SSIDs...")
        self.root.add_widget(loading_label)

        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message

        client.connect(broker_address, broker_port, 60)
        client.loop_start()

    def build(self):
        self.root = Box
