from machine import Pin, I2C
from ina219 import INA219
from logging import INFO

def myina219():
    SHUNT_OHMS = 0.1

    i2c = I2C(-1, Pin(22), Pin(21))
    ina = INA219(SHUNT_OHMS, i2c, log_level=INFO)
    ina.configure()
    lst=[]
    lst.append(ina.voltage, ina.current, ina.power)
    return lst

if __name__=='__main__':
    lst = myina219()
    print(lst)