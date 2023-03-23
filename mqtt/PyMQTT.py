from paho.mqtt import client as mqtt_client
import json
import os
# import time

mqtt_connect = {
    'broker': 'node02.myqtthub.com',
    'port': 1883,
    'client_id': 'PC_terminal',
    'username': 'operator_pc',
    'password': '',
}
client = ''


if os.path.exists('mqtt_connect.json'):
    with open("mqtt_connect.json") as fl:
        mqtt_connect = json.load(fl)


def connect_mqtt():
    global client
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(mqtt_connect['client_id'])
    client.username_pw_set(mqtt_connect['username'], mqtt_connect['password'])
    client.on_connect = on_connect
    client.connect(mqtt_connect['broker'], mqtt_connect['port'])
    client.loop_start()


def subscribe(topic, foo):
    def on_massage(client, userdata, msg):
        print(f"Recived '{msg.payload.decode()}' from '{msg.topic}' topic")
        foo(msg.payload.decode(), msg.topic)
    for item in topic:
        client.subscribe(item)
    client.on_message = on_massage


def disconnect_mqtt():
    client.loop_stop()
    client.disconnect()
    print("Disconnected to MQTT Broker")


def publish_massage_mqtt(topic, msg):
    result = client.publish(topic, msg)
    return result[0]


if __name__ == '__main__':
    connect_mqtt()
    disconnect_mqtt()
