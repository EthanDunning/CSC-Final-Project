
#A. 
#  Morse Code
# A light will begin flashing
# The players must decipher the four character word
# The defuser will hold their hand a certain distance away from the
# sonic sensor depending on the word
# If the hand is held at the correct distance for 2 seconds,
# the module is complete
# If the hand is at the incorrect distance for 2 seconds,
# a strike is counted
# There will be a maximum distance allowed

#B. 
# A short flash represents a dot
# A long flash represents a dash
# There is a long gap between letters
# There is a very long gap before the word repeats

from time import sleep
import RPi.GPIO as GPIO
import random
from Game import *
##from guiBase import *
from tkinter import *
##from lights import *

class Module_Morse_Code(Game):
    def __init__(self, other, lights):
        super().__init__()
        self.other = other
        self.Module_Started = False
        self.Module_Done = False
        self.word = False
        self.TrueFreq = False
        self.lights = lights
        self.name = 'Morse Code'
        self.other.loc = 'Morse Code'
        self.freq = 0
        self.main(self.Module_Started)

    # gui build
    def main(self, started):
        print('started')
        self.other.clearFrame()
        self.other.rows = 4
        self.other.cols = 1
        print('check 1')
        self.other.pause_button(0, 0, 2)
        self.other.back_button(0, 2, 2)
        self.other.countdown(1, 0, 1)
        self.other.location(1, 1, 1)
        self.other.health(1, 2, 1)
        self.other.Modules_completed = 0
        for module in self.other.Modules_Done:
            self.other.Modules_completed += 1

        print(self.other.Modules_completed)
##         # setting up the GPIO
##        GPIO.setmode(GPIO.BCM)
##         # I/O
##        GPIO.setup(leds, GPIO.OUT)
##         # GPIO.setup(test_led, GPIO.OUT)
##        GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
##        #GPIO.setup(wires, GPIO.IN, pull_up_down=GPIO.PUD_UP)
##         # GPIO.setup(wires, GPIO.IN)

        if started == False:
            self.other.Module_Started = True
            button_colors = ["red", "green", "blue"]
            button_labels = ["+", "-", self.freq, "OK"]
        
        # up button
        up = Button(self.other, bg='green', text='Up', font=('TexGyreAdventor', 45), borderwidth=10, relief='raised', command = lambda: self.Button_Press('up'))
        up.grid(row=2, column=0, sticky=N+S+E+W, padx=0, pady=0, columnspan=1)

        # down button
        down = Button(self.other, bg='red', text='Down', font=('TexGyreAdventor', 45), borderwidth=10, relief='raised', command = lambda: self.Button_Press('down'))
        down.grid(row=2, column=2, sticky=N+S+E+W, padx=0, pady=0, columnspan=1)

        # frequency counter
        freq = Label(self.other, bg='blue', text=self.freq, font=('TexGyreAdventor', 45), borderwidth=10, relief='raised')
        freq.grid(row=2, column=1, sticky=N+S+E+W, padx=0, pady=0, columnspan=1)

        # Check Button
        check = Button(self.other, bg='orange', text='Check', font=('TexGyreAdventor', 45), borderwidth=10, relief='raised', command = lambda: self.Button_Press('check'))
        check.grid(row=3, column=1, sticky=N+S+E+W, padx=0, pady=0, columnspan=1)
##        for row in range(0, self.other.rows):
##            Grid.rowconfigure(self.other, row, weight=2)
##        Grid.rowconfigure(self.other, 2, weight=5)
##
        for col in range(self.other.cols):
            Grid.columnconfigure(self.other, col, weight=5)
        #self.setup()
        self.other.pack(fill=BOTH, expand=True)
        #self.game_start()
##
##    def setup(self):
##         # setting up the GPIO
##        GPIO.setmode(GPIO.BCM)
##         # I/O
##        GPIO.setup(leds, GPIO.OUT)
##         # GPIO.setup(test_led, GPIO.OUT)
##        GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
##        #GPIO.setup(wires, GPIO.IN, pull_up_down=GPIO.PUD_UP)
##         # GPIO.setup(wires, GPIO.IN)
##        return

    def Button_Press(self, Button):
        if Button == 'up':
            self.freq += 1
            print(self.freq)
            freq = Label(self.other, bg='blue', text=self.freq, font=('TexGyreAdventor', 45), borderwidth=10, relief='raised')
            freq.grid(row=2, column=1, sticky=N+S+E+W, padx=0, pady=0, columnspan=1)
            return self.freq
        elif Button == 'down':
            self.freq -= 1
            print(self.freq)
            freq = Label(self.other, bg='blue', text=self.freq, font=('TexGyreAdventor', 45), borderwidth=10, relief='raised')
            freq.grid(row=2, column=1, sticky=N+S+E+W, padx=0, pady=0, columnspan=1)
            return self.freq
        elif Button == 'check':
            if self.freq == self.TrueFreq:
                self.Module_Complete = True
            else:
                self.other.strike
        

    # picks a random word from the list
    def word_select(self):
        words = ['fall', 'your', 'slid', 'bomb', 'left']
        freqs = [4, 13, 0, 6, 3]
        x = random.randint(0, 4)
        word = words[x]
        freq = freqs[x]
        return word, freq

    @property
    def word(self):
        return self._word
    @word.setter
    def word(self, value):
        self._word = value

    @property
    def TrueFreq(self):
        return self._TrueFreq

    @TrueFreq.setter
    def TrueFreq(self, value):
        self._TrueFreq = value

    # dot function
    def dot(self, light):
