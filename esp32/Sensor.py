from machine import Pin
from machine import SoftI2C as I2C
from machine import UART
from Lib.ina219 import INA219
from logging import INFO
import traceback
import struct
import time
from Lib.ssd1306 import em_read

class sensor():
    def __init__(self):
        pass
    
    def myina219(self): #g
        SHUNT_OHMS = 0.1
        
        i2c = I2C(Pin(22), Pin(21))
        ina = INA219(SHUNT_OHMS, i2c, log_level=INFO)
        ina.configure()
        
        print("Bus Voltage: %.3f V" % ina.voltage(), end=', ')
        print("Current: %.3f mA" % ina.current(), end=', ')
        print("Power: %.3f mW" % ina.power())
        lst=[]
        lst.append(ina.voltage())
        lst.append(ina.current())
        lst.append(ina.power())
        lst.append('esp32_1_INA219')
        return lst
    
    def ssd1306(self): #l
        data=[]
        read_all = em_read()                                    # Reads all parameters.
        voltage = read_all[0]/10.0
        data.append(voltage)
        current = ((read_all[2]<<16) |  (read_all[1]))/1000.0
        data.append(current)
        power = ((read_all[4]<<16) |  (read_all[3]))/10.0
        data.append(power)
        energy = ((read_all[6]<<16) |  (read_all[5]))/1000.0
        data.append(energy)
        freq = read_all[7]/10.0
        data.append(freq)
        pf = read_all[8]/10.0
        data.append(pf)
        data.append('esp32_01_ssd1306')
        return data


if __name__=='__main__':
    while True:
        Sen=sensor()
        Ina219  = Sen.myina219()
        Ssd1306 = Sen.ssd1306()
        print('\n'*2)
        print('---'*20)
        print('Ina219: ', Ina219)
        print('ssd1306: ', Ssd1306)
        print('---'*20)
        time.sleep(0.5)

