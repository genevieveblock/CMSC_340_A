import time

import RPi.GPIO as GPIO

def my_callback(channel):

if GPIO.input(channel):

     print("Channel {} is high".format(channel))

else:

     print("Channel {} is low".format(channel))

# Set pin 12 up for input

GPIO.setmode(GPIO.BCM)

GPIO.setup(12, GPIO.IN)


GPIO.add_event_detect(12, GPIO.BOTH, callback=my_callback)

