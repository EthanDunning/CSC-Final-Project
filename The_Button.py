from Game import Game
import RPi.GPIO as GPIO
from tkinter import *
from random import *
from math import *
from time import *
GPIO.setwarnings(False)
class Module_The_Button(Game):
    def __init__(self,other,button_input):
        super().__init__() 
        self.other = other
        self.name = "The Button"
        self.other.loc = "The Button"
        self.Module_Started = False
        self.Module_Done = False
        self.button = button_input
        
        self.start = None
        self.end = None
        self.button_time = None
        self.button_pressed = None
        
        self.button_checker = None
        self.main(self.Module_Started)
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
        self.Modules_Completed = 0
        for module in self.other.Modules_Done:
            if module == True:
                self.Modules_Completed += 1

        #print(self.Modules_Completed)

        if started == False:
            self.Module_Started = True
            button_colors = ["red", "blue", "yellow", "white", "gray"]
            button_labels = ["Abort", "Detonate", "Hold", "Press", "Disarm"]
            self.button_color = choice(button_colors)
            self.button_label = choice(button_labels)

            strip_colors = ["red", "blue", "yellow", "white"]
            self.strip_color = choice(strip_colors)
    
        the_button = Label(self.other, bg=self.button_color, text=self.button_label, font=(
            "TexGyreAdventor", 45), borderwidth=10, relief="raised")
        the_button.grid(row=2, column=0, sticky=N+S+E+W, padx=5, pady=5, columnspan=5)

        self.strip = Label(self.other, text="", bg="black",
                        borderwidth=10, relief="ridge")
        self.strip.grid(row=2, column=(self.other.cols-1), sticky=N+S+E+W, padx=5, pady=5, columnspan=1)

        for row in range(0, self.other.rows):
            Grid.rowconfigure(self.other, row, weight=2)
        Grid.rowconfigure(self.other, 2, weight=5)

        for col in range(self.other.cols):
            Grid.columnconfigure(self.other, col, weight=5)

        self.other.pack(fill=BOTH, expand=True)

        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(22, GPIO.OUT)
            GPIO.setup(self.button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            GPIO.remove_event_detect(self.button)
            GPIO.add_event_detect(self.button, GPIO.BOTH, callback=lambda *a: self.button_check(), bouncetime=100)
        except:
            pass

        

    def button_check(self):
        if self.Module_Started == True:
            self.button_pressed = None
            #GPIO.output(22, GPIO.input(self.button))
            if GPIO.input(self.button) == 1 and self.end==None and self.start==None:
                self.start = time()
                #print("started")
                self.strip.configure(bg=self.strip_color)
            if (GPIO.input(self.button) == 0 and self.start!=None and self.end==None):
                self.strip.configure(bg="black")
                self.end = time()
                #print("ended")
                self.button_time = (self.end-self.start)
                #print(self.button_time)
                self.button_pressed = True
                if self.button_time >= 1:
                    self.button_pressed = False
                        
                self.start = None
                self.end = None
            

                if self.button_color == "blue" and self.button_label == "Abort":
                    if self.button_pressed == True:
                        self.button_win()
                    else:
                        self.other.strike()

                elif self.button_label == "Detonate":
                    if len(self.button_color) > 4:
                        if self.button_pressed == True:
                            self.button_win()
                        else:
                            self.other.strike()

                    elif len(self.button_color) <= 4:
                        self.held_button()

                elif self.button_label == "Disarm":
                    if len(self.button_color) <= 4:
                        if self.button_pressed == True:
                            self.button_win()
                        else:
                            self.other.strike()

                    elif len(self.button_color) > 4:
                        self.held_button()

                elif self.button_color == "gray":
                    self.held_button()

                elif self.button_color == "yellow" and self.Modules_Completed <= 3:
                    if self.button_pressed==True:
                        self.button_win()
                    else:
                        self.other.strike()

                elif self.button_color == "red":
                    if self.button_pressed==True:
                            self.button_win()
                    else:
                        self.other.strike()

                if self.Modules_Completed == 5:
                    if self.button_pressed==True:
                            self.button_win()
                    else:
                        self.other.strike()
                    
                else:
                    self.held_button()
                    

    def held_button(self):
        
        #print(self.strip_color)
        time = self.other.time.get()
        #print(time)
        if self.strip_color == "red":
            if "1" in time:
                print("win")
                self.button_win()
            else:
                self.other.strike()

        elif self.strip_color == "yellow":
            if "3" in time:
                self.button_win()
            else:
                self.other.strike()

        elif self.strip_color == "blue":
            if "7" in time:
                self.button_win()
            else:
                self.other.strike()

        elif self.strip_color == "white":
            if "9" in time:
                self.button_win()
            else:
                self.other.strike()

    def button_win(self):
        self.Module_Done = True
        self.other.MainMenu() 

        
        



        

