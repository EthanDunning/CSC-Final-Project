
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

from tkinter import *

class Module_Morse_Code():
    def __init__(self, other):
        super().__init__()
        self.other = other
        self.Module_Started = False
        self.Module_Done = False
        # self.word = False
        # self.TrueFreq = False
        self.name = 'Morse Code'
        self.other.loc = 'Morse Code'
        self.Word_Freq, self.Word_Morse = self.dictionary_Setup()
        self.TrueFreq, self.g1, self.g2, self.g3, self.g4 = self.Word_Select_Split()
        self.leds = [17,16,13,12]
        self.freq = 0
        # self.word, self.TrueFreq = self.word_select()
        self.main(self.Module_Started)

    # gui build
    def main(self, started):
        # print('started')
        self.other.clearFrame()
        self.other.rows = 4
        self.other.cols = 1
        # print('check 1')
        self.other.pause_button(0, 0, 2)
        self.other.back_button(0, 2, 2)
        self.other.countdown(1, 0, 1)
        self.other.location(1, 1, 1)
        self.other.health(1, 2, 1)
        self.other.Modules_completed = 0
        for module in self.other.Modules_Done:
            self.other.Modules_completed += 1

        # print(self.other.Modules_completed)

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
        
        for row in range(self.other.rows):
            Grid.rowconfigure(self.other, row, weight=5)
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
            # print(self.freq)
            freq = Label(self.other, bg='blue', text=self.freq, font=('TexGyreAdventor', 45), borderwidth=10, relief='raised')
            freq.grid(row=2, column=1, sticky=N+S+E+W, padx=0, pady=0, columnspan=1)
            return self.freq
        elif Button == 'down':
            self.freq -= 1
            # print(self.freq)
            freq = Label(self.other, bg='blue', text=self.freq, font=('TexGyreAdventor', 45), borderwidth=10, relief='raised')
            freq.grid(row=2, column=1, sticky=N+S+E+W, padx=0, pady=0, columnspan=1)
            return self.freq
        elif Button == 'check':
            print(self.freq, self.TrueFreq)
            # print(self.Module_Started)
            if self.freq == self.TrueFreq:
                self.Module_Done = True
                self.other.MainMenu()
            elif self.freq != self.TrueFreq:
                self.other.strike()
        elif Button == 'start':
            self.game_start(self.Module_Started)
            self.timer_update()
        
    def dictionary_Setup(self):
        # L1{~~~~~}
        Word_Freq = {
            0:'Slid', 1:'Pens', 2:'That',
            3:'Left', 4:'Fall', 5:'Flip',
            6:'Bomb', 7:'Skip', 8:'Into',
            9:'Lean', 10:'Blew', 11:'Have',
            12:'Four', 13:'Your', 14:'Yeah'
        }
        # 0 = Dot, 1 = Dash, 2,3 = Break
        # L2{~~~~~}
        Word_Morse = {
            'Slid':'03030323031303032303032313030', 'Pens':'0313130323032313032303030',
            'That':'132303030303230313231', 'Left':'0313030323032303031303231',
            'Fall':'030313032303132303130303230313030', 'Flip':'0303130323031303032303030313130',
            'Bomb':'1303030323131313231313231303030', 'Skip':'03030323130313230303230313130',
            'Into':'030323130323132313131', 'Lean':'03130303230323031323130',
            'Blew':'13030303230313030323032303131', 'Have':'030303032303132303030313230',
            'Four':'0303130323131313230303132303130', 'Your':'1303131323131313230303132303130',
            'Yeah':'130313132303230313230303030'
        }
        return Word_Freq, Word_Morse

    def Word_Select_Split(self):
        # x, the frequency
        x = random.randint(0, 14)
        # print(x)
        # L1[x], The word
        y1 = self.Word_Freq[x]
        # print(y1)
        # L2[y1], the morse code in a string
        y2 = self.Word_Morse[y1]
        # print(y2)
        # y2.split('2'), a list of the letters in morse
        z1 = y2.split('2')
        # print(z1)
        # z1.split('3'), lists of each letter split into dots and dashes
        g1 = z1[0].split('3')
        # print(g1)
        g2 = z1[1].split('3')
        # print(g2)
        g3 = z1[2].split('3')
        # print(g3)
        try:
            g4 = z1[3].split('3')
        except:
            pass
        # print(g4)
        # x is the frequency, g1-4 are lists of each letter in morse
        try:
            return x, g1, g2, g3, g4
        except:
            return x, g1, g2, g3

                

    # picks a random word from the list
    # def word_select(self):
    #     words = ['fall', 'your', 'slid', 'bomb', 'left']
    #     freqs = [4, 13, 0, 6, 3]
    #     x = random.randint(0, 4)
    #     word = words[x]
    #     freq = freqs[x]
    #     return word, freq

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
        self.other.pack()
        return
    # dash function
    def dash(self, light):
        GPIO.output(self.leds[light], GPIO.HIGH)
        self.other.after(750)
        GPIO.output(self.leds[light], GPIO.LOW)
        self.other.after(1000)
        self.other.pack()
        return

    def timer_update(self):
        if self.other.secs <= 10:
            self.other.secs += 50
            self.other.mins -= 1
        else:
            self.other.secs -= 10


    def game_start(self, started):
        if self.Module_Done == False:
            # print('start test')
            # self.Word_Freq, self.Word_Morse = self.dictionary_Setup()
            # self.x, self.g1, self.g2, self.g3, self.g4 = self.Word_Select_Split()
            for i in self.g1:
                if i == '1':
                    self.dash(0)
                if i == '0':
                    self.dot(0)
            for i in self.g2:
                if i == '1':
                    self.dash(1)
                if i == '0':
                    self.dot(1)
            for i in self.g3:
                if i == '1':
                    self.dash(2)
                if i == '0':
                    self.dot(2)
            for i in self.g4:
                if i == '1':
                    self.dash(3)
                if i == '0':
                    self.dot(3)
            return
            # if self.word == 'fall':
            #     # print('fall')
            #     # F
            #     self.dot(0)
            #     self.dot(0)
            #     self.dash(0)
            #     self.dot(0)
            #     self.other.after(1000)
            #     # A
            #     self.dot(1)
            #     self.dash(1)
            #     self.other.after(1000)
            #     # L
            #     self.dot(2)
            #     self.dash(2)
            #     self.dot(2)
            #     self.dot(2)
            #     self.other.after(1000)
            #     # L
            #     self.dot(3)
            #     self.dash(3)
            #     self.dot(3)
            #     self.dot(3)
            #     self.other.after(1000)
            #     # print('after fall')
            
            # if self.word == 'your':
            #     # print('your')
            #     # Y
            #     self.dash(0)
            #     self.dot(0)
            #     self.dash(0)
            #     self.dash(0)
            #     self.other.after(1000)
            #     # O
            #     self.dash(1)
            #     self.dash(1)
            #     self.dash(1)
            #     self.other.after(1000)
            #     # U
            #     self.dot(2)
            #     self.dot(2)
            #     self.dash(2)
            #     self.other.after(1000)
            #     # R
            #     self.dot(3)
            #     self.dash(3)
            #     self.dot(3)
            #     self.other.after(1000)
            #     # print('after your')

            # if self.word == 'slid':
            #     # print('slid')
            #     # S
            #     self.dot(0)
            #     self.dot(0)
            #     self.dot(0)
            #     self.other.after(1000)
            #     # L
            #     self.dot(1)
            #     self.dash(1)
            #     self.dot(1)
            #     self.dot(1)
            #     self.other.after(1000)
            #     # I
            #     self.dot(2)
            #     self.dot(2)
            #     self.other.after(1000)
            #     # D
            #     self.dash(3)
            #     self.dot(3)
            #     self.dot(3)
            #     self.other.after(1000)
            #     # print('after slid')
            
            # if self.word == 'bomb':
            #     # print('bomb')
            #     # B
            #     self.dash(0)
            #     self.dot(0)
            #     self.dot(0)
            #     self.dot(0)
            #     self.other.after(1000)
            #     # O
            #     self.dash(1)
            #     self.dash(1)
            #     self.dash(1)
            #     self.other.after(1000)
            #     # M
            #     self.dash(2)
            #     self.dash(2)
            #     self.other.after(1000)
            #     # B
            #     self.dash(3)
            #     self.dot(3)
            #     self.dot(3)
            #     self.dot(3)
            #     self.other.after(1000)
            #     # print('after bomb')

            # if self.word == 'left':
            #     # print('left')
            #     # L
            #     self.dot(0)
            #     self.dash(0)
            #     self.dot(0)
            #     self.dot(0)
            #     self.other.after(1000)
            #     # E
            #     self.dot(1)
            #     self.other.after(1000)
            #     # F
            #     self.dot(2)
            #     self.dot(2)
            #     self.dash(2)
            #     self.dot(2)
            #     self.other.after(1000)
            #     # T
            #     self.dash(3)
            #     self.other.after(1000)
            #    # print('after left')

                

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

