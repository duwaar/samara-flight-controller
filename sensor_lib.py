#!/usr/bin/python3

'''
A library of sensor utilities.
Russell Jeffery
18 June 2018
'''

import RPi.GPIO as GPIO
from time import sleep
import serial

def buzzer(buzzer):
    '''
    Makes four chirps given the pin that the buzzer is attached to.
    '''
    for i in range(4):
        GPIO.output(buzzer, True)
        sleep(0.4)
        GPIO.output(buzzer, False)
        sleep(0.4)


def set_serial(port):
    '''
    Given a serial port, this will instantiate a Serial object,
    establishing a connection.
    '''
    if str(type(port)) == "<class 'str'>":
        ser = serial.Serial(port)
    else:
        print('Enter a valid serial port path as a string.')

    return ser


def read_serial(ser):
    '''
    This reads one line from the serial port.
    '''
    line = ser.readline()

    return line


   
