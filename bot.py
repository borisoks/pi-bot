import drive
import paho.mqtt.client as mqtt
from time import sleep # Import the sleep function from the time module
from picamera import PiCamera

camera = PiCamera()

topic = "pi-bot/move"
photoTopic = "pi-bot/photo"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic)

    drive.beepOn()
    drive.lightOn()
    sleep(2)
    drive.beepOff()
    drive.lightOff()

    setupCamera()

def setupCamera():
    camera.vflip = True
    camera.resolution = (200, 200)
    camera.framerate = 5
    camera.start_preview()

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    m = str(msg.payload)
    print("mqtt.on_message: topic= " + msg.topic + " message: " + m)
    if m == b'photo':
        print("Taking photo...")
        imgLocation = '/home/pi/pi-bot/img.jpg'
        # camera.resolution = (200, 200)
        # camera.framerate = 15
        # camera.start_preview()
        # sleep(3)
        camera.capture(imgLocation)
        # camera.stop_preview()

        with open(imgLocation) as fp:
            imgData = fp.read()
            client.publish(photoTopic, imgData)
            print("Published photo to " + photoTopic)

    else:
        drive.command(m)

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
