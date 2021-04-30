from Game import Game
import RPi.GPIO as GPIO
from tkinter import *
from random import *
from math import *
from time import *
GPIO.setwarnings(False)
class Module_The_Button(Game):
    def __init__(self,other):
        super().__init__() 
        self.other = other
        self.name = "The Button"
        self.other.loc = "The Button"
        self.Module_Started = False
        self.Module_Done = False
        self.button = 25
        self.main(self.Module_Started)
        self.start = None
        self.end = None
        
        self.button_checker = None
        #self.button_test()
        

        

    def main(self, started):

        self.other.clearFrame()
        self.other.rows = 3
        self.other.cols = 6
        self.other.pause_button(0, 0, 3)
        self.other.back_button(0, 3, 3)
        self.other.countdown(1, 0, 2)
        self.other.location(1, 2, 2)
        self.other.health(1, 4, 2)

        if started == False:
            self.Module_Started = True
            button_colors = ["red", "blue", "yellow", "white", "dim gray"]
            button_labels = ["Abort", "Detonate", "Hold", "Press", "Disarm"]
            self.button_color = choice(button_colors)
            self.button_label = choice(button_labels)
            strip_colors = ["red", "blue", "yellow", "white"]
            self.strip_color = choice(strip_colors)
    
        the_button = Label(self.other, bg=self.button_color, text=self.button_label, font=(
            "TexGyreAdventor", 25), borderwidth=10, relief="raised")
        the_button.grid(row=2, column=0, sticky=N+S+E+W, padx=5, pady=5, columnspan=5)

        strip = Label(self.other, text="", bg="black",
                        borderwidth=10, relief="ridge")
        strip.grid(row=2, column=(self.other.cols-1), sticky=N+S+E+W, padx=5, pady=5, columnspan=1)

        for row in range(0, self.other.rows):
            Grid.rowconfigure(self.other, row, weight=0)
        Grid.rowconfigure(self.other, 2, weight=5)

        for col in range(self.other.cols):
            Grid.columnconfigure(self.other, col, weight=5)

        self.other.pack(fill=BOTH, expand=True)

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(26, GPIO.OUT)
        GPIO.setup(self.button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.remove_event_detect(self.button)
        GPIO.add_event_detect(self.button, GPIO.BOTH, callback=lambda *a: self.button_check())

        

    def button_check(self):
        if self.Module_Started == True:
            




            if GPIO.input(self.button) == 1:
                self.start = time()
            elif (GPIO.input(self.button) == 0 and self.start != None):
                self.end = time()
                print(self.end-self.start)
                self.start = None
                self.end = None
            GPIO.output(26, GPIO.input(self.button))

        
        



        

