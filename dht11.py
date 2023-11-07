import DHT

class SensorDHT11:
    def __init__(self, pin):
        self.sensor = dht.DHT11(pin)

    def read_data(self):
        try:
            self.sensor.measure()
            temperature = self.sensor.temperature()
            humidity = self.sensor.humidity()
            return temperature, humidity
        except Exception:
            return None

if __name__ == '__main__':
    pass

