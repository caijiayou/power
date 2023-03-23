from machine import UART
import struct
import time

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
