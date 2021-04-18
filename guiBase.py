from tkinter import *
#import RPi.GPIO as GPIO
from time import *
from datetime import *

# the main GUI
class MainGUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg="white")
        parent.attributes("-fullscreen", False)
        self.mins=5
        self.secs=0
        self.hp=3
        self.maxhp=3
        self.loc = "Home"
        self.start_screen()

    def start_screen(self):

        button = Button(self, bg="red", text="Push to Start", font=("TexGyreAdventor", 25), borderwidth=10, highlightthickness=0, activebackground="blue", command=lambda: self.setupGUI())
        button.grid(row=0, column=0, sticky=N+S+E+W, padx=5, pady=5)

        for row in range(1):
            Grid.rowconfigure(self, row, weight=1)
            for col in range(1):
                Grid.columnconfigure(self, col, weight=1)

        self.pack(fill=BOTH, expand=1)
        

    def setupGUI(self):
        self.mins= 5
        self.secs=0
        self.hp = 3
        self.maxhp = 3
        self.loc = "Home"

        self.countdown(self.mins, self.secs)
        self.after(1000, self.update_timer)
        self.health()
        self.location()

        for row in range(1,3):
            Grid.rowconfigure(self, row, weight=1)
        for col in range(3):
            Grid.columnconfigure(self, col, weight=1)
            
        self.Button1()
        self.Button2()
        self.Button3()
        self.Button4()
        self.Button5()
        self.Button6()
        

        self.pack(fill=BOTH, expand=1)


    def countdown(self, mins, secs):
        mins = str(mins)
        if secs <10:
            secs = f"0{secs}"
        else:
            secs = str(secs)
        
        timer = Label(self, text=f"{mins}:{secs}", bg="white", font=("TexGyreAdventor", 45))
        timer.grid(row=0, column=0, sticky=N+S+E+W)

    def update_timer(self):
        self.after(1000, self.update_timer)
        self.secs -= 1
        if self.secs == -1:
            self.secs = 59
            self.mins -= 1
            if self.mins == -1:
                self.secs = 0
                self.mins = 0
        self.countdown(self.mins, self.secs)
        self.update()
        

    def health(self):
        
        health = Label(self, text=f"{self.hp}/{self.maxhp}", bg="white", font=("TexGyreAdventor", 45))
        health.grid(row=0, column=1, sticky=N+S+E+W, padx=5, pady=5)
        
    def location(self):

        location = Label(self, text=f"{self.loc}", bg="white", font=("TexGyreAdventor", 45))
        location.grid(row=0, column=2, sticky=N+S+E+W, padx=5, pady=5)

    def Button1(self):
        button = Button(self, bg="red", text="Module 1", font=("TexGyreAdventor", 25), borderwidth=10, highlightthickness=0, activebackground="blue", command=lambda: print("pushed"))
        button.grid(row=1, column=0, sticky=N+S+E+W, padx=5, pady=5)
    
    def Button2(self):
        button = Button(self, bg="red", text="Module 2", font=("TexGyreAdventor", 25), borderwidth=10, highlightthickness=0, activebackground="blue", command=lambda: print("pushed"))
        button.grid(row=1, column=1, sticky=N+S+E+W, padx=5, pady=5)
    
    def Button3(self):
        button = Button(self, bg="red", text="Module 3", font=("TexGyreAdventor", 25), borderwidth=10, highlightthickness=0, activebackground="blue", command=lambda: print("pushed"))
        button.grid(row=1, column=2, sticky=N+S+E+W, padx=5, pady=5)
    
    def Button4(self):
        button = Button(self, bg="red", text="Module 4", font=("TexGyreAdventor", 25), borderwidth=10, highlightthickness=0, activebackground="blue", command=lambda: print("pushed"))
        button.grid(row=2, column=0, sticky=N+S+E+W, padx=5, pady=5)
    
    def Button5(self):
        button = Button(self, bg="red", text="Module 5", font=("TexGyreAdventor", 25), borderwidth=10, highlightthickness=0, activebackground="blue", command=lambda: print("pushed"))
        button.grid(row=2, column=1, sticky=N+S+E+W, padx=5, pady=5)
    
    def Button6(self):
        button = Button(self, bg="red", text="Module 6", font=("TexGyreAdventor", 25), borderwidth=10, highlightthickness=0, activebackground="blue", command=lambda: print("pushed"))
        button.grid(row=2, column=2, sticky=N+S+E+W, padx=5, pady=5)
    
    


##############################
# the main part of the program
##############################


# create the window
window = Tk()
# set the window title
window.title("Continue Speaking And Everyone Lives")

## # generate the GUI
p = MainGUI(window)
## # display the GUI and wait for user interaction
p.mainloop()
