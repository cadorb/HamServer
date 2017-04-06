#!/usr/bin/python
from communication.MqttCom import MqttCom

if __name__ == '__main__':
    com = MqttCom()
    read = com.listen_topic()
    print(read)

    pub = com.write_topic("Coucou le monde")
    print(pub)
