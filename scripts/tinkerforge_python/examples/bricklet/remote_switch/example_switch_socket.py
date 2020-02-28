#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Remote Switch Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_remote_switch import BrickletRemoteSwitch

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    rs = BrickletRemoteSwitch(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Switch on a type A socket with house code 17 and receiver code 1.
    # House code 17 is 10001 in binary (least-significant bit first)
    # and means that the DIP switches 1 and 5 are on and 2-4 are off.
    # Receiver code 1 is 10000 in binary (least-significant bit first)
    # and means that the DIP switch A is on and B-E are off.
    rs.switch_socket_a(17, 1, rs.SWITCH_TO_ON)

    raw_input("Press key to exit\n") # Use input() in Python 3
    ipcon.disconnect()
