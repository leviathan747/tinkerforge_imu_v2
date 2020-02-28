#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Distance IR Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_distance_ir import BrickletDistanceIR

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    dir = BrickletDistanceIR(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get current distance
    distance = dir.get_distance()
    print("Distance: " + str(distance/10.0) + " cm")

    raw_input("Press key to exit\n") # Use input() in Python 3
    ipcon.disconnect()
