from Game import Game
#import RPi.GPIO as GPIO
from tkinter import *
from random import *
from math import *

class Module_The_Button(Game):
    def __init__(self,other):
        super().__init__() 
        self.other = other

        
        self.name = "The Button"
        
        
        self.other.loc = "The Button"

        self.Module_Started = False
        self.Module_Done = False

        
        self.main(self.Module_Started)

    def main(self, started):

        self.other.clearFrame()
        self.other.rows = 3
        self.other.cols = 6
        self.other.pause_button(0, 0, 3)
        self.other.back_button(0, 3, 3)
        self.other.countdown(self.other.mins, self.other.secs, 1, 0, 2)
        self.other.counter = self.other.after(1000, self.other.update_timer, 1, 0,2)
        self.other.location(1, 2, 2)
        self.other.health(1, 4, 2)

        if started == False:

            self.Module_Started = True
            button_colors = ["red", "blue", "yellow", "white", "dim gray"]
            button_labels = ["Abort", "Detonate", "Hold", "Press"]
            self.strip_color = choice(button_colors)
            self.button_color = choice(button_colors)
            self.button_label = choice(button_labels)



        button = Label(self.other, bg=self.button_color, text=self.button_label, font=(
            "TexGyreAdventor", 25), borderwidth=10, relief="raised")
        button.grid(row=2, column=0, sticky=N+S+E+W, padx=5, pady=5, columnspan=5)

        strip = Label(self.other, text="", bg=self.strip_color,
                        borderwidth=10, relief="ridge")
        strip.grid(row=2, column=(self.other.cols-1), sticky=N+S+E+W, padx=5, pady=5, columnspan=1)

        for row in range(0, self.other.rows):
            Grid.rowconfigure(self.other, row, weight=0)
        Grid.rowconfigure(self.other, 2, weight=5)

        for col in range(self.other.cols):
            Grid.columnconfigure(self.other, col, weight=5)

        self.other.pack(fill=BOTH, expand=True)