from tkinter import *
#import RPi.GPIO as GPIO
from time import *
from datetime import *
from random import *

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
        self.rows = None
        self.cols = None
        self.counter = None
        self.start_screen()

    def start_screen(self):
        self.rows = 1
        self.cols = 1
        button = Button(self, bg="red", text="Push to Start", font=("TexGyreAdventor", 25), borderwidth=10, highlightthickness=0, activebackground="blue", command=lambda: self.setupGUI())
        button.grid(row=0, column=0, sticky=N+S+E+W, padx=5, pady=5)

        for row in range(self.rows):
            Grid.rowconfigure(self, row, weight=1)
            for col in range(self.cols):
                Grid.columnconfigure(self, col, weight=1)

        self.pack(fill=BOTH, expand=1)
        

    def setupGUI(self):
        self.clearFrame()
        self.rows = 4
        self.cols = 3

        self.countdown(self.mins, self.secs)
        self.counter = self.after(1000, self.update_timer)
        self.health()
        self.location()
        self.pause_button()
        
        self.Button1()
        self.Button2()
        self.Button3()
        self.Button4()
        self.Button5()
        self.Button6()

        for row in range(2):
            Grid.rowconfigure(self, row, weight=2)

        for row in range(2,self.rows):
            Grid.rowconfigure(self, row, weight=3)
        for col in range(self.cols):
            Grid.columnconfigure(self, col, weight=3)

        self.pack(fill=BOTH, expand=1)

    def clearFrame(self):
        if self.counter is not None:
            self.after_cancel(self.counter)
            self.counter = None
        # destroy all widgets from frame
        for widget in self.winfo_children():
            widget.destroy()

        self.pack_forget()

        for row in range(self.rows):
            Grid.rowconfigure(self, row, weight=0)
            for col in range(self.cols):
                Grid.columnconfigure(self, col, weight=0)

    def pause(self):
        self.clearFrame()
        
        self.rows = 2
        self.cols = 1
        resume = Button(self, bg="red", text="Resume", font=("TexGyreAdventor", 25), borderwidth=10, highlightthickness=0, activebackground="blue", command=lambda: self.setupGUI())
        resume.grid(row=0, column=0, sticky=N+S+E+W, padx=5, pady=5)

        quit = Button(self, bg="red", text="Quit", font=("TexGyreAdventor", 25), borderwidth=10, highlightthickness=0, activebackground="blue", command=lambda: self.quit())
        quit.grid(row=1, column=0, sticky=N+S+E+W, padx=5, pady=5)

        for row in range(self.rows):
            Grid.rowconfigure(self, row, weight=1)
            for col in range(self.cols):
                Grid.columnconfigure(self, col, weight=1)

        self.pack(fill=BOTH, expand=1)

    def update_timer(self):
        self.counter = self.after(1000, self.update_timer)
        self.secs -= 1
        if self.secs == -1:
            self.secs = 59
            self.mins -= 1
            if self.mins == -1:
                self.secs = 0
                self.mins = 0
        self.countdown(self.mins, self.secs)
        self.update()

    def pause_button(self):
        button = Button(self, bg="gray", text="Pause", font=("TexGyreAdventor", 25), borderwidth=10, highlightthickness=0, activebackground="light grey", command=lambda: self.pause())
        button.grid(row=0, column=0, sticky=N+S+E+W, pady=5, columnspan=3)

    def countdown(self, mins, secs):
        mins = str(mins)
        if secs <10:
            secs = f"0{secs}"
        else:
            secs = str(secs)
        
        timer = Label(self, text=f"{mins}:{secs}", bg="white", font=("TexGyreAdventor",45))
        timer.grid(row=1, column=0, sticky=N+S+E+W, ipadx=30, pady=5)    

    def health(self):
        health = Label(self, text=f"{self.hp}/{self.maxhp}", bg="white", font=("TexGyreAdventor", 45))
        health.grid(row=1, column=1, sticky=N+S+E+W, ipadx=30, pady=5)
        
    def location(self):
        location = Label(self, text=f"{self.loc}", bg="white", font=("TexGyreAdventor", 45))
        location.grid(row=1, column=2, sticky=N+S+E+W, ipadx=30, pady=5)

    def Button1(self):
        button = Button(self, bg="red", text="The Button", font=("TexGyreAdventor", 25), borderwidth=10, highlightthickness=0, activebackground="blue", command=lambda: self.Module_Button())
        button.grid(row=2, column=0, sticky=N+S+E+W, padx=5, pady=5)
    
    def Button2(self):
        button = Button(self, bg="red", text="Module 2", font=("TexGyreAdventor", 25), borderwidth=10, highlightthickness=0, activebackground="blue", command=lambda: print("pushed 2"))
        button.grid(row=2, column=1, sticky=N+S+E+W, padx=5, pady=5)
    
    def Button3(self):
        button = Button(self, bg="red", text="Module 3", font=("TexGyreAdventor", 25), borderwidth=10, highlightthickness=0, activebackground="blue", command=lambda: print("pushed 3"))
        button.grid(row=2, column=2, sticky=N+S+E+W, padx=5, pady=5)
    
    def Button4(self):
        button = Button(self, bg="red", text="Module 4", font=("TexGyreAdventor", 25), borderwidth=10, highlightthickness=0, activebackground="blue", command=lambda: print("pushed 4"))
        button.grid(row=3, column=0, sticky=N+S+E+W, padx=5, pady=5)
    
    def Button5(self):
        button = Button(self, bg="red", text="Module 5", font=("TexGyreAdventor", 25), borderwidth=10, highlightthickness=0, activebackground="blue", command=lambda: print("pushed 5"))
        button.grid(row=3, column=1, sticky=N+S+E+W, padx=5, pady=5)
    
    def Button6(self):
        button = Button(self, bg="red", text="Module 6", font=("TexGyreAdventor", 25), borderwidth=10, highlightthickness=0, activebackground="blue", command=lambda: print("pushed 6"))
        button.grid(row=3, column=2, sticky=N+S+E+W, padx=5, pady=5)
    
    def Module_Button(self):
        self.clearFrame()

        self.rows = 1
        self.cols = 2
        button_colors = ["red", "blue", "yellow", "white", "dim gray"]
        button_labels = ["Abort", "Detonate", "Hold", "Press"]
        strip_color = choice(button_colors)
        button_color = choice(button_colors)
        button_label = choice(button_labels)

        button = Button(self, bg=button_color, text=button_label, font=("TexGyreAdventor", 25), borderwidth=10, highlightthickness=0, activebackground=button_color)

        button.grid(row=0, column=0, sticky=N+S+E+W, padx=15, pady=15)

        strip = Label(self, text="", bg=strip_color, borderwidth=10, relief="ridge")
        strip.grid(row=0, column=1, sticky=N+S+E+W, padx=15, pady=15)

        Grid.rowconfigure(self, 0, weight=1)
        Grid.columnconfigure(self, 0, weight=10)
        Grid.columnconfigure(self, 1, weight=1)

        self.pack(fill=BOTH, expand=1)




# create the window
window = Tk()
# set the window title
window.title("Continue Speaking And Everyone Lives")
window.geometry("800x400")
## # generate the GUI
p = MainGUI(window)
## # display the GUI and wait for user interaction
p.mainloop()
