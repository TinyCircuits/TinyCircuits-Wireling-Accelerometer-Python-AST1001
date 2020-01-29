# BMA250 Example
# Reads all sensor data from accelerometer (X, Y, Z, Temp) and prints
# Written by: Laverena Wienclaw for TinyCircuits

import tinycircuits_wireling
import tinycircuits_bma250
import time

# Enable power to pi hat and wirelings
wireling = tinycircuits_wireling.Wireling()
wireling.selectPort(0) # Select port (0-3) labeled on the Pi Hat

# Sensor init: See tinycircuits_bma250 for reg definition descriptions
bma250 = tinycircuits_bma250.BMA250(0x03, 0x08)

while True:
    bma250.readSensor()
    print("X: %0.1d" % bma250.X)
    print("Y: %0.1d" % bma250.Y)
    print("Z: %0.1d" % bma250.Z)
    print("Temp: %0.1f" % bma250.Temp)
    time.sleep(2)