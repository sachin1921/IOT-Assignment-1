# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 23:04:40 2019

@author: yinz
"""

import paho.mqtt.client as mqtt
import time

subscribes = input("Enter subscriber\noptions are \"temp\",\"accelerometer\",\"humidity\",\"barometer\",\"magnetometer\",\"gyroscope\",\"all\"\n")

sleeptime = int( input ("Enter display time\n"))


def on_connect(client, userdata, flags, rc):
    client.subscribe(subscribes)

             
def on_message(client, userdata, msg):
    print (msg.topic + " " + str(msg.payload))
    time.sleep(sleeptime)
    
def on_unsubscribe(client, userdata, mid):
    client.unsubscribe(subscribes)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org",1883,60)

client.loop_forever()
