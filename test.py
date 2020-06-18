import paho.mqtt.client as mqtt
import sys
from time import sleep

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("pi-bot/move")

    cmd = str(sys.argv[1])

    print("Command: " + cmd)

    client.publish("pi-bot/move", str(cmd))

    # sleep(5)

    # exit()

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("mqtt.on_message: topic= " + msg.topic + " message: " + str(msg.payload))
    exit()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()