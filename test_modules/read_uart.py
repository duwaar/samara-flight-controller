#!/usr/bin/python3

# Basic Serial Read
# Elaine Jeffery
# 15 June 2018

import serial

ser = serial.Serial('/dev/ttyS0') # Or whatever port your device shows up on.

while True:
    print(ser.readline())

