#!/usr/bin/python3.4
'''
Starts each sensor script and waits for the shutdown signal from the switch.
Russell Jeffery
27 June 2018
'''

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)




def main():
    '''
    Start the sensors, then wait for the kill signal.


