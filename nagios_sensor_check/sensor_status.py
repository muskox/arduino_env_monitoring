#! /usr/bin/python

import datetime
import time
import MySQLdb
import sys

dbhost = 'localhost'
dbname = 'DB_NAME'
dbuser = 'DB_USER'
dbpass = 'DB_PASSWORD'

# Make sure this file is executable. You should chmod +x sensor_status.py

def main():
    
    mysql_datetime = ""
    current_temp = ""    

    conn = MySQLdb.connect (host = dbhost,
                user = dbuser,
                passwd = dbpass,
                db = dbname)
    cursor = conn.cursor ()
    sql = "select created_at, temperature from arduino_temp where created_at = (select max(created_at) from arduino_temp);"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        mysql_datetime = row[0]
        current_temp = row[1]
    cursor.close ()
    conn.commit()
    conn.close ()        
    
    timediff = datetime.datetime.now() - mysql_datetime
    
    if int(timediff.total_seconds()) < 15:
        print "Shed was %s Fahrenheit and checked only %s seconds ago" % (str(current_temp), str(timediff.total_seconds()))
        sys.exit(0)
    else:
        sys.exit(2)


if __name__ == "__main__":
    main()

