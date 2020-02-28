#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Analog In Bricklet 2.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_analog_in_v2 import BrickletAnalogInV2

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    ai = BrickletAnalogInV2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get current voltage
    voltage = ai.get_voltage()
    print("Voltage: " + str(voltage/1000.0) + " V")

    raw_input("Press key to exit\n") # Use input() in Python 3
    ipcon.disconnect()
