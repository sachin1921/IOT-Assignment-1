# -*- coding: utf-8 -*-
import time
import json
from bluepy import sensortag as sensortag
import paho.mqtt.publish as mqtt



my_sensor = 'F0:F8:F2:86:32:81'
tag = sensortag.SensorTag(my_sensor)

print ("Connected to SensorTag", my_sensor)




base_topic = "all"

while True:

    tag.IRtemperature.enable()
    tag.humidity.enable()
    tag.barometer.enable()
    tag.accelerometer.enable()
    tag.magnetometer.enable()
    tag.gyroscope.enable()

    msgs = []

    ambient_temp, target_temp = tag.IRtemperature.read()
    acc_x,acc_y,acc_z = tag.accelerometer.read()
    ambient_temp, rel_humidity = tag.humidity.read()
    ambient_temp, pressure_millibars = tag.barometer.read()
    mag_x,mag_y,mag_z = tag.magnetometer.read()
    gyr_x,gyr_y,gry_z = tag.gyroscope.read()
    
    sensorType = ["temp","accelerometer","humidity","barometer","magnetometer","gyroscope"]

    tempData = {'ambient_temp':ambient_temp}
    accelerometerData = { 'accelerometer':"x="+ str (acc_x)+" y="+ str(acc_y)+" z="+str(acc_z)}
    humidityData = { 'humidity':rel_humidity}
    pressureData = {    'millibars': pressure_millibars}
    magnetometerData = { 'magnetometer': "x="+ str (mag_x)+" y="+ str(mag_y)+" z="+str(mag_z)}
    gyroscopeData = { 'gyroscope': "x="+ str (gyr_x)+" y="+ str(gyr_y)+" z="+str(gry_z)}

    data = {
        'ambient_temp'  : ambient_temp,
        'accelerometer' : "x="+ str (acc_x)+" y="+ str(acc_y)+" z="+str(acc_z),
        'humidity'      : rel_humidity,
        'millibars'     : pressure_millibars,
        'magnetometer'  : "x="+ str (mag_x)+" y="+ str(mag_y)+" z="+str(mag_z),
        'gyroscope'     : "x="+ str (gyr_x)+" y="+ str(gyr_y)+" z="+str(gry_z)

    }

    tempDataPayload = json.dumps(tempData)
    accelerometerDataPayload = json.dumps(accelerometerData)
    humidityDataPayload = json.dumps(humidityData)
    pressureDataPayload = json.dumps(pressureData)
    magnetometerDataPayload = json.dumps(magnetometerData)
    gyroscopeDataPayload = json.dumps(gyroscopeData)
    
    payload = json.dumps(data)
    print ("Server Side\n")
    print (payload)
    msgs.append((base_topic, payload, 0, False))
    for k in data:
        msgs.append( ( "%s/%s" % (base_topic, k), data[k], 0, False ) )
        
    mqtt.multiple(msgs, hostname='test.mosquitto.org', port=1883)

    time.sleep(1)

    
    payloads = [tempDataPayload,accelerometerDataPayload,humidityDataPayload,pressureDataPayload,magnetometerDataPayload,gyroscopeDataPayload]
    for i in range(len(sensorType)):
        msgs = []
        msgs.append((sensorType[i], payloads[i], 0, False))
        mqtt.multiple(msgs, hostname='test.mosquitto.org', port=1883)




tag.disconnect()