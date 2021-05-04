from Game import Game;
from tkinter import *;

'''
This is the module mimicking the wires game from KTANE.
The game will pause and allow the player to input the order of colored wires on the board,
since the program has no way of knowing which colored wires have been used. 
The game resumes, and the player must "cut" (remove) the correct wire based on the 
instructions relevant to the order. 
'''

class Module_Wires(Game):

	def __init__(self, other):
		super().__init__();
		self.name = "Wires"
		self.Module_Done = False
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

		# list of current colors in order
		colors = [];

		# button that finishes the wire sequence
		done = Button(self.other, bg="green", text="Done.", font=("TexGyreAdventor", 25), borderwidth=10, activebackground="blue", command=lambda: self.recordColors());
		done.grid(row=0, column=0, sticky=N+S+E+W, padx=5, pady=5, columnspan=2);

		# button that goes to the main menu
		mainMenu = Button(self.other, bg="grey", text="Go Back.", font=("TexGyreAdventor", 25), borderwidth=10, activebackground="red", command=lambda: self.other.MainMenu());
		mainMenu.grid(row=0, column=2, sticky=N+S+E+W, padx=5, pady=5);

		# label that shows the wire sequence
		colorsLabel = Label(self.other, bg="white", text=f"{colors}", font=("TexGyreAdventor", 28), relief="groove", borderwidth=10);
		colorsLabel.grid(row=1, column=0, sticky=N+S+E+W, padx=5, pady=5, columnspan=3);

		# list of tuples. each one contains the color name and function that adds it to the list (or removes in the case of the backspace)
		colorButtons = [("orange", lambda: appendColor("Orange")), ("yellow", lambda: appendColor("Yellow")), ("green", lambda: appendColor("Green")), ("blue", lambda: appendColor("Blue")), ("purple", lambda: appendColor("Purple")), ("red", lambda: appendColor("red"))];

		# this function will append the color to the list, then update the display label
		def appendColor (c):
			if (c == "red" and len(colors) > 0):
				colors.pop();
			elif (c != "red" and len(colors) < 5):
				colors.append(c);
			colorsLabel.configure(text=str(colors));

		# create the buttons in order
		count = 0;
		for row in range(2, self.other.rows):
			for col in range(self.other.cols):

				key = Button(self.other, bg=colorButtons[count][0], text=colorButtons[count][0], font=("TexGyreAdventor", 25), relief="groove", borderwidth=10, activebackground="grey", command=colorButtons[count][1]);
				key.grid(row=row, column=col, sticky=N+S+E+W, padx=1, pady=1);

				count += 1;

		# configure and pack the grid for display
		for row in range(self.other.rows):
			Grid.rowconfigure(self.other, row, weight=1);
		Grid.columnconfigure(self.other, 0, weight=4);			# make the done button bigger than the back button
		for col in range(1, self.other.cols):
			Grid.columnconfigure(self.other, col, weight=1);
		self.other.pack(fill=BOTH, expand=True);

		self.chooseCorrect();

	# function allows the player to input the order of the colored wires on the breadboard 
	def recordColors(self):
		pass;

	# function picks the correct wire to pull based on the order of the wires
	def chooseCorrect(self):
		pass;

	# function waits for a wire to be pulled and checks that it was correct 
	def wirePull(self):
		pass;