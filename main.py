import machine
import time
import dht11

Pin_Sensor_DHT = 15

Sensor_DHT = SensorDHT11(15)


while True:
    data_dht = Sensor_DHT.read_data()
    if data_dht:
        temperatura, humedad = data_dht
        print(f"Temperatura: {temperatura}°C, Humedad: {humedad}%")
    else:
        print("Error al leer los datos del sensor")
    time.sleep(200)