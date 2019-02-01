import time

import RPi.GPIO as GPIO

GPIO.setup(17, GPIO.OUT)

GPIO.setup(12, GPIO.OUT)



while True:

 GPIO.output(17, GPIO.HIGH)

 print("LED On")

 GPIO.output(12, GPIO.HIGH)

 print("LED On")



 time.sleep(1)



 GPIO.output(17, GPIO.LOW)

 print("LED Off")

 GPIO.output(12, GPIO.LOW)

 print("LED Off")

 time.sleep(1)



