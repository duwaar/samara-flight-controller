#!/usr/bin/python3

#Servo Driver
#Russell Jeffery
#15 June 2018

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

servo = 7
GPIO.setup(servo, GPIO.OUT)

def setServo(angle):
    # Convert angle to pulse width.
    pulse = angle * (0.001 / 180) + 0.001

    # Send the appropriate signal.
    GPIO.output(servo, True)
    sleep(pulse)
    GPIO.output(servo, False)
    sleep(0.020)


angle = 0
while True:
    print(angle)
    setServo(angle)

    if angle < 180:
        angle += 0.1
    else:
        angle = 0

    


GPIO.cleanup()
