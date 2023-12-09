import DHT

sensor = dht.DHT11(pin)
temperature = self.sensor.temperature()
humidity = self.sensor.humidity()
return temperature, humidity

if __name__ == '__main__':
    temperature,humidity = 