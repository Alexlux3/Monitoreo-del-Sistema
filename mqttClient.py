import psutil
import paho.mqtt.client as mqtt
import time

# Configuración del cliente MQTT
broker_address = "broker.hivemq.com"  # Reemplaza con la dirección de tu servidor MQTT
port = 1883  # Puerto predeterminado para MQTT
topic = "uce/arquitectura/grupo2"

# Callback cuando el cliente se conecta al servidor
def on_connect(client, userdata, flags, rc):
    print(f"Conectado con el código de resultado: {rc}")
    client.subscribe(topic)  # Suscribirse al tema deseado

# Callback cuando un mensaje es recibido en el tema suscrito
def on_message(client, userdata, msg):
    print(f"Mensaje recibido en el tema {msg.topic}: {msg.payload.decode()}")

# Configuración del cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Conectar al servidor MQTT
client.connect(broker_address, port, 60)

# Iniciar el bucle de red
client.loop_start()

# Bandera para controlar el bucle
correr = False

# Iniciar el bucle de red
client.loop_start()

while True:
    # Obtener estadísticas de la memoria
    memoria = psutil.virtual_memory()

    # Crear un mensaje con las estadísticas
    mensaje_a_enviar = f"Memoria total: {memoria.total}, Memoria usada: {memoria.used}, Porcentaje de uso: {memoria.percent}"
    client.publish(topic, mensaje_a_enviar)

# Esperar un tiempo para recibir mensajes
time.sleep(1000000000)

# Detener el bucle y cerrar la conexión
client.loop_stop()
client.disconnect()
