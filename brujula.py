from machine import I2C
from HMC5883L import HMC5883L

i2c = I2C(1, sda=pin(2), scl=pin(3), freq=100000)
compass = HMC5883L(i2c)

while True:
    h = compass.get_heading()
    print("Orientación con respecto al norte:", h)