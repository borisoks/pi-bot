import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(31, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off6
GPIO.setup(33, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(35,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(37,GPIO.OUT, initial=GPIO.LOW)

GPIO.output(31, GPIO.LOW)
GPIO.output(33, GPIO.LOW)
GPIO.output(35, GPIO.LOW)
GPIO.output(37, GPIO.LOW)

exit()

def go_straight():
 print("Straight")
 GPIO.output(31, GPIO.LOW)
 GPIO.output(33, GPIO.HIGH)
 GPIO.output(35, GPIO.LOW)
 GPIO.output(37, GPIO.HIGH)

def go_back():
 print("Back")
 GPIO.output(31, GPIO.HIGH)
 GPIO.output(33, GPIO.LOW)
 GPIO.output(35, GPIO.HIGH)
 GPIO.output(37, GPIO.LOW)

def turn_right():
 print("Right")
 GPIO.output(31, GPIO.LOW)
 GPIO.output(33, GPIO.HIGH)
 GPIO.output(35, GPIO.LOW)
 GPIO.output(37, GPIO.LOW)

def turn_left():
 print("Left")
 GPIO.output(31, GPIO.LOW)
 GPIO.output(33, GPIO.LOW)
 GPIO.output(35, GPIO.LOW)
 GPIO.output(37, GPIO.HIGH)

def spin():
 print("Spin")
 GPIO.output(31, GPIO.HIGH)
 GPIO.output(33, GPIO.LOW)
 GPIO.output(35, GPIO.LOW)
 GPIO.output(37, GPIO.HIGH)

while True: # Run forever
 go_straight()
 sleep(1)
 turn_right()
 sleep(0.5)
 go_straight()
 sleep(1)
 turn_right()
 sleep(0.5)
 go_straight()
 sleep(1)
 turn_right()
 sleep(0.5)
 go_straight()
 sleep(1)
 turn_right()
 sleep(0.5)

