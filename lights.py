# One light of a random color will begin blinking
# Depending on the light, different buttons must
# be held to stop the blinking and light the 
# light completely.
# Red light, button 1 only
# Blue light, buttons 2 and 4
# Green light, button 4 only
# Yellow light, buttons 2 and 3

# if the wrong buttons are pressed, a strike is added.
# if the right buttons are pressed and released before the 
# light stops blinking, a strike will be added.
# if the players complete the puzzle, the light will stay on,
# then turn off.

import random
import RPi.GPIO as GPIO
from time import sleep
from Game import *
#from guiBase import *
from tkinter import *

class Module_Flashing_Lights(Game):
    def __init__(self, leds, switches, other):
        super().__init__()
        self.other = other
        self.leds = leds
        self.switches = switches
        self.module_Started = False
        self.module_Done = False
        self.name = 'Flashing Light'

##    def gpio_setup(self):
##        leds = [17, 16, 13, 12]
##        switches = [18, 19, 20, 21]
##         # setting up the GPIO
##        GPIO.setmode(GPIO.BCM)
##         # I/O
##        GPIO.setup(self.leds, GPIO.OUT)
##        GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
##        return

        
    def main(self, started):
##        leds = [17, 16, 13, 12]
##        switches = [18, 19, 20, 21]
##         # setting up the GPIO
##        GPIO.setmode(GPIO.BCM)
##         # I/O
##        GPIO.setup(self.leds, GPIO.OUT)
##        GPIO.setup(self.switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
##        GPIO.output(self.leds, GPIO.HIGH)
##        self.other.after(1000)
##        GPIO.output(self.leds, GPIO.LOW)
        print('started')
        self.other.clearFrame()
        print('1')
        self.other.rows = 3
        print('2')
        self.other.cols = 1
        self.other.pause_button(0, 0, 1)
        self.other.back_button(0,2,1)
        self.other.countdown(0,1,1)
        self.other.location(1,1,1)
        self.other.health(1,2,1)
        alert = Label(self.other, bg='blue', text='Look at the GPIO', font=('TexGyreAdventor',45), borderwidth=10, relief='raised')
        alert.grid(row=1, column=0, sticky=N+E+S+W, padx=0, pady=0, columnspan=4)
       
        print('lmao')
