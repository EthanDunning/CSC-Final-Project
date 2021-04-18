from tkinter import *
import RPi.GPIO as GPIO
from time import *
from datetime import *
from random import *

# the game class contains the basic components necessary for each module
# as well as the components necessary for the non-module parts of the game like
# the timer and mistakes


class Game:

    # constructor initializes with the time (in seconds) and mistakes allotted; inputs and outputs are false/low by default
    def __init__(self, time=360, mistakes=2):
        # game difficulty settings
        self.time = time
        self.mistakes = mistakes
        # I/O lists
        self.input = [False, False, False, False, False]
        self.output = [False, False, False, False, False]

    # getters and setters
    @property
    def time(self):					# time
        return self._time
    @time.setter
    def time(self, value):
        if (value <= 0):
            value = self.time
        self._time = value

    @property
    def mistakes(self):				# mistakes
        return self._mistakes
    @mistakes.setter
    def mistakes(self, value):
        if (value <= 0):
            value = self.mistakes
        self._mistakes = value

    @property
    def input(self):				# input list
        return self._input
    @input.setter
    def input(self, value):
        self._input = value

    @property
    def output(self):				# output list
        return self._output
    @output.setter
    def output(self, value):
        self._input = value


# pins
# leds = []
# switches = []
# wires = []
# sonic_sensor = []
# test_led = []
# speaker = []

# setting up the GPIO
GPIO.setmode(GPIO.BCM)
# I/O
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(test_led, GPIO.OUT)
GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(wires, GPIO.IN)

try:
	# testing the leds
	def all_on():
		for i in leds:
			GPIO.output(leds, True)

	def all_off():
		for i in leds:
			GPIO.output(leds, False)

	def switch_test():
		for i in switches:
			if i == True:
				GPIO.output(test_led, True)

except KeyboardInterrupt:
	GPIO.cleanup()

all_on()
sleep(0.5)
all_off()
sleep(0.5)

# ultrasonic sensor
GPIO_TRIGGER = []
GPIO_ECHO = <>
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()