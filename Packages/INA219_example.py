from machine import Pin, I2C
from ina219 import INA219
from logging import INFO

SHUNT_OHMS = 0.1

i2c = I2C(-1, Pin(22), Pin(21))
ina = INA219(SHUNT_OHMS, i2c, log_level=INFO)
ina.configure()

if __name__=='__main__':
    print("Bus Voltage: %.3f V" % ina.voltage())
    print("Current: %.3f mA" % ina.current())
    print("Power: %.3f mW" % ina.power())