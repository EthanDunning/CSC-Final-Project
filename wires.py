import Game;

'''
This is the module mimicking the wires game from KTANE.
The game will pause and allow the player to input the order of colored wires on the board,
since the program has no way of knowing which colored wires have been used. 
The game resumes, and the player must "cut" (remove) the correct wire based on the 
instructions relevant to the order. 
'''

class Wires(Game):

	def __init__(self):
		super().__init__(None, None);

		self.wires = [];
		self.correct = 0;

	# getters/setters
	@property
	def wires(self):														# order of wire colors
		return self._wires;
	@wires.setter
	def wires(self, value):
		if (value in ["orange", "yellow", "green", "blue", "purple"]):
			self.wires = value;
		else:
			self.wires = "orange";
	@property
	def correct(self):														# the index of correct wire to cut
		return self._correct;
	@correct.setter
	def correct(self, value):
		self.correct = value;

	# other methods 

	# setup the GPIO pins 
	def gpioSetup():
		self.output = [True, True, True, True, True];
		self.giveOutput();
		self.

	# set the GUI
	def setGUI():
		pass;

	# pause the game so colors can be input 
	def pause():
		self.recordColors();
		self.chooseCorrect();
		pass;

	# function allows the player to input the order of the colored wires on the breadboard 
	def recordColors():
		pass;

	# function picks the correct wire to pull based on the order of the wires
	def chooseCorrect():
		pass;

	# function waits for a wire to be pulled and checks that it was correct 
	def wirePull():
		pass;