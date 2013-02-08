import serial
import time
import MySQLdb

dbhost = 'localhost'
dbname = 'DB_NAME'
dbuser = 'DB_USERNAME'
dbpass = 'DB_PASSWORD'

ser = serial.Serial('/dev/ttyACM0',9600,timeout=1) # On Ubuntu systems, /dev/ttyACM0 is the default path to the serial device on Arduinos, yours is likely different.
while 1:
    time.sleep(10)

    the_goods = ser.readline()
    str_parts = the_goods.split(' ')

    conn = MySQLdb.connect (host = dbhost,
                    user = dbuser,
                    passwd = dbpass,
                    db = dbname)
    cursor = conn.cursor ()
    sql = "INSERT arduino_temp (temperature) VALUES ('%s');" % (str_parts[0])
    try:
        cursor.execute(sql)
    except:
        pass
    cursor.close ()
    conn.commit()
    conn.close ()        

    print the_goods 
