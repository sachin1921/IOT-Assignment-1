# IOT-Assignment-1

## Team Members

| Name        | Student ID           | 
| ------------- |:-------------:| 
| Sachin Teckchandani     | 100620287|
| Zeerak Siddiqui      | 100554495      |
| Yin Zhou  |    100314426    |

## Task 1
We implemented the MQTT protocol that uses publish/subscribe operations allowing users to exchange data between clients and the server.
Communication with the Pi was not that tough. However, in order for us to be able to use python scripts we installed a library paho-mqtt. We created a broker.py script that is run from within the rpi and connects to the sensor tag’s BLE address. This publishes all sensor data from the sensor tags.

Below are the screenshots taken of the results that are displayed when the client has requested statistics as well as the broker: 
















