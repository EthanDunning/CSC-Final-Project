from tkinter import *
import RPi.GPIO as GPIO;
from time import sleep, time;

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
        self.SETTLE_TIME = 2;
        self.CALIBRATIONS = 5;
        self.CALIBRATION_DELAY = 200;
        self.TRIGGER_TIME = 0.01;
        self.SPEED_OF_SOUND = 343;

        self.correction_factor = 0;

        # GPIO setup
        GPIO.setmode(GPIO.BCM);
        self.TRIG = 5;
        self.ECHO = 4;
        GPIO.setup(self.TRIG, GPIO.OUT);
        GPIO.setup(self.ECHO, GPIO.IN);

    # calibrate the sensor by returning a correction factor for later measurements 
    def calibrate(self):

        #print("Calibrating...");

        # prompt the user for an object's known distance
        #print("-Place the sensor a known distance away from an object.");
        #known_distance = float(input("-What is the measured distance (cm)? "));
        known_distance = 7.62;

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

        print("Done.");
        print();
        
        return correction_factor;

    # uses the sensor to calculate the distance to an object
    def getDistance (self):
        # trigger the sensor by setting it high for a short time and then shutting it low
        GPIO.output(self.TRIG, GPIO.HIGH);
        #sleep(self.TRIGGER_TIME);
        self.other.after(self.TRIGGER_TIME, GPIO.output(self.TRIG, GPIO.LOW));

        # wait for the ECHO pin to read high
        # once the ECHO pin is high, the start time is set
        # once the ECHO pin is low, the end time is set
        while (GPIO.input(self.ECHO) == GPIO.LOW):
            start = time();
        while (GPIO.input(self.ECHO) == GPIO.HIGH):
            end = time();

        # calculate the duration that the ECHO pin was high
        # this is how long the pulse took to get from the sensor to the object -- and back again
        duration = end - start;
        # calculate the total distance that the pulse traveled by factoring in the speed of sound (m/s)
        distance = duration * self.SPEED_OF_SOUND;
        # the distance from the sensor to the object is half of the total distance traveled
        distance /= 2;
        # convert from meters to centimeters
        distance *= 100;

        return distance;

    def main(self, started):

        # clear the frame
        self.other.clearFrame();

        # update started 
        self.Module_Started = True;

        # first, allow the sensor to settle for a bit 
        print(f"Waiting for sensor to settle({self.SETTLE_TIME}ms)...");
        if DEBUG:
            print("about to GPIO");
        GPIO.output(self.TRIG, GPIO.LOW);
        if DEBUG:
            print("about to settle time");
        self.other.after(self.SETTLE_TIME);
        if DEBUG:
            print("just after settle time");

        # next, calibrate the sensor 
        self.correction_factor = self.calibrate();

        # then, measure
        input("Press enter to begin...");
        print("Getting measurements:");

        while (True):
            # get the distance to an object and correct it with the correction factor
            print("-Measuring...");
            distance = self.getDistance() * self.correction_factor;
            #sleep(1);

            # and round to four decimal places 
            self.other.after(1000, distance = round(distance, 4));

            # display the distance calculated 
            print(f"--Distance measured: {distance}cm");

            # prompt for another measurement 
            i = input("--Get another measurement (Y/N)? ");
            # stop measuring if desired 
            i = i.lower();
            if (not i in ["y", "yes", ""]):
                break;

        # finally, cleanup the GPIO pins
        print("Done.");
        GPIO.cleanup();

#piss = Module_Targeting("temp");
#piss.main(True);
