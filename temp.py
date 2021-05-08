import paho.mqtt.client as mqtt
import time
import random

lista = []
num = 10

for n in range(num) :
    i = random.randint(1 , 10000)
    lista.append(i)
    print("Data : " +str(lista))
    if len(lista) > 3 :
        lista.pop(0)

def on_message(client, userdata, message):
    print("recieved message: ", str(message.payload.decode("utf-8")))
    print("message topic :", message.topic)
    print("qos : ", message.qos)
    print("retain flag : ", message.retain)

broker_addr = "anugrahaplikasi.com"
client = mqtt.Client("C11190018")
print("Create an MQTT Instance")
client.on_message=on_message
client.connect(broker_addr)

print("Connecting to broker")
client.loop_start()
client.subscribe("temperature")
client.publish("temperature", "Dari kevin" + str(lista))
time.sleep(5)
client.loop_stop()
