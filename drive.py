import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
# import mock_GPIO as GPIO
import threading

def setup():
 GPIO.setwarnings(False) # Ignore warning for now
 GPIO.setmode(GPIO.BOARD)
 GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) #LED
 GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW) #BUZZER
 GPIO.setup(31, GPIO.OUT, initial=GPIO.LOW)
 GPIO.setup(33, GPIO.OUT, initial=GPIO.LOW)
 GPIO.setup(35, GPIO.OUT, initial=GPIO.LOW)
 GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW)

def lightOn():
    print("lightOn")
    GPIO.output(8, GPIO.HIGH)

def lightOff():
    print("lightOff")
    GPIO.output(8, GPIO.LOW)

def beepOn():
    print("beepOn")
    GPIO.output(10, GPIO.HIGH)

def beepOff():
    print("beepOff")
    GPIO.output(10, GPIO.LOW)

def stop():
 print("Stop")
 GPIO.output(31, GPIO.LOW)
 GPIO.output(33, GPIO.LOW)
 GPIO.output(35, GPIO.LOW)
 GPIO.output(37, GPIO.LOW)

def go_straight():
 print("Straight")
 GPIO.output(31, GPIO.HIGH)
 GPIO.output(33, GPIO.LOW)
 GPIO.output(35, GPIO.HIGH)
 GPIO.output(37, GPIO.LOW)

def go_back():
 print("Back")
 GPIO.output(31, GPIO.LOW)
 GPIO.output(33, GPIO.HIGH)
 GPIO.output(35, GPIO.LOW)
 GPIO.output(37, GPIO.HIGH)

def turn_right():
 print("Right")
 GPIO.output(31, GPIO.LOW)
 GPIO.output(33, GPIO.HIGH)
 GPIO.output(35, GPIO.HIGH)
 GPIO.output(37, GPIO.LOW)

def turn_left():
 print("Left")
 GPIO.output(31, GPIO.HIGH)
 GPIO.output(33, GPIO.LOW)
 GPIO.output(35, GPIO.LOW)
 GPIO.output(37, GPIO.HIGH)

# timer = threading.Timer(0.5, stop)
# timer.start()

def command(cmd):
    # timer.cancel()
    # if timer.is_alive():
    #     timer.cancel()

    # timer = threading.Timer(2.0, stop)
    # timer.start()

    if cmd == b'straight':
        go_straight()
    elif cmd == b'back':
        go_back()
    elif cmd == b'right':
        turn_right()
    elif cmd == b'left':
        turn_left()
    elif cmd == b'beepOn':
        beepOn()
    elif cmd == b'beepOff':
        beepOff()
    elif cmd == b'lightOn':
        lightOn()
    elif cmd == b'lightOff':
        lightOff()
