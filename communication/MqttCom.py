#!/usr/bin/python
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import paho.mqtt.publish as publish


class MqttCom():

    def __init__(self):
        self.BROKER_IP = "192.168.1.12"
        self.BROKER_PORT = 1883
        self.TOPIC = "/iot"


    def listen_topic(self):
        msg = subscribe.simple(self.TOPIC, qos=0, msg_count=1, retained=False, hostname=self.BROKER_IP,
                               port=self.BROKER_PORT, client_id="",
                               keepalive=60, will=None, auth=None, tls=None, protocol=mqtt.MQTTv311)
        return msg.payload

    def write_topic(self, payload):
        pub = publish.single(self.TOPIC, payload=payload, qos=0, retain=False, hostname=self.BROKER_IP,
                             port=self.BROKER_PORT, client_id="",
                             keepalive=60, will=None, auth=None, tls=None, protocol=mqtt.MQTTv311, transport="tcp")
        return pub
