# Complete project details at https://RandomNerdTutorials.com

from machine import Pin, SoftI2C
import ssd1306
from time import sleep

# ESP32 Pin assignment 
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

def oLed(data):
    
    '''input list=[Voltage, Current, Power, Energy, Frequency, pf]'''
    oled.fill(0)
    Voltage    = 'Voltage: '   + str(data[0]) + ' V'
    Current    = 'Current: '   + str(data[1]) + ' A'
    Power      = 'Power: '     + str(data[2]) + ' W'
    Energy     = 'Energy: '    + str(data[3]) + ' kWh'
    Frequency  = 'Frequency: ' + str(data[4]) + ' Hz'
    pf         = 'pf: '        + str(data[5]) + ' '
    oled.text(Voltage, 0, 5)
    oled.text(Current, 0, 17)
    oled.text(Power, 0, 25)
    oled.text(Energy, 0, 35)
    oled.text(Frequency, 0, 45)
    oled.text(pf, 0, 55)
    oled.show()

if __name__=='__main__':
    data=[111, 0.1, 13, 0.0, 60, 0.0]
    oLed(data) 
    data=[220, 0.1, 13, 0.0, 60, 0.0]
    oLed(data)
