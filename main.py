import machine
import time
import dht
import gps


class SensorDHT11:
    def __init__(self, pin):
        self.sensor = dht.DHT11(pin)

    def leer_datos(self):
        try:
            self.sensor.measure()
            temperature = self.sensor.temperature()
            humidity = self.sensor.humidity()
            return temperature, humidity
        except Exception:
            return None

pin_dht = 15 
mi_sensor = SensorDHT11(pin_dht)

while True:
    data_dht = mi_sensor.leer_datos()
    if data_dht:
        temperatura, humedad = data_dht
        print(f"Temperatura: {temperatura}°C, Humedad: {humedad}%")
    else:
        print("Error al leer los datos del sensor")
    time.sleep(2)
