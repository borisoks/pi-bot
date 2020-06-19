import drive
import paho.mqtt.client as mqtt
from time import sleep # Import the sleep function from the time module

topic = "pi-bot/move"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic)

    drive.beepOn
    drive.lightOn
    sleep(2)
    drive.beepOff
    drive.lightOff

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("mqtt.on_message: topic= " + msg.topic + " message: " + str(msg.payload))
    drive.command(msg.payload)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)

drive.setup()

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
