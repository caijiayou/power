import upip
from Lib.my_mqtt import myMqtt

if __name__=='__main__':
    mqtt = myMqtt(None, None, None)
    mqtt.wifi('ACL', '00000000')
    upip.install('micropython-umqtt.simple')
    upip.install('logging')
    upip.install('traceback')
    print('End')