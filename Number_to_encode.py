import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(12,GPIO.OUT)

GPIO.setup(17,GPIO.OUT)

bits_to_encode = 16

number_to_encode = 23

t = 0.1

d = 0.2

use_clock = True

GPIO.output(12,GPIO.LOW)

time.sleep(.5)

for bit_pos in range(bits_to_encode):

        bit = (1 << bit_pos) & number_to_encode

        if bit != 0:

                bit_value = 1

                GPIO.output(12,GPIO.LOW)

                time.sleep(t)

                GPIO.output(17,GPIO.HIGH)

                time.sleep(t)

                GPIO.output(17,GPIO.LOW)

                time.sleep(t)

        else:

                bit_value = 0

                GPIO.output(12,GPIO.HIGH)

                time.sleep(t)

                GPIO.output(17,GPIO.HIGH)

                time.sleep(t)

                GPIO.output(17,GPIO.LOW)

                time.sleep(t)

        print("Bit position {:2} is {} which is worth {:2}".format(bit_pos,bit_value,bit))

print("clock runtime = " + str(bits_to_encode * (t+d)))

use_clock = False

GPIO.output(17,GPIO.LOW)

GPIO.output(12,GPIO.LOW)



