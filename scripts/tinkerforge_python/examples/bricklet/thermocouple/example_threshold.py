#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "XYZ" # Change XYZ to the UID of your Thermocouple Bricklet

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_thermocouple import BrickletThermocouple

# Callback function for temperature reached callback
def cb_temperature_reached(temperature):
    print("Temperature: " + str(temperature/100.0) + " °C")

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    t = BrickletThermocouple(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Get threshold callbacks with a debounce time of 10 seconds (10000ms)
    t.set_debounce_period(10000)

    # Register temperature reached callback to function cb_temperature_reached
    t.register_callback(t.CALLBACK_TEMPERATURE_REACHED, cb_temperature_reached)

    # Configure threshold for temperature "greater than 30 °C"
    t.set_temperature_callback_threshold(">", 30*100, 0)

    raw_input("Press key to exit\n") # Use input() in Python 3
    ipcon.disconnect()
