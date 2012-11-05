arduino_env_monitoring
======================

DIY Environmental Monitoring for the server room. 

It is very simple to take temperature reading from an Arduino using the LM35 sensor. 
http://my.safaribooksonline.com/book/hardware/arduino/9781449321185/6dot-getting-input-from-sensors/id3027173

This takes temperature sensor input and outputs them to the serial bus every 10 seconds. The python script is a serial
bus reader that looks for data every ten seconds and records it in a text file.

As a test I put this sensor in my shed outside, this is not climate controlled. This makes for more interesting data because 
the day to night fluctuation is more dramatic than a climate controlled server room.

The first few reads from the serial line can be a little funky. I truncated the first 5 reading of the sensor_data.txt file
because those had a few extra characters. I set the update time to 10 seconds both on the create side (the Arduino code)
and the python serial read time. There could exist weird conditions where you get only partial data on the read so
this could be more thoroughly engineered. This data file spans the daylight savings time change so system datatimes should
have a weird blip when that happened.
