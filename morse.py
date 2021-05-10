
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
from tkinter import *

class Module_Morse_Code(Game):
    def __init__(self, other):
        super().__init__()
        self.other = other
        self.Module_Started = False
        self.Module_Done = False
        self.word = False
        self.TrueFreq = False
        self.name = 'Morse Code'
        self.other.loc = 'Morse Code'
        self.freq = 0
        self.leds = [17,16,13,12]
        self.word, self.TrueFreq = self.word_select()
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

        if started == False:
            self.Module_Started = True
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

        # start button
        start = Button(self.other, bg='purple', text = 'Start', font=('TexGyreAdventor', 45), borderwidth=10, relief='raised', command = lambda: self.Button_Press('start'))
        start.grid(row=3, column=0, sticky=N+S+E+W, padx=0, pady=0, columnspan=1)
        
        for col in range(self.other.cols):
            Grid.columnconfigure(self.other, col, weight=5)
        self.other.pack(fill=BOTH, expand=True)
        self.gpio_setup()
        #self.game_start(self.Module_Started)

    def gpio_setup(self):
         # setting up the GPIO
        GPIO.setmode(GPIO.BCM)
         # I/O
        GPIO.setup(self.leds, GPIO.OUT)
        return

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
            print(self.freq, self.TrueFreq)
            print(self.Module_Started)
            if self.freq == self.TrueFreq:
                self.Module_Done = True
                self.other.MainMenu()
            elif self.freq != self.TrueFreq:
                self.other.strike()
        elif Button == 'start':
            self.game_start(self.Module_Started)
            self.timer_update()
    

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
        GPIO.output(self.leds[light], GPIO.HIGH)
        self.other.after(250)
        GPIO.output(self.leds[light], GPIO.LOW)
        self.other.after(250)
        return
    # dash function
    def dash(self, light):
        GPIO.output(self.leds[light], GPIO.HIGH)
        self.other.after(750)
        GPIO.output(self.leds[light], GPIO.LOW)
        self.other.after(1000)
        return

    def timer_update(self):
        if self.other.secs <= 10:
            self.other.secs += 50
            self.other.mins -= 1
        else:
            self.other.secs -= 10


    def game_start(self, started):
        if self.Module_Done == False:
            print('start test')
            if self.word == 'fall':
                print('fall')
                # F
                self.dot(0)
                self.dot(0)
                self.dash(0)
                self.dot(0)
                self.other.after(1000)
                # A
                self.dot(1)
                self.dash(1)
                self.other.after(1000)
                # L
                self.dot(2)
                self.dash(2)
                self.dot(2)
                self.dot(2)
                self.other.after(1000)
                # L
                self.dot(3)
                self.dash(3)
                self.dot(3)
                self.dot(3)
                self.other.after(1000)
                print('after fall')
            
            if self.word == 'your':
                print('your')
                # Y
                self.dash(0)
                self.dot(0)
                self.dash(0)
                self.dash(0)
                self.other.after(1000)
                # O
                self.dash(1)
                self.dash(1)
                self.dash(1)
                self.other.after(1000)
                # U
                self.dot(2)
                self.dot(2)
                self.dash(2)
                self.other.after(1000)
                # R
                self.dot(3)
                self.dash(3)
                self.dot(3)
                self.other.after(1000)
                print('after your')

            if self.word == 'slid':
                print('slid')
                # S
                self.dot(0)
                self.dot(0)
                self.dot(0)
                self.other.after(1000)
                # L
                self.dot(1)
                self.dash(1)
                self.dot(1)
                self.dot(1)
                self.other.after(1000)
                # I
                self.dot(2)
                self.dot(2)
                self.other.after(1000)
                # D
                self.dash(3)
                self.dot(3)
                self.dot(3)
                self.other.after(1000)
                print('after slid')
            
            if self.word == 'bomb':
                print('bomb')
                # B
                self.dash(0)
                self.dot(0)
                self.dot(0)
                self.dot(0)
                self.other.after(1000)
                # O
                self.dash(1)
                self.dash(1)
                self.dash(1)
                self.other.after(1000)
                # M
                self.dash(2)
                self.dash(2)
                self.other.after(1000)
                # B
                self.dash(3)
                self.dot(3)
                self.dot(3)
                self.dot(3)
                self.other.after(1000)
                print('after bomb')

            if self.word == 'left':
                print('left')
                # L
                self.dot(0)
                self.dash(0)
                self.dot(0)
                self.dot(0)
                self.other.after(1000)
                # E
                self.dot(1)
                self.other.after(1000)
                # F
                self.dot(2)
                self.dot(2)
                self.dash(2)
                self.dot(2)
                self.other.after(1000)
                # T
                self.dash(3)
                self.other.after(1000)
                print('after left')

                

##leds = [17, 16, 13, 12]
##switches = [18, 19, 20, 21]
###flashing_lights(leds, switches)
##    
## # setting up the GPIO
##GPIO.setmode(GPIO.BCM)
## # I/O
##GPIO.setup(leds, GPIO.OUT)
## # GPIO.setup(test_led, GPIO.OUT)
##GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
## # GPIO.setup(wires, GPIO.IN)


##f1 = Module_Morse_Code(leds)

