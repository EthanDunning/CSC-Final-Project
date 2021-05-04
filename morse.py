
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
import tkinter
import random
class morse():
    def __init__(self, lights):
        self.module_Started = False
        self.module_Done = False
        self.word = False
        self.lights = lights
        self.name = 'Morse Code'

    # picks a random word from the list
    def word_select(self):
        words = ['fall', 'your', 'slid', 'bomb', 'left']
        word = random.choice(words)
        return word

    @property
    def word(self):
        return self._word
    @word.setter
    def word(self, value):
        self._word = value

    # dot function
    def dot(self, light):
        GPIO.output(leds[light], GPIO.HIGH)
        sleep(0.25)
        GPIO.output(leds[light], GPIO.LOW)
        sleep(0.25)
    # dash function
    def dash(self, light):
        GPIO.output(leds[light], GPIO.HIGH)
        sleep(0.75)
        GPIO.output(leds[light], GPIO.LOW)
        sleep(1)


    def game_start(self):
        self.word = self.word_select()
        while self.module_Done == False:
            if word == 'fall':
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
                if 2 == 2:
                    #self.module_Done = True
                    #return self.module_Done
                    pass
                else:
                    self.strike()
            
            if word == 'your':
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
                if 4 == 4:
                    #self.module_Done = True
                    #return self.module_Done
                    pass
                else:
                    self.strike()

            if word == 'slid':
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
                if 7 == 7:
                    #self.module_Done = True
                    #return self.module_Done
                    pass
                else:
                    self.strike()
            
            if word == 'bomb':
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
                if 8 == 8:
                    #self.module_Done = True
                    #return self.module_Done
                    pass
                else:
                    self.strike()

            if word == 'left':
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
                if 12 == 12:
                    #self.module_Done = True
                    #return self.module_Done
                    pass
                else:
                    self.strike()


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
# flashing_lights(leds, switches)
    
# setting up the GPIO
GPIO.setmode(GPIO.BCM)
# I/O
GPIO.setup(leds, GPIO.OUT)
# GPIO.setup(test_led, GPIO.OUT)
GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(wires, GPIO.IN)

g1 = morse(leds)
g1.game_start()

