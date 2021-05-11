import random
import RPi.GPIO as GPIO
from time import sleep
#from guiBase import *
from tkinter import *

class Module_Flashing_Lights():
    def __init__(self, other):
        super().__init__()
        self.other = other
        self.leds = [17, 16, 13, 12]
        self.switches = [18, 19, 20, 21]
        self.module_Started = False
        self.Module_Done = False
        self.name = 'Flashing Light'
        self.Modules_Completed = 0
        self.light_1 = 17#random.choice(self.leds)
        for i in self.other.Modules_Done:
            if i == True:
                self.Modules_Completed += 1
        # print('drifter', self.Modules_Completed)



        
    def main(self, started):
        # print('drifter', self.Modules_Completed)
        self.other.clearFrame()
        self.other.rows = 3
        self.other.cols = 6
        self.other.pause_button(0, 0, 3)
        self.other.back_button(0,3,3)
        self.other.countdown(1,0,2)
        self.other.location(1,2,2)
        self.other.health(1,4,2)
        alert = Button(self.other, bg='blue', text='Look at the GPIO', font=('TexGyreAdventor',45), borderwidth=10, relief='raised', command = lambda:self.switch_check())
        alert.grid(row=2, column=0, sticky=N+E+S+W, padx=0, pady=0, columnspan=6)
       
        # print('lmao')
        for col in range(self.other.cols):
            Grid.columnconfigure(self.other, col, weight=1)
        for row in range(self.other.rows):
            Grid.rowconfigure(self.other, row, weight=1)
        Grid.rowconfigure(self.other, 2, weight=5)
        self.other.pack(fill=BOTH, expand=True)
        # print('0')
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.light_1, GPIO.OUT)
        GPIO.output(self.light_1, GPIO.HIGH)
        # print('A')
        #self.switch_check()
        # print('penis')

    def switch_check(self):
        # print('ddick too')
        for i in range(len(self.switches)):
            GPIO.setup(self.switches[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        print('butt')
        # Red light 1
        if self.light_1 == 17:
            print('k')
            # if Modules Completed is even
            if self.Modules_Completed % 2 == 0:
                # if strikes = 0
                if self.other.strikes == 0:
                    print('l')
                    # press buttons 1, 3
                    if (GPIO.input(self.switches[0]) == GPIO.HIGH) and (GPIO.input(self.switches[2]) == GPIO.HIGH):
                        self.Module_Done = True
                        print('m')
                        self.other.MainMenu()
                    elif (GPIO.input(self.switches[1]) == GPIO.HIGH) or (GPIO.input(self.switches[3]) == GPIO.HIGH):
                        self.other.strike()
                # if strikes = 1
                elif self.other.strikes == 1:
                    # press buttons 2, 3
                    if (GPIO.input(self.switches[1]) == GPIO.HIGH) and (GPIO.input(self.switches[2]) == GPIO.HIGH):
                        self.Module_Done = True
                        self.other.MainMenu()
                    elif (GPIO.input(self.switches[0]) == GPIO.HIGH) or (GPIO.input(self.switches[3]) == GPIO.HIGH):
                        self.other.strike()
                # if strikes >= 2
                elif self.other.strikes >= 2:
                    # press button 1
                    if (GPIO.input(self.switches[0]) == GPIO.HIGH):
                        self.Module_Done = True
                        self.other.MainMenu()
                    elif (GPIO.input(self.switches[1]) == GPIO.HIGH) or (GPIO.input(self.switches[2]) == GPIO.HIGH) or (GPIO.input(self.switches[3]) == GPIO.HIGH):
                        self.other.strike()
            # if Modules Completed is odd
            elif  not (self.Modules_Completed % 2):
                # if more than half time left
                if (self.other.secs >= 30 and self.other.mins >= 2) or (self.other.mins > 2):
                    # press button 4
                    if (GPIO.input(self.switches[3]) == GPIO.HIGH):
                        self.Module_Done = True
                        self.other.MainMenu()
                    elif (GPIO.input(self.switches[0]) == GPIO.HIGH) or (GPIO.input(self.switches[1]) == GPIO.HIGH) or (GPIO.input(self.switches[2]) == GPIO.HIGH):
                        self.other.strike()
                # if less than half time left 
                elif (self.other.secs <= 30 and self.other.mins<= 2) or (self.other.mins < 2):
                    # press buttons 1, 3
                    if (GPIO.input(self.switches[0]) == GPIO.HIGH) and (GPIO.input(self.switches[2]) == GPIO.HIGH):
                        self.Module_Done = True
                        self.other.MainMenu()

        # Blue light 2, 4
        elif self.light_1 == 12:
            # if modules completed = 1 or 5
            if self.Modules_Completed == 1 or self.Modules_Completed == 5:
                # if strikes = 0
                if self.other.strikes == 0:
                    # press buttons 2, 4
                    if (GPIO.input(self.switches[1]) == GPIO.HIGH) and (GPIO.input(self.switches[3]) == GPIO.HIGH):
                        self.Module_Done = True
                        self.other.MainMenu()
                    elif (GPIO.input(self.switches[0]) == GPIO.HIGH) or (GPIO.input(self.switches[2]) == GPIO.HIGH):
                        self.other.strike()
                # if strikes = 1
                elif self.other.strikes == 1:
                    # press button 3
                    if (GPIO.input(self.switches[3]) == GPIO.HIGH):
                        self.Module_Done = True
                        self.other.MainMenu()
                    elif (GPIO.input(self.switches[0]) == GPIO.HIGH) or (GPIO.input(self.switches[1]) == GPIO.HIGH) or (GPIO.input(self.switches[2]) == GPIO.HIGH):
                        self.other.strike()
                # if strikes >= 2
                elif self.other.strikes >= 2:
                    # press buttons 1, 2
                    if (GPIO.input(self.switches[0]) == GPIO.HIGH) and (GPIO.input(self.switches[1]) == GPIO.HIGH):
                        self.Module_Done = True
                        self.other.MainMenu()
                    elif (GPIO.input(self.switches[2]) == GPIO.HIGH)  or (GPIO.input(self.switches[3]) == GPIO.HIGH):
                        self.other.strike()
            if self.Modules_Completed == 2 or self.Modules_Completed == 3:
                # if strikes = 0
                if self.other.strikes == 0:
                    # press buttons 4
                    if (GPIO.input(self.switches[3]) == GPIO.HIGH):
                        self.Module_Done = True
                        self.other.MainMenu()
                    elif (GPIO.input(self.switches[0]) == GPIO.HIGH) or (GPIO.input(self.switches[2]) == GPIO.HIGH) or (GPIO.input(self.switches[1]) == GPIO.HIGH):
                        self.other.strike()
                # if strikes = 1
                elif self.other.strikes == 1:
                    # press button 3,4
                    if (GPIO.input(self.switches[3]) == GPIO.HIGH) and (GPIO.input(self.switches[2]) == GPIO.HIGH):
                        self.Module_Done = True
                        self.other.MainMenu()
                    elif (GPIO.input(self.switches[0]) == GPIO.HIGH) or (GPIO.input(self.switches[1]) == GPIO.HIGH):
                        self.other.strike()
                # if strikes >= 2
                elif self.other.strikes >= 2:
                    # press buttons 1, 3
                    if (GPIO.input(self.switches[0]) == GPIO.HIGH) and (GPIO.input(self.switches[2]) == GPIO.HIGH):
                        self.Module_Done = True
                        self.other.MainMenu()
                    elif (GPIO.input(self.switches[1]) == GPIO.HIGH)  or (GPIO.input(self.switches[3]) == GPIO.HIGH):
                        self.other.strike()
            if self.Modules_Completed == 4 or self.Modules_Completed == 6:
                # if strikes = 0
                if self.other.strikes == 0:
                    # press buttons 2
                    if (GPIO.input(self.switches[1]) == GPIO.HIGH):
                        self.Module_Done = True
                        self.other.MainMenu()
                    elif (GPIO.input(self.switches[0]) == GPIO.HIGH) or (GPIO.input(self.switches[2]) == GPIO.HIGH) or (GPIO.input(self.switches[3]) == GPIO.HIGH):
                        self.other.strike()
                # if strikes = 1
                elif self.other.strikes == 1:
                    # press button 1,3
                    if (GPIO.input(self.switches[0]) == GPIO.HIGH) and (GPIO.input(self.switches[2]) == GPIO.HIGH):
                        self.Module_Done = True
                        self.other.MainMenu()
                    elif (GPIO.input(self.switches[1]) == GPIO.HIGH) or (GPIO.input(self.switches[3]) == GPIO.HIGH):
                        self.other.strike()
                # if strikes >= 2
                elif self.other.strikes >= 2:
                    # press buttons 1, 4
                    if (GPIO.input(self.switches[0]) == GPIO.HIGH) and (GPIO.input(self.switches[3]) == GPIO.HIGH):
                        self.Module_Done = True
                        self.other.MainMenu()
                    elif (GPIO.input(self.switches[1]) == GPIO.HIGH)  or (GPIO.input(self.switches[2]) == GPIO.HIGH):
                        self.other.strike()

        # Green light 3
        elif self.light_1 == 13:
            # push this button
            if (GPIO.input(self.switches[2]) == GPIO.HIGH):
                self.Module_Done = True
                self.other.MainMenu()
            # not these buttons
            elif (GPIO.input(self.switches[0]) == GPIO.HIGH) or (GPIO.input(self.switches[1]) == GPIO.HIGH) or (GPIO.input(self.switches[3]) == GPIO.HIGH):
                self.other.strike()

        

        # Yellow light 2, 3
        elif self.light_1 == 16:
            # if more than half time left
            if (self.other.secs >= 30 and self.other.mins >= 2) or (self.other.mins > 2):
                # if modules completed is odd
                if not (self.Modules_Completed % 2):
                    # press button 3
                    if GPIO.input(self.switches[2]) == GPIO.HIGH:
                        self.Module_Done = True
                        self.other.MainMenu()
                    elif (GPIO.input(self.switches[0]) == GPIO.HIGH) or (GPIO.input(self.switches[1]) == GPIO.HIGH) or (GPIO.input(self.switches[3]) == GPIO.HIGH):
                        self.other.strike()
                # if modules completed is even
                elif self.Modules_Completed % 2:
                    # press buttons 1, 2
                    if (GPIO.input(self.switches[0]) == GPIO.HIGH) and (GPIO.input(self.switches[1]) == GPIO.HIGH):
                        self.Module_Done = True
                        self.other.MainMenu()
                    elif (GPIO.input(self.switches[2]) == GPIO.HIGH) and (GPIO.input(self.switches[3]) == GPIO.HIGH):
                        self.other.strike()
            elif (self.other.secs <= 30 and self.other.mins<= 2) or (self.other.mins < 2):
                if not (self.Modules_Completed % 2):
                    if (GPIO.input(self.switches[0]) == GPIO.HIGH) and (GPIO.input(self.switches[3]) == GPIO.HIGH):
                        self.Module_Done = True
                        self.other.MainMenu()
                    elif (GPIO.input(self.switches[1]) == GPIO.HIGH) and (GPIO.input(self.switches[2]) == GPIO.HIGH):
                        self.other.strike()
                elif self.Modules_Completed % 2:
                    if (GPIO.input(self.switches[0]) == GPIO.HIGH) and (GPIO.input(self.switches[2]) == GPIO.HIGH):
                        self.Module_Done= True
                        self.other.MainMenu()
                    elif (GPIO.input(self.switches[1]) == GPIO.HIGH) and (GPIO.input(self.switches[3]) == GPIO.HIGH):
                        self.other.strike()
        # print('balls as well')

