import RPi.GPIO as GPIO;
import time;
#import guiBase as GUI;

# set gpio mode
GPIO.setmode(GPIO.BCM);
# set gpio defaults 
inputPins = [18, 19, 20, 21, 22];
outputPins = [17, 16, 13, 12, 6];
GPIO.setup(inputPins, GPIO.IN, pull_up_down=GPIO.PUD_DOWN);
GPIO.setup(outputPins, GPIO.OUT);

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

    # other methods 

    # I/O methods that interface with the gpio

    # input from the gpio pins
    def takeInput ():
        for i in range(len(inputPins)):
            # set high pins to true
            if (GPIO.input(inputPins[i]) == True):
                self.input[i] = True;

            # set low pins to false
            else:
                self.input[i] = False;

        return;

    # output to the gpio pins
    def giveOutput(self):
        for i in range(len(outputPins)):
            GPIO.output(outputPins[i], self.output[i]);
        return;

    # clear I/O
    def clear ():
        self.input = [False, False, False, False, False];
        self.output = [False, False, False, False, False];

    # end states 

    # failure 
    def boom ():
        pass;

    # success
    def defuse ():
        pass; 


# clean pins
GPIO.cleanup();