# Here we import all our modules
import RPi.GPIO as GPIO
from tkinter import *
from random import *
from math import *
from time import *
GPIO.setwarnings(False)

# Here is the class for the module
class Module_The_Button():
    def __init__(self, other, button_input):
        super().__init__()

        # Here we set up the class functions
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
        self.give_strike = False
        self.button_checker = None
        self.main(self.Module_Started)
        
    def main(self, started):
        # Here we set up the widgets and frame
        try:
            GPIO.cleanup()
        except:
            pass
        
        self.other.clearFrame()
        self.other.rows = 3
        self.other.cols = 6
        self.other.pause_button(0, 0, 3)
        self.other.back_button(0, 3, 3)
        self.other.countdown(1, 0, 2)
        self.other.location(1, 2, 2)
        self.other.health(1, 4, 2)
        self.Modules_Completed = 0
        

        

        # Here we set up the color and label for the button and strip
        if started == False:
            self.Module_Started = True
            button_colors = ["red", "blue", "yellow", "white", "gray"]
            button_labels = ["Abort", "Detonate", "Hold", "Press", "Disarm"]
            self.button_color = choice(button_colors)
            self.button_label = choice(button_labels)

            strip_colors = ["red", "blue", "yellow", "white"]
            self.strip_color = choice(strip_colors)
    
        # Here we set up the widgets
        the_button = Label(self.other, bg=self.button_color, text=self.button_label, font=(
            "TexGyreAdventor", 45), borderwidth=10, relief="raised")
        the_button.grid(row=2, column=0, sticky=N+S+E+W, padx=5, pady=5, columnspan=5)

        self.strip = Label(self.other, text="", bg="black",
                        borderwidth=10, relief="ridge")
        self.strip.grid(row=2, column=(self.other.cols-1), sticky=N+S+E+W, padx=5, pady=5, columnspan=1)

        # Here we configure the grid
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
        # Here we check to see if the defuser has followed the correct instructions
        if self.Module_Started == True:
            self.Modules_Completed = 0
            for module in self.other.Modules_Done:
                if module == True:
                    self.Modules_Completed += 1
            self.button_pressed = None
            
            # Here we get the time so we can mesure the time the button was pressed
            if GPIO.input(self.button) == 1 and self.end==None and self.start==None:
                self.start = time()
                
                self.strip.configure(bg=self.strip_color)
            if (GPIO.input(self.button) == 0 and self.start!=None and self.end==None):
                # set the strip color to default to black
                self.strip.configure(bg="black")

                # time the button was pressed
                self.end = time()
                
                self.button_time = (self.end-self.start)
                
                self.button_pressed = True
                if self.button_time >= 1:
                    self.button_pressed = False
                if self.button_time < 0.1:
                    self.button_pressed = None
                        
                self.start = None
                self.end = None
            
                # We set up the logic that is defined in the bomb defusal manual
                if self.button_color == "blue" and self.button_label == "Abort":
                    if self.button_pressed == True:
                        self.button_win()
                    else:
                        self.give_strike = True

                elif self.button_label == "Detonate":
                    if len(self.button_color) > 4:
                        if self.button_pressed == True:
                            self.button_win()
                        else:
                            self.give_strike = True

                    elif len(self.button_color) <= 4:
                        self.held_button()

                elif self.button_label == "Disarm":
                    if len(self.button_color) <= 4:
                        if self.button_pressed == True:
                            self.button_win()
                        else:
                            self.give_strike = True

                    elif len(self.button_color) > 4:
                        self.held_button()

                elif self.button_color == "gray":
                    self.held_button()

                elif self.button_color == "yellow" and self.Modules_Completed <= 3:
                    if self.button_pressed==True:
                        self.button_win()
                    else:
                        self.give_strike = True

                elif self.button_color == "red":
                    if self.button_pressed==True:
                            self.button_win()
                    else:
                        self.give_strike = True

                elif self.Modules_Completed == 5:
                    if self.button_pressed==True:
                            self.button_win()
                    else:
                        self.give_strike = True
                    
                else:
                    self.held_button()

            if self.give_strike == True:
                self.other.strike()
                self.give_strike = False
                    

    def held_button(self):
        # if the button is held we follow the logic in the bomb defusal manual
        
        time = self.other.time.get()
        
        if self.strip_color == "red":
            if "1" in time:
                
                self.button_win()
            else:
                self.give_strike = True

        elif self.strip_color == "yellow":
            if "3" in time:
                self.button_win()
            else:
                self.give_strike = True

        elif self.strip_color == "blue":
            if "7" in time:
                self.button_win()
            else:
                self.give_strike = True

        elif self.strip_color == "white":
            if "9" in time:
                self.button_win()
            else:
                self.give_strike = True

    def button_win(self):
        # if the instructions are followed correctly, the user wins and returns to the main menu 
        self.Module_Done = True
        self.other.MainMenu() 

        
        



        

