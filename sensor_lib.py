#!/usr/bin/python3

'''
A library of sensor utilities.
Russell Jeffery
18 June 2018
'''

import RPi.GPIO as GPIO
from time import sleep, time
from os import system, popen
import serial
import smbus



def buzzer(buzzer_pin, beeps):
    '''
    Makes four chirps given the pin that the buzzer is attached to.
    '''
    for i in range(beeps):
        GPIO.output(buzzer_pin, True)
        sleep(0.4)
        GPIO.output(buzzer_pin, False)
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


class GPS():
    def __init__(self, port='/dev/ttyS0'):
        self.ser = serial.Serial(port) # Or whatever port the GPS is on.

        # Open a data file.
        filename = "position_" + str(time()) + ".txt"
        self.file = open(filename, mode='x')


    def get(self):
        '''
        Get a line of GPS data.
        '''
        # Search for $GPGGA sentences only.
        got_it = False
        while not got_it:
            line = self.ser.readline()
            line = str(line)
            if line[5:8] == 'GGA':
                got_it = True
        
        return line


    def save(self):
        '''
        Write data to a file.
        '''
        data = self.get()
        line = str(time()) + ',' + str(data) + '\n'
        self.file.write(line)


    def stop(self):
        '''
        Gracefully end the processes.
        '''
        self.file.close()

        

class MPL3115A2():
    def __init__(self, port=1, device='0x60'):
        # Device: the MPL3115A2.
        self.dev = int(device, 16)

        # Connects to i2c-1 by default.
        self.bus = smbus.SMBus(port)

        # Configure the chip.
        reg = int('0x26', 16) # Address control register 1.
        cmd = int('0x80', 16) # Set to altimeter mode.
        self.bus.write_byte_data(self.dev, reg, cmd)

        # Open a data file.
        filename = "altitude_" + str(time()) + ".txt"
        self.file = open(filename, mode='x')


    def get(self):
        '''
        Get one sample of altitude data.
        '''
        reg = int('0x26', 16) # Address control register 1.
        cmd = int('0x82', 16) # Initiate one-shot measurement.
        self.bus.write_byte_data(self.dev, reg, cmd)

        # Get altitude data from the chip.
        reg = int('0x1', 16)
        byte1 = self.bus.read_byte_data(self.dev, reg)
        reg = int('0x2', 16)
        byte2 = self.bus.read_byte_data(self.dev, reg)
        reg = int('0x3', 16)
        byte3 = self.bus.read_byte_data(self.dev, reg)

        # Adjust magnitudes.
        num1 = byte1 << 8
        num2 = byte2
        num3 = byte3 >> 4 # The four LSBs of this register are not used.

        # Convert integer to decimal.
        while num3 >= 1:
            num3 = num3 / 10

        # Combine parts.
        num = num1 + num2 + num3

        # Two's comp. Invert if necessary.
        if num >= 32768:
            num = num - 65536

        return num # This number should be altitude in meters.


    def save(self):
        '''
        Save an altitude reading to a file.
        '''
        data = self.get()
        line = str(time()) + ',' + str(data) + '\n'
        self.file.write(line)


    def stop(self):
        '''
        Gracefully end the processes.
        '''
        self.file.close()



