#!/usr/bin/python

import Adafruit_DHT
import RPi_I2C_driver
from time import *
from datetime import datetime

# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
sensor = Adafruit_DHT.DHT11

# Example using a Raspberry Pi with DHT sensor
# connected to GPIO17.
pin = 17


while True:
   humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

   humi=str(humidity)
   temp=str(temperature)
   dtime=str(datetime.now().ctime())
   
   print "Temperature: "+temp
   print "Humidity RH%: "+humi
   print "LUpdate: "+dtime

   mylcd = RPi_I2C_driver.lcd()
   mylcd.lcd_clear()
   mylcd.lcd_display_string("Temprature: "+temp,1)
   mylcd.lcd_display_string("Humidity: "+humi,2)
   mylcd.lcd_display_string("Last Update: "+dtime,4)
   sleep(60)
   mylcd.lcd_clear()
