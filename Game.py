print("This is the start to the new project.");


import RPi.GPIO as GPIO;
import time;

# the game class contains the basic components necessary for each module 
# as well as the components necessary for the non-module parts of the game like 
# the timer and mistakes 
class Game:

	# constructor initializes with the time (in seconds) and mistakes allotted; inputs and outputs are false/low by default
	def __init__(self, time=360, mistakes=2):
		# game difficulty settings
		self.time = time;
		self.mistakes = mistakes;
		# I/O lists
		self.input = [False, False, False, False, False];
		self.output = [False, False, False, False, False];

	# getters and setters 
	@property
	def time(self):					# time
		return self._time;
	@time.setter
	def time(self, value):
		if (value <= 0):
			value = self.time;
		self._time = value;
	@property
	def mistakes(self):				# mistakes
		return self._mistakes;		
	@mistakes.setter
	def mistakes(self, value):
		if (value <= 0):
			value = self.mistakes;
		self._mistakes = value;
	@property
	def input(self):				# input list
		return self._input;
	@input.setter
	def input(self, value):
		self._input = value;
		
	

