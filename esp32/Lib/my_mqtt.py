from umqtt.simple import MQTTClient
import machine, utime, time, network
import random

class myMqtt:
    def __init__(self, SERVER, CLIENT_ID, TOPIC):
        # SERVER = '192.168.2.126'
        # CLIENT_ID = 'msg/info' # 客户端的ID
        # TOPIC = b'msg/info' # TOPIC的ID
        self.SERVER        = SERVER
        self.CLIENT_ID     = CLIENT_ID
        self.TOPIC         = TOPIC
        self.client        = MQTTClient(CLIENT_ID, SERVER)
    
    def wifi(self, WiFi_name, WiFi_password):
        wifi= network.WLAN(network.STA_IF)
        wifi.active(True)
        wifi.connect(WiFi_name, WiFi_password)
        print('start to connect wifi')
        for i in range(20):
            print('try to connect wifi in {}s'.format(i))
            utime.sleep(1)
            if wifi.isconnected():
                break          
        if wifi.isconnected():
            print('WiFi connection OK!')
            print('Network Config=',wifi.ifconfig())
        else:
            print('WiFi connection Error')
        i=0
        
    def mqtt_pub(self, data):
        self.client.connect()
        self.client.publish(self.TOPIC, data)
        self.client.disconnect()

if __name__=='__main__':
    mqtt = myMqtt('192.168.2.126', 'msg/info', b'msg/info')
    mqtt.wifi('ACL', '00000000')
    while 1:
        try:
            for i in range(100):
                mqtt.mqtt_pub(str(random.randint(0, 100)))
                print(i)
                time.sleep(0.5)
            break
        except:
            print('404')
            pass



