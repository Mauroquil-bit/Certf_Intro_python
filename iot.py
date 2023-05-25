# Quiero aprender a programar para tecnología IoT.  ¿Por dónde empiezo?
import paho.mqtt.client as mqtt # pip install paho-mqtt

def on_connect(client, userdata, flags, rc):    # Función que se ejecuta cuando se conecta al broker MQTT    
    print("Connected with result code "+str(rc))   # Muestra el código de resultado de la conexión 
    client.subscribe("test")    # Se suscribe al topic "test"

def on_message(client, userdata, msg):  # Función que se ejecuta cuando llega un mensaje al topic suscrito
    print(msg.topic+" "+str(msg.payload))   # Muestra el topic y el payload del mensaje

client = mqtt.Client()  # Instancia del cliente
client.on_connect = on_connect  # Se configura la función "on_connect" que se ejecutará cuando se conecte al broker
client.on_message = on_message  # Se configura la función "on_message" que se ejecutará cuando llegue un mensaje al topic suscrito

client.connect("localhost", 1883, 60)   # Conexión al broker

client.loop_forever()   # Se mantiene a la espera de mensajes del broker

# Una verguenza COPILOT, no sabés nada de IOT
#
#

# ¿Qué es un broker MQTT?
# 
# Un broker MQTT es un servidor que se encarga de recibir los mensajes de los clientes
#  y enviarlos a los clientes suscritos a los topics correspondientes.
#  

# ¿Qué es un topic?
#
# Un topic es una cadena de texto que identifica un canal de comunicación entre un cliente y el broker.
#  Los clientes pueden suscribirse a un topic para recibir los mensajes que se envíen a ese topic.
#  Los clientes también pueden publicar mensajes en un topic para que el broker los envíe a los clientes suscritos a ese topic.
#
#  Por ejemplo, si un cliente se suscribe al topic "test", recibirá todos los mensajes que se envíen al topic "test".
#  Si un cliente publica un mensaje en el topic "test", el broker lo enviará a todos los clientes suscritos al topic "test".

# ¿Qué es un cliente MQTT?
#
# Un cliente MQTT es un programa que se conecta a un broker MQTT para enviar y recibir mensajes.
# ¿Qué es un broker?
#
# Un broker es un servidor que se encarga de recibir los mensajes de los clientes
#  y enviarlos a los clientes suscritos a los topics correspondientes.
# ¿Qué es un topic?
#
# Un topic es una cadena de texto que identifica un canal de comunicación entre un cliente y el broker.
#  Los clientes pueden suscribirse a un topic para recibir los mensajes que se envíen a ese topic.
#  Los clientes también pueden publicar mensajes en un topic para que el broker 
# los envíe a los clientes suscritos a ese topic.
#
#  Por ejemplo, si un cliente se suscribe al topic "test", 
# recibirá todos los mensajes que se envíen al topic "test".
#  Si un cliente publica un mensaje en el topic "test",
# el broker lo enviará a todos los clientes suscritos al topic "test".
# ¿Qué es un cliente MQTT?
#
# Un cliente MQTT es un programa que se conecta a un broker MQTT para enviar y recibir mensajes.
# ¿Qué es un broker?
#





