from tkinter import *
import RPi.GPIO as GPIO;
from time import sleep, time;
import multiprocessing;
import random;

DEBUG = True

'''
This module focuses on focusing on a target distance between the ultrasonic sensor
and an object (such as a hand or paper). The defuser must place their object in the
specified range of distances (given by the expert) and press a confirm button.
As each range is confirmed, the next range becomes a smaller range within the previous
one as if the distance were "focusing in on a target spot".
''' 

# the targeting class 
class Module_Targeting:

    def __init__(self, other):

        # required generalized properties 
        self.other = other;
        self.name = "Targeting";
        self.Module_Done = False;
        self.Module_Started = False;

        # constants 
        self.SETTLE_TIME = 200;
        self.CALIBRATIONS = 5;
        self.CALIBRATION_DELAY = 200;
        self.TRIGGER_TIME = 0.00001;
        self.SPEED_OF_SOUND = 343;

        self.correction_factor = 0;

        # GPIO setup
        self.TRIG = 5;
        self.ECHO = 4;
        # GPIO.setmode(GPIO.BCM);
        # GPIO.setup(self.TRIG, GPIO.OUT);
        # GPIO.setup(self.ECHO, GPIO.IN);

        # puzzle properties 
        self.minPhrase = "Set slide to calibrating distance.";
        self.maxPhrase = "Press the Calibrate button."
        self.currentMin = 0.0000;
        self.currentMax = 15.0000;
        self.currentRange = 0;

    # calibrate the sensor by returning a correction factor for later measurements 
    def calibrate(self):

        if DEBUG:
            print("Begin calibrate")

        #print("Calibrating...");

        # prompt the user for an object's known distance
        #print("-Place the sensor a known distance away from an object.");
        #known_distance = float(input("-What is the measured distance (cm)? "));
        known_distance = 8.56;

        # measure the distance to the object with the sensor
        # do this several times and get an average
        #print("-Getting calibration measurements...");
        distance_avg = 0;

        for i in range(self.CALIBRATIONS):
            distance = self.getDistance();
            if (DEBUG):
                print("--Got {}cm".format(distance));
            # keep a running sum
            distance_avg += distance;
            # delay a short time before using the sensor again
            self.other.after(self.CALIBRATION_DELAY);

        # calculate the average of the distances
        distance_avg /= self.CALIBRATIONS;
        if (DEBUG):
            print("--Average is {}cm".format(distance_avg));

        # calculate the correction factor
        correction_factor = known_distance / distance_avg;
        if (DEBUG):
            print("--Correction factor is {}".format(correction_factor));

        # print("Done.");
        # print();

        if DEBUG:
            print(f"finish calibration got {correction_factor}");
        
        self.correction_factor = correction_factor;

        return correction_factor;

    # uses the sensor to calculate the distance to an object
    def getDistance (self):

        if DEBUG:
            print("begin getDistance");





        # GPIO setup
        GPIO.setmode(GPIO.BCM);
        GPIO.setup(self.TRIG, GPIO.OUT);
        GPIO.setup(self.ECHO, GPIO.IN);

        # sensor init 
        # first, allow the sensor to settle for a bit 
        print(f"Waiting for sensor to settle({self.SETTLE_TIME}ms)...");
        if DEBUG:
            print("about to GPIO");
        self.other.pinOutput(self.TRIG, GPIO.LOW);
        if DEBUG:
            print("about to settle time");
        self.other.after(self.SETTLE_TIME);
        if DEBUG:
            print("just after settle time");


        
        # trigger the sensor by setting it high for a short time and then shutting it low
        self.other.pinOutput(self.TRIG, GPIO.HIGH);
        if DEBUG:
            print("GPIO.output 1 done");
        #sleep(self.TRIGGER_TIME);
        sleep(self.TRIGGER_TIME);
        self.other.pinOutput(self.TRIG, GPIO.LOW);

        # wait for the ECHO pin to read high
        # once the ECHO pin is high, the start time is set
        # once the ECHO pin is low, the end time is set
        if DEBUG:
            print("before while")

        # multiprocessing because tk cannot handle while loops
        # and a while loop is required here
        def loop ():
            while (GPIO.input(self.ECHO) == GPIO.LOW):
                start = time();
                if DEBUG:
                    print("in first while")

            while (GPIO.input(self.ECHO) == GPIO.HIGH):
                end = time();
                if DEBUG:
                    print("in second while")

            return (start - end);

        def queue_loop():
            p = multiprocessing.Process(target=loop);
            p.start();


        if DEBUG:
            print("after while")

        # calculate the duration that the ECHO pin was high
        # this is how long the pulse took to get from the sensor to the object -- and back again
        duration = queue_loop();
        # calculate the total distance that the pulse traveled by factoring in the speed of sound (m/s)
        distance = duration * self.SPEED_OF_SOUND;
        # the distance from the sensor to the object is half of the total distance traveled
        distance /= 2;
        # convert from meters to centimeters
        distance *= 100;

        # finally, cleanup the GPIO pins
        print("Done.");
        GPIO.cleanup();

        distance = round(distace, 4);

        if DEBUG:
            print(f"got distance {distance}cm");

        return distance;

    def main(self, started):


        if DEBUG:
            print("begin targeting main");


        # create a dictionary of tuples for button-specific information at each stage
        # ignore the tuple, it is not used anymore, just the first part of the tuple is used 
        buttonFuncs = {"calibrate": ("CALIBRATE", "self.calibrate()"), "range 1": ("CONFIRM\nRANGE 1", "supervisor(1)"), 
                        "range 2": ("CONFIRM\nRANGE 2", "supervisor(2)"), "range 3": ("CONFIRM\nRANGE 3", "supervisor(3)")};

        if DEBUG:
            print(buttonFuncs["calibrate"]);

        # function supervises the functions that are to be called upon button press 
        def supervisor(stage):
            rangeHasWord = [False, False, False];

            # button functions if the 
            if self.currentRange > 0:
                if (not rangeHasWord[stage - 1]):
                    makeRange(stage);
                    rangeHasWord[stage - 1] = True;

                confirm(stage);
            else:
                self.calibrate();
                makeRange(1);

            minWord.configure(text=f"MIN: {self.minPhrase}");
            maxWord.configure(text=f"MAX: {self.maxPhrase}");
            confirmButton.configure(text=buttonFuncs["calibrate"][0], command=supervisor(self.currentRange));

        # calculate the current range 
        def makeRange(stage):

            # phrases that determine the increments 
            words1 = {"THEIR": 0.0451, "I C": 1.0451, 
                      "I DON\'T KNOW": 0.3210, "THEY\'RE": 1.3210, 
                      "WHAT": 0.6124, "I SEE": 1.6124};

            words2 = {"GO BACK": 0.0000, "NOTHING": 1.0000, "I GOT IT":2.0000, 
                      "": 0.1372, "OUT OF RANGE": 1.1372, "READ": 2.1372, 
                      "RED": 0.4444, "UHHH": 1.4444, "BLANK": 2.4444};

            words3 = {"OK": 0.0000, "I GOT A STRIKE": 1.0000, "NOPE": 2.0000,
                      "ARE YOU SURE": 0.1082, "OKAY": 1.1082, "UH HUH": 2.1082, 
                      "LIKE": 0.2169, "YOU DONE?": 1.2169, "CORRECT": 2.2169, 
                      "YOU DONE": 0.3292, "IT\'S BLANK": 1.3292, "READY": 2.3292,
                      "SLOW DOWN": 0.4031, "DON\'T TELL ME": 1.4031, "IT SAYS": 2.4031};

            # list that assigns each dictionary to its range
            rangeOfWords = [words1, words2, words3];

            self.currentMin = self.currentMin + random.choice(list(rangeOfWords[stage - 1].values()));
            self.minPhrase = random.choice(list(rangeOfWords[stage - 1].items()));

            self.currentMax = self.currentMax - random.choice(list(rangeOfWords[stage - 1].values()));
            self.maxPhrase = random.choice(list(rangeOfWords[stage - 1].items()));


        # function to confirm inputs
        def confirm(stage):
            pass;




            



        # clear the frame
        self.other.clearFrame();

        # update started 
        self.Module_Started = True;

        # change location 
        self.other.loc = "Targeting";

        if DEBUG:
            print("pre gui nonsense");
        

        # gui nonsense 

        # grid setup
        self.other.rows = 4
        self.other.cols = 2;

        if DEBUG:
            print("post grid size");

        # necessary button/parts 
        self.other.pause_button(0, 0, 1);
        self.other.back_button(0, 1, 1);
        self.other.countdown(1, 0, 1);
        self.other.health(1, 1, 1);

        if DEBUG:
            print("post necessary buttons")

        # init min and max labels 
        minWord = Label(self.other, bg="white", text=f"MIN: {self.minPhrase}", font=("TexGyreAdventor", 20), relief="groove", borderwidth=5);
        minWord.grid(row=2, column=0, sticky=N+S+E+W, padx=5, pady=5);
        maxWord = Label(self.other, bg="white", text=f"MAX: {self.maxPhrase}", font=("TexGyreAdventor", 20), relief="groove", borderwidth=5);
        maxWord.grid(row=2, column=1, sticky=N+S+E+W, padx=5, pady=5);

        if DEBUG:
            print("post min/max labels");

        # label that shows the current distance
        currentDistLabel = Label(self.other, bg="white", text=f"temp text", font=("TexGyreAdventor", 20), relief="sunken", borderwidth=5);
        currentDistLabel.grid(row=3, column=0, sticky=N+S+E+W, padx=5, pady=5);

        if DEBUG:
            print("post current distance label");

        # button that confirms the distance 
        confirmButton = Button(self.other, bg="chartreuse3", text=buttonFuncs["calibrate"][0], font=("TexGyreAdventor", 20), borderwidth=5, activebackground="DarkOrchid1", command=lambda: supervisor(0));
        if DEBUG:
            print("post confirm button creation");
        confirmButton.grid(row=3, column=1, sticky=N+S+E+W, padx=5, pady=5);        

        if DEBUG:
            print("post current label and button\npre packing");
        
        # configure and pack the grid for display
        for row in range(self.other.rows):
            Grid.rowconfigure(self.other, row, weight=1)
        for col in range(self.other.cols):
            Grid.columnconfigure(self.other, col, weight=1)
        self.other.pack(fill=BOTH, expand=True)

        if DEBUG:
            print("post packing");





#piss = Module_Targeting("temp");
#piss.main(True);
