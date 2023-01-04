# Author    : Goutham Rapolu
# Date      : 09-05-2022
#
# Works with PZEM-004T V3 energy meter module.
# Connect energy meter 'Tx' & 'Rx' to A9 module 'Rx2' & 'Tx2' pins.
# 

from machine import UART
import time
import struct

uart = UART(1, 9600, tx=17, rx=16)                                            # Initialize UART port.

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
        read_all = em_read()                                    # Reads all parameters.
        voltage = read_all[0]/10.0                              
        print('Voltage = ' + str(voltage) + ' V', end=', ')
        current = ((read_all[2]<<16) |  (read_all[1]))/1000.0
        print('Current = ' + str(current) + ' A', end=', ')
        power = ((read_all[4]<<16) |  (read_all[3]))/10.0
        print('Power = ' + str(power) + 'W', end=', ')
        energy = ((read_all[6]<<16) |  (read_all[5]))/1000.0
        print('Energy = ' + str(energy) + 'kWh', end=', ')
        freq = read_all[7]/10.0
        print('Frequency = ' + str(freq) + ' Hz', end=', ')
        pf = read_all[8]/10.0
        print('Power Factor = ' + str(pf))
    except:
        
        print('error reading the PZEM-004T module')
        
    time.sleep(1)

