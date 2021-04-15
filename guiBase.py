#################################################################
# Name:
# Date:
# Description:
#################################################################
from tkinter import *
#import RPi.GPIO as GPIO
import time

# the main GUI
class MainGUI(Frame):
    # the constructor
    def __init__(self, parent):
        Frame.__init__(self, parent, bg="white")
##        parent.attributes('-fullscreen', True)
        self.setupGUI()
    # sets up the GUI
    def setupGUI(self):
        self.display = Label(self, text="", anchor=E, bg="white", height=2, width=15, font=("TexGyreAdventor", 50))
        self.display.grid(row=0, column=0, columnspan=4,rowspan=4, sticky=E+W+N+S)
        for row in range(3):
            Grid.rowconfigure(self, row, weight=1)
        for col in range(3):
            Grid.columnconfigure(self, col, weight=1)
            
        # pack the GUI
        self.pack(fill=BOTH, expand=1)
        for i in range(3):
            for j in range(3):
                img = PhotoImage(file="sub.gif")
                button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0,
                    activebackground="white", command=lambda: self.process("test{}".format(i+j)))
                button.image = img
                button.grid(row=i, column=j, sticky=N+S+E+W)

##############################
# the main part of the program
##############################
# create the window
window = Tk()
# set the window title
window.title("The Reckoner")
# generate the GUI
p = MainGUI(window)
# display the GUI and wait for user interaction
window.mainloop()
