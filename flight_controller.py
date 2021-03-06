#!/usr/bin/python3
'''
For collecting in-flight data from a samara-based device.
Elaine Jeffery
28 June 2018
'''

import RPi.GPIO as GPIO
from sensor_lib import *
from os import system, popen
from time import time


# GPIO setup.
GPIO.setmode(GPIO.BOARD)

battery_low = 7
buzzer_pin = 11
switch_pin = 12

GPIO.setup(battery_low, GPIO.IN)
GPIO.setup(buzzer_pin, GPIO.OUT)
GPIO.setup(switch_pin, GPIO.IN, GPIO.PUD_UP)

# Sensor objects setup.
gps = GPS()
alt = MPL3115A2()

# Signal completion of start procedure.
print("Startup complete.")
buzzer(buzzer_pin, 2)


# Start the main loop.
pwr = True
fly = True
while pwr and fly:
    # Write sensor data to files.
    gps.save()
    alt.save()

    # Check stop switch.
    if not GPIO.input(switch_pin):
        sleep(5)
        if not GPIO.input(switch_pin):
            print("Received shutdown signal. Shutting Down.")
            pwr = False

    # Check battery status.
    if not GPIO.input(battery_low):
        print("Battery low. Shutting down.")
        pwr = False


# Shutdown routine.
gps.stop()
alt.stop()
buzzer(buzzer_pin, 4)
GPIO.cleanup()
system('sudo shutdown -h now')

