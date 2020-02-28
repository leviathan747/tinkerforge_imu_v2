#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your IO-16 Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_io16 import BrickletIO16

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    io = BrickletIO16(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Set pin 0 on port A to output low
    io.set_port_configuration("a", 1 << 0, "o", False)

    # Set pin 0 and 7 on port B to output high
    io.set_port_configuration("b", (1 << 0) | (1 << 7), "o", True)

    raw_input("Press key to exit\n") # Use input() in Python 3
    ipcon.disconnect()
