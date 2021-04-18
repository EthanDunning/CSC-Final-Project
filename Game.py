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
    def __init__(self, time=360, mistakes=3):
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
leds = []
switches = []
wires = []
sonic_sensor = []
test_led = []
speaker = []

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