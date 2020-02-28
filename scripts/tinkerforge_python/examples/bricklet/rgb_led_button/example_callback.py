#!/usr/bin/env python
# -*- coding: utf-8 -*-

# FIXME: This example is incomplete

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your RGB LED Button Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_rgb_led_button import BrickletRGBLEDButton

# Callback function for button state changed callback
def cb_button_state_changed(state):
    print("State: " + str(state))

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    rlb = BrickletRGBLEDButton(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register button state changed callback to function cb_button_state_changed
    rlb.register_callback(rlb.CALLBACK_BUTTON_STATE_CHANGED, cb_button_state_changed)

    raw_input("Press key to exit\n") # Use input() in Python 3
    ipcon.disconnect()
