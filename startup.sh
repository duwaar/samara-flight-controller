#!/bin/bash

cd /home/pi/samara/

# Run the command inside `` and stick the result in "usb".
usb=`lsusb | grep '248a:00da'`

# If "usb" contains anything (test returns true), that means there is
# a keyboard attached. Kill the program.
if [ "$usb" ]; then
    echo "Found a keyboard." > ./start_msg.txt
    exit 0
fi

# Start the flight controller.
python3 ./flight_controller.py 1> fc.out 2> fc.err

echo "startup.sh has finished." > ./start_msg.txt
exit 0
