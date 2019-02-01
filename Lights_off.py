import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)



GPIO.setup(17,GPIO.OUT)

GPIO.setup(12, GPIO.OUT)



GPIO.output(12,GPIO.LOW)

GPIO.output(17,GPIO.LOW)