##        GPIO.output(leds[light], GPIO.HIGH)
##        sleep(0.25)
##        GPIO.output(leds[light], GPIO.LOW)
##        sleep(0.25)
        pass
    # dash function
    def dash(self, light):
##        GPIO.output(leds[light], GPIO.HIGH)
##        sleep(0.75)
##        GPIO.output(leds[light], GPIO.LOW)
##        sleep(1)
        pass


    def game_start(self):
        self.word, self.TrueFreq = self.word_select()
        while self.Module_Done == False:
            if self.word == 'fall':
                # F
                self.dot(0)
                self.dot(0)
                self.dash(0)
                self.dot(0)
                sleep(1)
                # A
                self.dot(1)
                self.dash(1)
                sleep(1)
                # L
                self.dot(2)
                self.dash(2)
                self.dot(2)
                self.dot(2)
                sleep(1)
                # L
                self.dot(3)
                self.dash(3)
                self.dot(3)
                self.dot(3)
                sleep(1)
            
            if self.word == 'your':
                # Y
                self.dash(0)
                self.dot(0)
                self.dash(0)
                self.dash(0)
                sleep(1)
                # O
                self.dash(1)
                self.dash(1)
                self.dash(1)
                sleep(1)
                # U
                self.dot(2)
                self.dot(2)
                self.dash(2)
                sleep(1)
                # R
                self.dot(3)
                self.dash(3)
                self.dot(3)
                sleep(1)

            if self.word == 'slid':
                # S
                self.dot(0)
                self.dot(0)
                self.dot(0)
                sleep(1)
                # L
                self.dot(1)
                self.dash(1)
                self.dot(1)
                self.dot(1)
                sleep(1)
                # I
                self.dot(2)
                self.dot(2)
                sleep(1)
                # D
                self.dash(3)
                self.dot(3)
                self.dot(3)
                sleep(1)
            
            if self.word == 'bomb':
                # B
                self.dash(0)
                self.dot(0)
                self.dot(0)
                self.dot(0)
                sleep(1)
                # O
                self.dash(1)
                self.dash(1)
                self.dash(1)
                sleep(1)
                # M
                self.dash(2)
                self.dash(2)
                sleep(1)
                # B
                self.dash(3)
                self.dot(3)
                self.dot(3)
                self.dot(3)
                sleep(1)

            if self.word == 'left':
                # L
                self.dot(0)
                self.dash(0)
                self.dot(0)
                self.dot(0)
                sleep(1)
                # E
                self.dot(1)
                sleep(1)
                # F
                self.dot(2)
                self.dot(2)
                self.dash(2)
                self.dot(2)
                sleep(1)
                # T
                self.dash(3)
                sleep(3)


# def Distance():
#     # set Trigger to HIGH
#     GPIO.output(GPIO_TRIGGER, True)

#     # set Trigger after 0.01ms to LOW
#     time.sleep(0.00001)
#     GPIO.output(GPIO_TRIGGER, False)

#     StartTime = time.time()
#     StopTime = time.time()

#     # save StartTime
#     while GPIO.input(GPIO_ECHO) == 0:
#         StartTime = time.time()

#     # save time of arrival
#     while GPIO.input(GPIO_ECHO) == 1:
#         StopTime = time.time()

#     # time difference between start and arrival
#     TimeElapsed = StopTime - StartTime
#     # multiply with the sonic speed (34300 cm/s)
#     # and divide by 2, because there and back
#     distance = (TimeElapsed * 34300) / 2

#     return distance

leds = [17, 16, 13, 12]
switches = [18, 19, 20, 21]
#flashing_lights(leds, switches)
    
 # setting up the GPIO
GPIO.setmode(GPIO.BCM)
 # I/O
GPIO.setup(leds, GPIO.OUT)
 # GPIO.setup(test_led, GPIO.OUT)
GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
 # GPIO.setup(wires, GPIO.IN)


##f1 = Module_Morse_Code(leds)

