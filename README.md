arduino_env_monitoring
======================

DIY Environmental Monitoring for the server room. 

It is very simple to take temperature reading from an Arduino using the LM35 sensor. 
http://my.safaribooksonline.com/book/hardware/arduino/9781449321185/6dot-getting-input-from-sensors/id3027173

This takes temperature sensor input and outputs them to the serial bus every 10 seconds. The python script is a serial
bus reader that looks for data every ten seconds and records it in a text file.

As a test I put this sensor in my shed outside, this is not climate controlled. This makes for more interesting data because 
the day to night fluctuation is more dramatic than a climate controlled server room.
