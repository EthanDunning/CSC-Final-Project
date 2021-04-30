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

class flashing_lights():
    def __init__(self, leds, switches):
        self.leds = leds
        self.switches = switches
        self.module_Started = False
        self.module_Done = False
    def game_start(self):
        light_1 = random.choice(self.leds)
        while complete == False:
            GPIO.output(light_1, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(light_1, GPIO.LOW)
            sleep(0.5)
            # Red light 1
            if light_1 == 17 and GPIO.input(self.switches[0]) == GPIO.HIGH:
                sleep(3)
                if GPIO.input(switches[0]) == GPIO.HIGH:
                    self.module_Done = True
                    return self.module_Done
            

            # Blue light 2, 4
            elif light_1 == 12 and GPIO.input(self.switches[1]) == GPIO.HIGH and GPIO.input(self.switches[3]) == GPIO.HIGH:
                sleep(3)
                if GPIO.input(self.switches[1]) == GPIO.HIGH and GPIO.input(self.switches[3]) == GPIO.HIGH:
                    self.module_Done = True
                    return self.module_Done
            

            # Green light 4
            elif light_1 == 13 and GPIO.input(self.switches[3]) == GPIO.HIGH:
                sleep(3)
                if GPIO.input(self.switches[3]) == GPIO.HIGH:
                    self.module_Done = True
                    return self.module_Done

            

            # Yellow light 2, 3
            elif light_1 == 16 and GPIO.input(self.switches[1]) == GPIO.HIGH and GPIO.input(self.switches[2]) == GPIO.HIGH:
                sleep(3)
                if GPIO.input(self.switches[1]) == GPIO.HIGH and GPIO.input(self.switches[2]) == GPIO.HIGH:
                    self.module_Done = True
                    return self.module_Done

    
leds = [17, 16, 13, 12]
switches = [18, 19, 20, 21]
# flashing_lights(leds, switches)
    
# setting up the GPIO
GPIO.setmode(GPIO.BCM)
# I/O
GPIO.setup(leds, GPIO.OUT)
# GPIO.setup(test_led, GPIO.OUT)
GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(wires, GPIO.IN)

try:
    # testing the leds
    def all_on():
        for i in leds:
            GPIO.output(leds, True)

    def all_off():
        for i in leds:
            GPIO.output(leds, False)

    def switch_test():
        while True:
            for i in switches:
                if i == GPIO.HIGH:
                    GPIO.output(leds[1], True)


except KeyboardInterrupt:
    GPIO.cleanup()
try:
    all_on()
    sleep(0.5)
    all_off()
    sleep(0.5)
    
    g1 = flashing_lights(leds, switches)
    g1.game_start()
    GPIO.cleanup()
    print(x)
except KeyboardInterrupt:
    GPIO.cleanup()
