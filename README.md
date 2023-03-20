<font color=#00FFFF>**將esp32資料夾內code燒入晶片中執行main.py檔即可**</font>
>|--main.py              #主程式   
>|--oled.py              #oled副程式沒用到刪除即可   
>|--py_mqtt.py           #mptt副程式   
>|--ssd1306.py           #oled_I2C介面副程式   
>|--INA219_example.py    #電源檢測(發電機)模組程式  
>|--ina219.py            #電源檢測(發電機)模組I2C介面副程式  

<font color=#00FFFF>**RPi資料夾內code為模擬mqtt發收.py檔**</font>
>|--Publisher.py     #mqtt發佈端.py   
>|--Subscriber.py    #mqtt訂閱端.py   

<font color=#FFFF00>**Packages內code為單功能測試檔**</font>
>|--mqtt.py   
>|--serial.py   
>|--uarl.py   
>|--INA219_example.py  
>|--ina219.py