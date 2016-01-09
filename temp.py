import glob
import time
import urllib, urllib2
import os
import RPi.GPIO as GPIO



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)


base_dir = "/sys/bus/w1/devices/"
device_folder = glob.glob(base_dir + "28*")[0]
device_file = device_folder + "/w1_slave"


def read_temp_raw():
   time.sleep(5)
   f = open (device_file, 'r')
   lines = f.readlines()
   f.close()
   return lines




def read_temp():
   lines = read_temp_raw()
   while lines[0].strip()[-3:] != 'YES':
	time.sleep(0.2)
	lines = read_temp_raw()
   equals_pos = lines[1].find('t=')
   if equals_pos != -1:
	temp_string = lines[1][equals_pos+2:]
	temp_c = float(temp_string) / 1000.0
	return temp_c

temp = read_temp()


while temp < 21:

   print 'Your current Room Temprature is:' 
   print temp
   GPIO.output(18,GPIO.LOW)
   time.sleep(5)
   temp = read_temp()	



GPIO.output(18,GPIO.HIGH)
time.sleep(30)
GPIO.output(18,GPIO.LOW)
