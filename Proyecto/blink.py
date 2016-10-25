#!/usr/bin/python
#import libraries
import Adafruit_BBIO.GPIO as GPIO
import time

#setup del led
led = "P8_13"

GPIO.setup(led,GPIO.OUT)

while True:
    GPIO.output(led,GPIO.HIGH)
    time.sleep (1)
    GPIO.output (led,GPIO.LOW)
    time.sleep(1)