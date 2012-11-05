
/*
This code is from Arduino Cookbook 2nd Edition by Michael Margolis.
http://my.safaribooksonline.com/book/hardware/arduino/9781449321185/6dot-getting-input-from-sensors/id3027173

This uses the LM35 temperature sensor.

*/


const int inputPin = 0;


void setup()
{
  Serial.begin(9600);
}

void loop()
{
  // LM35 temperature sensor input
  int value = analogRead(inputPin);
  float millivolts = (value / 1024.0) * 5000;
  float celsius = millivolts / 10; // LM35 sensor output is 10mV per degree Celsius
  // convert to fahrenheit
  float fahrenheit = (celsius * 9)/ 5 + 32;
  
  Serial.print( fahrenheit );
  Serial.println(" degrees Fahrenheit");

  delay(10000); // wait 10 seconds
}
