from machine import Pin, I2C
from ina219 import INA219
from logging import INFO

def myina219():
    SHUNT_OHMS = 0.1

    i2c = I2C(-1, Pin(22), Pin(21))
    ina = INA219(SHUNT_OHMS, i2c, log_level=INFO)
    ina.configure()

    print("Bus Voltage: %.3f V" % ina.voltage(), end=', ')
    print("Current: %.3f mA" % ina.current(), end=', ')
    print("Power: %.3f mW" % ina.power())
    lst=[]
    lst.append(ina.voltage())
    lst.append(ina.current())
    lst.append(ina.power())
    return lst