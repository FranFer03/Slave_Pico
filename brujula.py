from machine import I2C, Pin
from HMC5883L import HMC5883L
from utime import sleep_ms

# Initialize I2C communication
i2c = I2C(0, scl=Pin(17), sda=Pin(16))
sensor = HMC5883L(i2c)

while True:
    # Read the heading from the sensor
    heading = sensor.get_heading()
    
    # Print the heading to the console
    print("Heading: {:.2f} degrees".format(heading))
    
    # Wait for a short period before taking another reading
    sleep_ms(1000)
