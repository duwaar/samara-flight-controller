#!/usr/bin/python3

#Elaine Jeffery
#14 June 2018

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

buzzer = 7
GPIO.setup(buzzer, GPIO.OUT)

for i in range(4):
    GPIO.output(buzzer, True)
    sleep(0.4)
    GPIO.output(buzzer, False)
    sleep(0.4)

GPIO.cleanup()
