from Game import Game
from tkinter import *
from collections import Counter
import RPi.GPIO as GPIO

DEBUG = True
'''
This is the module mimicking the wires game from KTANE.
The game will pause and allow the player to input the order of colored wires on the board,
since the program has no way of knowing which colored wires have been used. 
The game resumes, and the player must "cut" (remove) the correct wire based on the 
instructions relevant to the order. 
'''


class Module_Wires(Game):

    def __init__(self, other):
        super().__init__()
        self.name = "Wires"
        self.Module_Done = False
        self.Module_Started = False
        self._wires = []
        self.wires = []
        self.correct = 0
        self.inputPins = [18, 19, 20, 21, 22]
        # This may seem unintuitive, but I am saving the baseGUI as a property
        # so that it can be repeatedly accessed here without having to repeatedly
        # pass it in every time a function is called from elsewhere
        self.other = other

        # getters/setters

        @property
        # order of wire colors
        def wires(self):
            return self._wires

        @wires.setter
        def wires(self, value):
            # if (value in ["Orange", "Yellow", "Green", "Blue", "Purple"]):
            #   self._wires = value;
            # else:
            #   self._wires.append("orange");
            self._wires = value

        @property
        # the index of correct wire to cut
        def correct(self):
            return self._correct

        @correct.setter
        def correct(self, value):
            self._correct = value

        # other methods

        #self.main()

    # setup the GPIO pins
    def gpioSetup(self):
        if (DEBUG):
            print("gpioSetup()")
        self.output = [False, False, False, False, False]
        self.giveOutput()

    # set the GUI for the main part of the puzzle
    def setGUI(self):
        if (DEBUG):
            print("setGUI()")
        # clear the frame and set the grid
        self.other.clearFrame()
        self.other.rows = 3
        self.other.cols = 2
        self.other.loc = "Wires"

        # button that goes to the main menu
        mainMenu = Button(self.other, bg="grey", text="Go Back.", font=("TexGyreAdventor", 25),
                          borderwidth=10, activebackground="red", command=lambda: self.other.MainMenu())
        mainMenu.grid(row=0, column=1, sticky=N+S+E+W, padx=5, pady=5)

        # button that pauses the game
        pause = Button(self.other, bg="grey", text="Pause", font=("TexGyreAdventor", 25),
                       borderwidth=10, activebackground="red", command=lambda: self.other.pause())
        pause.grid(row=0, column=0, sticky=N+S+E+W, padx=5, pady=5)

        # label for the colors
        colorsLabel = Label(self.other, bg="white", text=str(self.wires), font=(
            "TexGyreAdventor", 28), relief="groove", borderwidth=10)
        colorsLabel.grid(row=1, column=0, sticky=N+S+E +
                         W, padx=5, pady=5, columnspan=2)

        # label for timer
        self.other.countdown(2, 0, 1)

        # label for strikes
        self.other.health(2, 1, 1)

        # configure and pack the grid for display
        for row in range(self.other.rows):
            Grid.rowconfigure(self.other, row, weight=1)
        for col in range(self.other.cols):
            Grid.columnconfigure(self.other, col, weight=1)
        self.other.pack(fill=BOTH, expand=True)

        self.wirePull()

    # pause the game so colors can be input

    def main(self, started):
        if (DEBUG):
            print("main()")
        # clear the frame and setup the right size of grid
        if (DEBUG):
            print(self.Module_Started)
        if started == False:

            self.other.clearFrame()
            self.other.rows = 4
            self.other.cols = 3

            # list of current colors in order
            colors = ["Please input wire color order."]

            # internal functions
            # this function will append the color to the list, then update the display label
            def appendColor(color):
                if (DEBUG):
                    print("appendColor()")

                # remove initial text
                try:
                    if (colors[0] == "Please input wire color order." or colors[0] == "There must be 5 wires."):
                        colors.pop()
                except:
                    if (DEBUG):
                        print("Initial message already deleted.")
                    else:
                        pass
                # delete or append the color
                if (color == "red" and len(colors) > 0):
                    colors.pop()
                elif (color != "red" and len(colors) < 5):
                    colors.append(color)
                colorsLabel.configure(text=str(colors))

            # function maps the player input colors into the object properties;
            def recordColors(c):
                if (DEBUG):
                    print("recordColors()")

                # check that there are 5 wires in the list
                if (len(c) == 5):
                    self.wires = c
                    chooseCorrect()
                else:
                    colors = ["There must be 5 wires."]
                    colorsLabel.configure(text=str(colors))

                if (DEBUG):
                    print(c)
                    print(self.wires)
                    print(f"Correct wire to pull: {self.correct}")

                return

            if (DEBUG):
                print("after record")
            # button that finishes the wire sequence
            done = Button(self.other, bg="green", text="Done.", font=("TexGyreAdventor", 25),
                          borderwidth=10, activebackground="blue", command=lambda: recordColors(colors))
            done.grid(row=0, column=0, sticky=N+S+E +
                      W, padx=5, pady=5, columnspan=2)

            # button that goes to the main menu
            mainMenu = Button(self.other, bg="grey", text="Go Back.", font=("TexGyreAdventor", 25),
                              borderwidth=10, activebackground="red", command=lambda: self.other.MainMenu())
            mainMenu.grid(row=0, column=2, sticky=N+S+E+W, padx=5, pady=5)

            # label that shows the wire sequence
            colorsLabel = Label(self.other, bg="white", text=f"{colors}", font=(
                "TexGyreAdventor", 28), relief="groove", borderwidth=10)
            colorsLabel.grid(row=1, column=0, sticky=N+S+E +
                             W, padx=5, pady=5, columnspan=3)

            # list of tuples. each one contains the color name and function that adds it to the list (or removes in the case of the backspace)
            colorButtons = [("Orange", lambda: appendColor("Orange")), ("Yellow", lambda: appendColor("Yellow")), ("Green", lambda: appendColor(
                "Green")), ("Blue", lambda: appendColor("Blue")), ("Purple", lambda: appendColor("Purple")), ("red", lambda: appendColor("red"))]

            # create the buttons in order
            count = 0
            for row in range(2, self.other.rows):
                for col in range(self.other.cols):

                    # make the delete button
                    if (colorButtons[count][0] == "red"):
                        key = Button(self.other, bg=colorButtons[count][0], text="f", font=(
                            "Wingdings 3", 25), relief="groove", borderwidth=10, activebackground="grey", command=colorButtons[count][1])
                    else:
                        key = Button(self.other, bg=colorButtons[count][0], text=colorButtons[count][0], font=(
                            "TexGyreAdventor", 25), relief="groove", borderwidth=10, activebackground="grey", command=colorButtons[count][1])
                    key.grid(row=row, column=col,
                             sticky=N+S+E+W, padx=1, pady=1)

                    count += 1

            # configure and pack the grid for display
            for row in range(self.other.rows):
                Grid.rowconfigure(self.other, row, weight=1)
            # make the done button bigger than the back button
            Grid.columnconfigure(self.other, 0, weight=1)
            for col in range(1, self.other.cols):
                Grid.columnconfigure(self.other, col, weight=1)
            self.other.pack(fill=BOTH, expand=True)

        else:
            if (DEBUG):
                print("Pass")
            self.setGUI()

        # function picks the correct wire to pull based on the order of the wires
        def chooseCorrect():
            if (DEBUG):
                print("chooseCorrect()")

            # create lists from the list of wires to determine:
            # 1. If that color is being used
            # 2. How many of that color is being used
            counts = {"Orange": 0, "Yellow": 0,
                      "Green": 0, "Blue": 0, "Purple": 0}
            for c in counts:
                if DEBUG:
                    print(c)
                counts[c] = self.wires.count(c)
            falses = 0
            for i in counts:
                if (counts[i] == 0):
                    falses += 1

            # ladder of elifs for each possiblity
            # why the FUCK does python not have switch cases??????

            # If the last wire is purple and there are no yellow wires, pull the fourth wire
            if (self.wires[-1] == "Purple" and counts["Yellow"] == 0):
                self.correct = 3

            # If there is exactly one green wire, and there is more than one blue wire, pull the first wire.
            elif (counts["Green"] == 1 and counts["Blue"] > 1):
                self.correct = 0

            # If there are no orange wires, pull the second wire
            elif (counts["Orange"] == 0):
                self.correct = 1

            # If there are only two different colors in the set of wires, pull the last wire.
            elif (falses == 3):
                self.correct = 4

            # If there are all different colors of wires in the set, pull the third wire.
            elif (falses == 0):
                self.correct = 2

            # If the first and last wires are green and there are no purple wires, pull the second wire.
            elif (self.wires[0] == "Green" and self.wires[4] == "Green" and counts["Purple"] == 0):
                self.correct = 1

            # Otherwise, pull the first wire.
            else:
                self.correct = 0

            if DEBUG:
                print(counts)
                print("Wire to pull:")
                print(self.correct)

            self.setGUI()

    # function waits for a wire to be pulled and checks that it was correct

    def wirePull(self):
        if (DEBUG):
            print("wirePull()")
        self.connections = self.inputPins

        # detect a pulled line
        GPIO.setmode(GPIO.BCM)
        # for i in range(len(self.inputPins)):
        #     print(i)
        #     if (DEBUG):
        #         print(f"{self.connections[i]} set as {i}")
        #     # dont want to double-call a previously incorrectly pulled wire
        #     GPIO.setup(self.connections[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        #     GPIO.add_event_detect( self.connections[i], GPIO.FALLING, callback=lambda *a: self.check(i), bouncetime=1000)

        try:
            GPIO.setup(self.connections[0], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            GPIO.add_event_detect( self.connections[0], GPIO.FALLING, callback=lambda *a: self.check(0), bouncetime=1000)
        except:
            pass

        try:
            GPIO.setup(self.connections[1], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            GPIO.add_event_detect( self.connections[1], GPIO.FALLING, callback=lambda *a: self.check(1), bouncetime=1000)
        except:
            pass

        try:
            GPIO.setup(self.connections[2], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            GPIO.add_event_detect( self.connections[2], GPIO.FALLING, callback=lambda *a: self.check(2), bouncetime=1000)
        except:
            pass

        try:
            GPIO.setup(self.connections[3], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            GPIO.add_event_detect( self.connections[3], GPIO.FALLING, callback=lambda *a: self.check(3), bouncetime=1000)
        except:
            pass

        try:
            GPIO.setup(self.connections[4], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            GPIO.add_event_detect( self.connections[4], GPIO.FALLING, callback=lambda *a: self.check(4), bouncetime=1000)
        except:
            pass

    # check if the correct pin was pulled

    def check(self, index):
        # print(GPIO.input(20))
        # print("check()")

        # check that the pin is not previously incorrectly pulled
        if (DEBUG):
            print(index)
            print(self.connections[index])
        if (self.connections[index] != "checked"):
            GPIO.remove_event_detect(self.connections[index])
            if (DEBUG):
                print("processing")
                print("index :", str(self.correct))
            # check that the pull is correct
            if (index == self.correct):
                if (DEBUG):
                    print(index)
                self.Module_Done = True
                self.other.MainMenu()
            else:
                if (DEBUG):
                    print(index)
                    print("Wrong!")
                self.other.strike()
                self.connections[index] = "checked"

        # print("done")
