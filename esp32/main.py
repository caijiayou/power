from machine import UART
import time
import struct
import py_mqtt as mq
import oled as OLed
from INA219_example import myina219

uart = UART(1, 9600, tx=17, rx=16)                                            # Initialize UART port.
mq.wifi_init()

def G_read():
    Generator = myina219()
    return Generator

def em_read():
    signed=True
    uart.write(b'\xF8\x04\x00\x00\x00\x0A\x64\x64')             # Request for all parameters from the EM module.
    time.sleep(0.1)
    recv_data = uart.read()
    recv_data = recv_data[3:-2]
    data_length = int(len(recv_data) / 2)
    data_f = '>' + (('h' if signed else 'H') * data_length)
    return struct.unpack(data_f, recv_data)

def reset_energy():                                             # Resets 'kWh' data.
    uart.write(b'\xF8\x42\xC2\x41')                             

while True:
    try:
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
        print('Voltage: %sV, Current: %sA, Power: %sW, Energy: %skWh, Frequency: %sHz, pf: %s' %(voltage, current, power, energy, freq, pf))
        #OLed.oLed(data)
        data.append('esp32_01')
        mq.mqtt_pub(str(data))
        
        Generator = myina219()
        print(Generator)
        # mq.mqtt_pub(str(Generator))
        
        time.sleep(0.5)
    except:
        print('Error')
        pass


