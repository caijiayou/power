from umqtt.simple import MQTTClient
import machine,utime,time,network

SERVER = '192.168.2.126'
CLIENT_ID = 'msg/info' # 客户端的ID
TOPIC = b'msg/info' # TOPIC的ID
client = MQTTClient(CLIENT_ID, SERVER)
    
def wifi_init():
    wifi= network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect('ACL', '00000000')
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
def mqtt_pub(data):
    client.connect()
    client.publish(TOPIC, data)

if __name__=='__main__':
    wifi_init()
    mqtt_pub('jkasdflk;sajfgklasdjfk')
