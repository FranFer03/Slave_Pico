from machine import Pin, SoftI2C
from time import sleep

import bmp180

i2c = SoftI2C(sda=Pin(16), scl=Pin(17), freq=100000)
handle_i2c=bmp180.BMP180(i2c)

while True:
    temp=handle_i2c.temperature
    press=handle_i2c.pressure
    alt=handle_i2c.altitude
    print("T=%.2f" %temp, " ", "P=%.2f" %(press/100), " ", "Alt=%.2f" %alt, " ", end="\r")
    sleep(1)
