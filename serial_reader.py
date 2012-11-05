import serial
import time
import datetime

ser = serial.Serial('/dev/ttyACM0',9600,timeout=1) // On Ubuntu systems, /dev/ttyACM0 is the default path to the serial device on Arduinos, yours is likely different.
while 1:
    time.sleep(10)

    the_goods = ser.readline()

    f = open('/home/spustay/sensor_data.txt','a') // put your path here
    f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' ' + the_goods)
    f.close()

    print the_goods 
