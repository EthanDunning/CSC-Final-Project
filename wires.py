from Game import Game;
from tkinter import *;

'''
This is the module mimicking the wires game from KTANE.
The game will pause and allow the player to input the order of colored wires on the board,
since the program has no way of knowing which colored wires have been used. 
The game resumes, and the player must "cut" (remove) the correct wire based on the 
instructions relevant to the order. 
'''

class Wires(Game):

	def __init__(self, other):
		super().__init__(None, None);

		self.wires = [];
		self.correct = 0;
		# This may seem unintuitive, but I am saving the baseGUI as a property
		# so that it can be repeatedly accessed here without having to repeatedly
		# pass it in every time a function is called from elsewhere
		self.other = other;

	# getters/setters
	@property
	def wires(self):														# order of wire colors
		return self._wires;
	@wires.setter
	def wires(self, value):
		if (value in ["orange", "yellow", "green", "blue", "purple"]):
			self._wires = value;
		else:
			self._wires = "orange";
	@property
	def correct(self):														# the index of correct wire to cut
		return self._correct;
	@correct.setter
	def correct(self, value):
		self._correct = value;

	# other methods 

	# setup the GPIO pins 
	def gpioSetup():
		self.output = [True, True, True, True, True];
		self.giveOutput();

	# set the GUI
	def setGUI():
		pass;

	# pause the game so colors can be input 
	def pauseForColor(self):
		# clear the frame and setup the right size of grid
		self.other.clearFrame();
		self.other.rows = 4;
		self.other.cols = 3;

		# button to go back to the main screen
		back = Button(self.other, bg="red", text="Go Back", font=("TexGyreAdventor", 25),
                      borderwidth=10, activebackground="blue", command=lambda: self.other.setupGUI());

		# label that shows the current order of colors
		colors = ["go", "crazy", "go", "stupid", "aaaa"]
		colorsLabel = Label(self.other, bg="white", text=f"{colors}", font=("TexGyreAdventor", 40), relief="groove", borderwidth=10);
		colorsLabel.grid(row=1, column=1, sticky=N+S+E+W, padx=5, pady=5, columnspan=3);

		self.other.pack(fill=BOTH, expand=1);


		self.recordColors();
		self.chooseCorrect();
		pass;

	# function allows the player to input the order of the colored wires on the breadboard 
	def recordColors(self):
		pass;

	# function picks the correct wire to pull based on the order of the wires
	def chooseCorrect(self):
		pass;

	# function waits for a wire to be pulled and checks that it was correct 
	def wirePull(self):
		pass;