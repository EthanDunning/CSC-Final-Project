
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

class morse_code():
    def __init__():
        self.module_Started = False
        self.module_Done = False
        self.word = False

    def word_select():
        words = [fall, your, slid, bomb, left]
        self.word = random.choice(words)

    def dot(light):
        GPIO.output(lights[light], GPIO.HIGH)
        sleep(0.25)
        GPIO.output(lights[light], GPIO.LOW)
        sleep(0.25)

    def dash(light):
        GPIO.output(lights[light], GPIO.HIGH)
        sleep(0.75)
        GPIO.output(lights[light], GPIO.LOW)
        sleep(0.25)

    def distance():
        # set Trigger to HIGH
        GPIO.output(GPIO_TRIGGER, True)
    
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)
    
        StartTime = time.time()
        StopTime = time.time()
    
        # save StartTime
        while GPIO.input(GPIO_ECHO) == 0:
            StartTime = time.time()
    
        # save time of arrival
        while GPIO.input(GPIO_ECHO) == 1:
            StopTime = time.time()
    
        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
    
        return distance

    @property
    def word():
        return self._word
    @word.setter
    def word(value):
        self._word = value


    def game_start():
        while self.module_Done == False:
            if self.word == fall:
                # F
                dot(0)
                dot(0)
                dash(0)
                dot(0)
                sleep(1)
                # A
                dot(1)
                dash(1)
                sleep(1)
                # L
                dot(2)
                dash(2)
                dot(2)
                dot(2)
                sleep(1)
                # L
                dot(3)
                dash(3)
                dot(3)
                dot(3)
                sleep(1)
                if Distance() == 2:
                    self.module_Done = True
                    return self.module_Done
                else:
                    self.mistakes += 1
            
            if self.word == your:
                # Y
                dash(0)
                dot(0)
                dash(0)
                dash(0)
                sleep(1)
                # O
                dash(1)
                dash(1)
                dash(1)
                sleep(1)
                # U
                dot(2)
                dot(2)
                dash(2)
                sleep(1)
                # R
                dot(3)
                dash(3)
                dot(3)
                sleep(1)
                if Distance() == 4:
                    self.module_Done = True
                    return self.module_Done
                else:
                    self.mistakes += 1

            if self.word == slid:
                # S
                dot(0)
                dot(0)
                dot(0)
                sleep(1)
                # L
                dot(1)
                dash(1)
                dot(1)
                dot(1)
                sleep(1)
                # I
                dot(2)
                dot(2)
                sleep(1)
                # D
                dash(3)
                dot(3)
                dot(3)
                sleep(1)
                if Distance() == 7:
                    self.module_Done = True
                    return self.module_Done
                else:
                    self.mistakes += 1
            
            if self.word == bomb:
                # B
                dash(0)
                dot(0)
                dot(0)
                dot(0)
                sleep(1)
                # O
                dash(1)
                dash(1)
                dash(1)
                sleep(1)
                # M
                dash(2)
                dash(2)
                sleep(1)
                # B
                dash(3)
                dot(3)
                dot(3)
                dot(3)
                sleep(1)
                if Distance() == 8:
                    self.module_Done = True
                    return self.module_Done
                else:
                    self.mistakes += 1

            if self.word == left:
                # L
                dot(0)
                dash(0)
                dot(0)
                dot(0)
                sleep(1)
                # E
                dot(1)
                sleep(1)
                # F
                dot(2)
                dot(2)
                dash(2)
                dot(2)
                sleep(1)
                # T
                dash(3)
                sleep(3)
                if Distance() == 12:
                    self.module_Done = True
                    return self.module_Done
                else:
                    self.mistakes += 1

                
