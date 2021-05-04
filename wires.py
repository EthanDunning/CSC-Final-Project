from Game import Game;
from tkinter import *;
from collections import Counter;

DEBUG = True;
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
		self.name = "Wires"
		self.Module_Done = False
		self._wires = [];
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
		# if (value in ["Orange", "Yellow", "Green", "Blue", "Purple"]):
		# 	self._wires = value;
		# else:
		# 	self._wires.append("orange");
		self._wires = value;
	@property
	def correct(self):														# the index of correct wire to cut
		return self._correct;
	@correct.setter
	def correct(self, value):
		self._correct = value;

	# other methods 

	# setup the GPIO pins 
	def gpioSetup(self):
		self.output = [True, True, True, True, True];
		self.giveOutput();

	# set the GUI for the main part of the puzzle 
	def setGUI(self):
		# clear the frame and set the grid 
		self.other.clearFrame();
		self.other.rows = 3;
		self.other.cols = 2;
		self.other.loc = "Wires";


		# button that goes to the main menu
		mainMenu = Button(self.other, bg="grey", text="Go Back.", font=("TexGyreAdventor", 25), borderwidth=10, activebackground="red", command=lambda: self.other.MainMenu());
		mainMenu.grid(row=0, column=1, sticky=N+S+E+W, padx=5, pady=5);

		# button that pauses the game
		pause = Button(self.other, bg="grey", text="Pause.", font=("TexGyreAdventor", 25), borderwidth=10, activebackground="red", command=lambda: self.other.pause());
		pause.grid(row=0, column=0, sticky=N+S+E+W, padx=5, pady=5);

		# label for the colors 
		colorsLabel = Label(self.other, bg="white", text=str(self.wires), font=("TexGyreAdventor", 28), relief="groove", borderwidth=10);
		colorsLabel.grid(row=1, column=0, sticky=N+S+E+W, padx=5, pady=5, columnspan=2);

		# label for timer
		self.other.countdown(self.other.mins, self.other.secs, 2, 0, 1);
		self.other.counter = self.other.after(1000, self.other.update_timer, 2, 0, 1);

		# label for strikes 
		self.other.health(2, 1, 1);

		# configure and pack the grid for display
		for row in range(self.other.rows):
			Grid.rowconfigure(self.other, row, weight=1);
		for col in range(self.other.cols):
			Grid.columnconfigure(self.other, col, weight=1);
		self.other.pack(fill=BOTH, expand=True);


	# pause the game so colors can be input 
	def pauseForColor(self):
		# clear the frame and setup the right size of grid
		self.other.clearFrame();
		self.other.rows = 4;
		self.other.cols = 3;

		# list of current colors in order
		colors = ["Please input wire color order."];

		# internal functions 
		# this function will append the color to the list, then update the display label
		def appendColor (c):

			# remove initial text
			try:
				if (colors[0] == "Please input wire color order." or colors[0] == "There must be 5 wires."):
					colors.pop();
			except:
				print("Initial message already deleted.");

			# delete or append the color 
			if (c == "red" and len(colors) > 0):
				colors.pop();
			elif (c != "red" and len(colors) < 5):
				colors.append(c);
			colorsLabel.configure(text=str(colors));

		# function maps the player input colors into the object properties;
		def recordColors(c):

			# check that there are 5 wires in the list 
			if (len(c) == 5):		
				self.wires = c;
				self.chooseCorrect();
			else:
				colors = ["There must be 5 wires."];
				colorsLabel.configure(text=str(colors));
			if (DEBUG):
				print(c);
				print(self.wires);
			return;

		# button that finishes the wire sequence
		done = Button(self.other, bg="green", text="Done.", font=("TexGyreAdventor", 25), borderwidth=10, activebackground="blue", command=lambda: recordColors(colors));
		done.grid(row=0, column=0, sticky=N+S+E+W, padx=5, pady=5, columnspan=2);

		# button that goes to the main menu
		mainMenu = Button(self.other, bg="grey", text="Go Back.", font=("TexGyreAdventor", 25), borderwidth=10, activebackground="red", command=lambda: self.other.MainMenu());
		mainMenu.grid(row=0, column=2, sticky=N+S+E+W, padx=5, pady=5);

		# label that shows the wire sequence
		colorsLabel = Label(self.other, bg="white", text=f"{colors}", font=("TexGyreAdventor", 28), relief="groove", borderwidth=10);
		colorsLabel.grid(row=1, column=0, sticky=N+S+E+W, padx=5, pady=5, columnspan=3);

		# list of tuples. each one contains the color name and function that adds it to the list (or removes in the case of the backspace)
		colorButtons = [("Orange", lambda: appendColor("Orange")), ("Yellow", lambda: appendColor("Yellow")), ("Green", lambda: appendColor("Green")), ("Blue", lambda: appendColor("Blue")), ("Purple", lambda: appendColor("Purple")), ("red", lambda: appendColor("red"))];



		# create the buttons in order
		count = 0;
		for row in range(2, self.other.rows):
			for col in range(self.other.cols):

				# make the delete button
				if (colorButtons[count][0] == "red"):
					key = Button(self.other, bg=colorButtons[count][0], text="f", font=("Wingdings 3", 25), relief="groove", borderwidth=10, activebackground="grey", command=colorButtons[count][1]);					
				else:
					key = Button(self.other, bg=colorButtons[count][0], text=colorButtons[count][0], font=("TexGyreAdventor", 25), relief="groove", borderwidth=10, activebackground="grey", command=colorButtons[count][1]);
				key.grid(row=row, column=col, sticky=N+S+E+W, padx=1, pady=1);

				count += 1;

		# configure and pack the grid for display
		for row in range(self.other.rows):
			Grid.rowconfigure(self.other, row, weight=1);
		Grid.columnconfigure(self.other, 0, weight=1);			# make the done button bigger than the back button
		for col in range(1, self.other.cols):
			Grid.columnconfigure(self.other, col, weight=1);
		self.other.pack(fill=BOTH, expand=True);

		



	# function picks the correct wire to pull based on the order of the wires
	def chooseCorrect(self):

		# create lists from the list of wires to determine:
		# 1. If that color is being used
		# 2. How many of that color is being used
		counts = {"Orange":0, "Yellow":0, "Green":0, "Blue":0, "Purple":0};
		for c in counts:
			if DEBUG:
				print(c);
			counts[c] = self.wires.count(c);
		falses = 0;
		for i in counts:
			if (counts[i] == 0):
				falses += 1;

		# ladder of elifs for each possiblity 
		# why the FUCK does python not have switch cases??????
		
		# If the last wire is purple and there are no yellow wires, pull the fourth wire
		if (self.wires[4] == "Purple" and counts["Yellow"] == 0):
			self.correct = 3;

		# If there is exactly one green wire, and there is more than one blue wire, pull the first wire.
		elif (counts["Green"] == 1 and counts["Blue"] > 1):
			self.correct = 0;

		# If there are no orange wires, pull the second wire
		elif (counts["Orange"] == 0):
			self.correct = 1;

		# If there are only two different colors in the set of wires, pull the last wire.
		elif (falses == 3):
			self.correct = 4;

		# If there are all different colors of wires in the set, pull the third wire.
		elif (falses == 0):
			self.correct = 2;

		# If the first and last wires are green and there are no purple wires, pull the second wire.
		elif (self.wires[0] == "Green" and self.wires[4] == "Green" and counts["Purple"] == 0):
			self.correct = 1;

		# Otherwise, pull the first wire.
		else:
			self.correct = 0;


		if DEBUG:
			print(counts);
			print(self.correct);

		self.setGUI();

	# function waits for a wire to be pulled and checks that it was correct 
	def wirePull(self):
		pass;