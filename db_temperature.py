import paho.mqtt.client as mqtt
import random
import time
import threading

# Configuración del cliente de publicación
publish_topic = "Hola"

def temperature_generator():
    temperature = random.randint(45, 60)
    time.sleep(1)
    return temperature

def on_publish(client, userdata, mid):
    print("Dato publicado en el topic %s: %s" % (publish_topic, userdata))

def publish_thread():
    while True:
        temp = temperature_generator()
        print("Temperatura:", temp)

        client = mqtt.Client(client_id='pub', clean_session=False)
        client.on_connect = on_connect
        client.on_publish = on_publish

        client.connect(host='192.168.0.196', port=1883)
        client.loop_start()

        # Publicar el valor de temperatura en el tópico
        result = client.publish(publish_topic, temp, qos=1)

        # Esperar a que el mensaje sea publicado antes de continuar
        while not result.is_published():
            time.sleep(1)

        client.disconnect()
        time.sleep(5)

# Configuración del cliente de suscripción
subscribe_topic = "Holis"

def on_message(client, userdata, message):
    message_decode = message.payload.decode("utf-8")
    print("Mensaje recibido en el tópico %s: %s" % (message.topic,message_decode))
    print(type(message_decode))

def subscribe_thread():
    client = mqtt.Client(client_id='sub', clean_session=False)
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(host='192.168.0.196', port=1883)
    client.subscribe(subscribe_topic, qos=1)
    client.loop_start()

def on_connect(client, userdata, flags, rc):
    print('Conectado (%s)' % client._client_id)

if __name__ == '__main__':
    publish_thread = threading.Thread(target=publish_thread)
    subscribe_thread = threading.Thread(target=subscribe_thread)

    publish_thread.start()
    subscribe_thread.start()

    # Mantener el programa principal en ejecución
    while True:
        time.sleep(1)
