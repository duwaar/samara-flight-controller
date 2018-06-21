#!/usr/bin/python3

import smbus
from os import system
from time import sleep

bus = smbus.SMBus(1) # Pass in the number of the bus your device is on (I think).

# Note: hex format starts with "0x" and is followed by the hex number.
address = input("Enter the address of your device in hex format: ")
address = int(address, 16)
scan = input("Enter the highest register number you wish to scan to in hex format: ")
scan = int(scan, 16)

while True:
    input("Hit enter to refresh.")
    system("clear")
    print("sent:\t\trecieved:") # Print column headers.
    for i in range(scan):
        msg = bus.read_byte_data(address, i) # Send a message and record the response.
        if msg != 0:
            print(hex(i) + "\t\t" + hex(msg))
        else:
            pass


