from machine import Pin
from machine import UART

def main():
    com = UART(2, 9600, tx=17, rx=16)
    com.init(9600)

    led = Pin(5, Pin.OUT, value=1)  # 設定LED接腳
    print('MicroPython Ready...')  # 輸出訊息到終端機

    while True:
        choice = com.readline()
        if choice != None:
            print('choice: ', choice)

if __name__ == '__main__':
    main()