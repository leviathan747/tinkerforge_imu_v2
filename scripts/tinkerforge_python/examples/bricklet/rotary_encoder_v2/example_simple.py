#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Rotary Encoder Bricklet 2.0

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_rotary_encoder_v2 import BrickletRotaryEncoderV2

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    re = BrickletRotaryEncoderV2(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get current count without reset
    count = re.get_count(False)
    print("Count: " + str(count))

    raw_input("Press key to exit\n") # Use input() in Python 3
    ipcon.disconnect()