##        self.all_on()
##        self.other.after(1000)
##        self.all_off()
##        self.other.after(1000)
        for col in range(self.other.cols):
            Grid.columnconfigure(self.other, col, weight=5)
        self.other.pack(fill=BOTH, expand=True)
        self.game_start()
        self.light_flash()

    def light_flash(self):
        if self.module_Done == False:
            GPIO.output(self.light_1, GPIO.HIGH)
            self.other.after(500)

    def game_start(self):
        GPIO.setmode(GPIO.BCM)
         # I/O
        GPIO.setup(self.leds, GPIO.OUT)
        GPIO.setup(self.switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.output(self.leds, GPIO.HIGH)
        self.other.after(1000)
        GPIO.output(self.leds, GPIO.LOW)
        print('3')
        self.Module_Started = True
        self.light_1 = random.choice(self.leds)
        print('light test')
        print(self.light_1)
        self.light_flash()
        print('method test')
        
    def switch_check(self):
        # Red light 1
        if light_1 == 17: 
            # push this button
            if GPIO.input(self.switches[0]) == GPIO.HIGH:
                GPIO.output(light_1, GPIO.HIGH)
                self.other.after(500)
                GPIO.output(light_1, GPIO.LOW)
                self.other.after(500)
                GPIO.output(light_1, GPIO.HIGH)
                self.other.after(500)
                GPIO.output(light_1, GPIO.LOW)
                self.other.after(500)   
                GPIO.output(light_1, GPIO.HIGH)
                self.other.after(500)
                GPIO.output(light_1, GPIO.LOW)
                self.other.after(500)      
                # after 3 seconds ...           
                if GPIO.input(switches[0]) == GPIO.HIGH:
                    self.module_Done = True
                    return self.module_Done
            # not these buttons
            elif GPIO.input(self.switches[3]) == GPIO.HIGH or GPIO.input(self.switches[1]) == GPIO.HIGH or GPIO.input(self.switches[2]) == GPIO.HIGH:
                self.strike()
        

        # Blue light 2, 4
        elif light_1 == 12:
            # Push these buttons
            if GPIO.input(self.switches[1]) == GPIO.HIGH and GPIO.input(self.switches[3]) == GPIO.HIGH:
                GPIO.output(light_1, GPIO.HIGH)
                self.other.after(500)
                GPIO.output(light_1, GPIO.LOW)
                self.other.after(500)
                GPIO.output(light_1, GPIO.HIGH)
                self.other.after(500)
                GPIO.output(light_1, GPIO.LOW)
                self.other.after(500)   
                GPIO.output(light_1, GPIO.HIGH)
                self.other.after(500)
                GPIO.output(light_1, GPIO.LOW)
                self.other.after(500)
                # after 3 seconds, if they are still pressed, the module is complete
                if GPIO.input(self.switches[1]) == GPIO.HIGH and GPIO.input(self.switches[3]) == GPIO.HIGH:
                    self.module_Done = True
                    return self.module_Done
            # not these buttons
            elif GPIO.input(self.switches[2]) == GPIO.HIGH or GPIO.input(self.switches[0]) == GPIO.HIGH:
                self.strike()
        

        # Green light 4
        elif light_1 == 13:
            # push this button
            if GPIO.input(self.switches[3]) == GPIO.HIGH:
                GPIO.output(light_1, GPIO.HIGH)
                self.other.after(500)
                GPIO.output(light_1, GPIO.LOW)
                self.other.after(500)
                GPIO.output(light_1, GPIO.HIGH)
                self.other.after(500)
                GPIO.output(light_1, GPIO.LOW)
                self.other.after(500)   
                GPIO.output(light_1, GPIO.HIGH)
                self.other.after(500)
                GPIO.output(light_1, GPIO.LOW)
                self.other.after(500)
                # after 3 seconds, if the button is still pressed, the module is complete
                if GPIO.input(self.switches[3]) == GPIO.HIGH:
                    self.module_Done = True
                    return self.module_Done
            # not these buttons
            elif GPIO.input(self.switches[0]) == GPIO.HIGH or GPIO.input(self.switches[1]) == GPIO.HIGH or GPIO.input(self.switches[2]) == GPIO.HIGH:
                self.strike()

        

        # Yellow light 2, 3
        elif light_1 == 16:
            # push these buttons 
            if GPIO.input(self.switches[1]) == GPIO.HIGH and GPIO.input(self.switches[2]) == GPIO.HIGH:
                GPIO.output(light_1, GPIO.HIGH)
                self.other.after(500)
                GPIO.output(light_1, GPIO.LOW)
                self.other.after(500)
                GPIO.output(light_1, GPIO.HIGH)
                self.other.after(500)
                GPIO.output(light_1, GPIO.LOW)
                self.other.after(500)   
                GPIO.output(light_1, GPIO.HIGH)
                self.other.after(500)
                GPIO.output(light_1, GPIO.LOW)
                self.other.after(500)
                # after 3 seconds ...
                if GPIO.input(self.switches[1]) == GPIO.HIGH and GPIO.input(self.switches[2]) == GPIO.HIGH:
                    self.module_Done = True
                    return self.module_Done
            # not these buttons
            elif GPIO.input(self.switches[0]) == GPIO.HIGH or GPIO.input(self.switches[3]) == GPIO.HIGH:
                self.strike()

    
##leds = [17, 16, 13, 12]
##switches = [18, 19, 20, 21]
### flashing_lights(leds, switches)
##    
### setting up the GPIO
##GPIO.setmode(GPIO.BCM)
### I/O
##GPIO.setup(leds, GPIO.OUT)
### GPIO.setup(test_led, GPIO.OUT)
##GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(wires, GPIO.IN)

##try:
    # testing the leds
    def all_on(self):
        for i in self.leds:
            GPIO.output(i, True)

    def all_off(self):
        for i in self.leds:
            GPIO.output(i, False)

    def switch_test():
        while True:
            for i in switches:
                if i == GPIO.HIGH:
                    GPIO.output(leds[1], True)
##
##
##except KeyboardInterrupt:
##    GPIO.cleanup()
##try:
##    all_on()
##    sleep(0.5)
##    all_off()
##    sleep(0.5)
##    
##    g1 = flashing_lights(leds, switches)
##    g1.game_start()
##    GPIO.cleanup()
##except KeyboardInterrupt:
##    GPIO.cleanup()
##g1 = Module_Flashing_Lights(leds, switches)
##g1.game_start()
