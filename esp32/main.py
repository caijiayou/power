from Sensor import sensor
from Lib.my_mqtt import myMqtt
import time 

S    = sensor()
Mqtt = myMqtt('192.168.2.126', 'msg/info', b'msg/info')
Mqtt.wifi('ACL', '00000000')

while True:

    Ina219  = S.myina219()
    Ssd1306 = S.ssd1306()
    
    Mqtt.mqtt_pub(str(Ina219))
    Mqtt.mqtt_pub(str(Ssd1306))
    
    print('\n*2')
    print('---'*20)
    print('ina219: ', Ina219)
    print('ssd1306: ', Ssd1306)
    print('---'*20)
    time.sleep(0.5)
