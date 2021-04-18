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
        self.maxstrikes = 2
        self.startmins = 5
        self.startsecs = 0
        self.timer_pause = False

        self.mins = self.startmins
        self.secs = self.startsecs
        self.strikes = 0
        self.loc = "Home"
        self.counter = None
        self.rows = 1
        self.cols = 1


         @property
        def timer_pause(self):
            return self._timer_pause
        @timer_pause.setter
        def timer_pause(self, value):
            self._timer_pause = value

        @property
        def maxstrikes(self):
            return self._maxstrikes
        @maxstrikes.setter
        def maxstrikes(self, value):
            self._maxstrikes = value

        @property
        def startmins(self):
            return self._startmins
        @startmins.setter
        def startmins(self, value):
            self._startmins = value
        
        @property
        def startsecs(self):
            return self._startsecs
        @startsecs.setter
        def startsecs(self, value):
            self._startsecs = value
        
        @property
        def mins(self):
            return self._mins
        @mins.setter
        def mins(self, value):
            self._mins = value
        
        @property
        def secs(self):
            return self._secs
        @secs.setter
        def secs(self, value):
            self._secs = value
        
        @property
        def strikes(self):
            return self._strikes
        @strikes.setter
        def strikes(self, value):
            self._strikes = value
        
        @property
        def loc(self):
            return self._loc
        @loc.setter
        def loc(self, value):
            self._locs = value
        
        @property
        def counter(self):
            return self._counter
        @counter.setter
        def counter(self, value):
            self._counter = value
        
        @property
        def rows(self):
            return self._rows
        @rows.setter
        def rows(self, value):
            self._rows = value
        
        @property
        def cols(self):
            return self._cols
        @cols.setter
        def cols(self, value):
            self._cols = value



        self.start_screen()

    def reset(self):
        self.clearFrame()
        self.mins = self.startmins
        self.secs = self.startsecs
        self.strikes = 0
        self.loc = "Home"
        self.counter = None
        self.rows = 1
        self.cols = 1
        self.start_screen()

    def start_screen(self):
        self.clearFrame()
        self.rows = 2
        self.cols = 1
        self.loc = "Home"
        button = Button(self, bg="red", text="Push to Start", font=(
            "TexGyreAdventor", 25), borderwidth=10, activebackground="blue", command=lambda: self.setupGUI())
        button.grid(row=0, column=0, sticky=N+S+E+W, padx=5, pady=5)

        quit = Button(self, bg="dim gray", text="Quit", font=("TexGyreAdventor", 25),
                      borderwidth=10, activebackground="light grey", command=lambda: self.quit())
        quit.grid(row=1, column=0, sticky=N+S+E+W, padx=5, pady=5)

        Grid.rowconfigure(self, 0, weight=3)
        Grid.rowconfigure(self, 1, weight=1)

        Grid.columnconfigure(self, 0, weight=1)

        self.pack(fill=BOTH, expand=1)

    def setupGUI(self):
        self.clearFrame()

        self.rows = 4
        self.cols = 3

        self.pause_button(0, 0, 3)

        self.countdown(self.mins, self.secs, 1, 0, 1)
        self.counter = self.after(1000, self.update_timer)

        self.location(1, 1, 1)
        self.health(1, 2, 1)

        self.Button1(2, 0, 1)
        self.Button2(2, 1, 1)
        self.Button3(2, 2, 1)
        self.Button4(3, 0, 1)
        self.Button5(3, 1, 1)
        self.Button6(3, 2, 1)

        Grid.rowconfigure(self, 0, weight=2)
        Grid.rowconfigure(self, 1, weight=1)

        for row in range(2, self.rows):
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

        self.rows = 3
        self.cols = 1

        resume = Button(self, bg="red", text="Resume", font=("TexGyreAdventor", 25),
                        borderwidth=10, activebackground="blue", command=lambda: self.setupGUI())
        resume.grid(row=0, column=0, sticky=N+S+E+W, padx=5, pady=5)

        reset = Button(self, bg="green", text="Reset", font=("TexGyreAdventor", 25), borderwidth=10, activebackground="forest green", command=lambda: self.reset())
        reset.grid(row=1, column=0, sticky=N+S+E+W, padx=5, pady=5)

        quit = Button(self, bg="dim gray", text="Quit", font=("TexGyreAdventor", 25),
                      borderwidth=10, activebackground="light grey", command=lambda: self.quit())
        quit.grid(row=2, column=0, sticky=N+S+E+W, padx=5, pady=5)

        for row in range(self.rows):
            Grid.rowconfigure(self, row, weight=1)
            for col in range(self.cols):
                Grid.columnconfigure(self, col, weight=1)

        self.pack(fill=BOTH, expand=1)

    def update_timer(self):
        while self.pause==False:
            if self.strikes == 0:
                self.counter = self.after(1000, self.update_timer)
            elif self.strikes == 1:
                self.counter = self.after(750, self.update_timer)
            elif self.strikes == 2:
                self.counter = self.after(500, self.update_timer)

            self.secs -= 1
            if self.secs == -1:
                self.secs = 59
                self.mins -= 1
                if self.mins == -1:
                    self.secs = 0
                    self.mins = 0
            self.countdown(self.mins, self.secs, 1, 0, 1)
            self.update()

    def strike(self):
        self.strikes += 1
        self.health(1, 2, 1)
        if self.strikes == 3:
            self.Game_Over()

    def pause_button(self, x, y, span):
        button = Button(self, bg="gray", text="Pause", font=("TexGyreAdventor", 25),
                        borderwidth=10, activebackground="light grey", command=lambda: self.pause())
        button.grid(row=x, column=y, sticky=N+S+E+W, pady=5, columnspan=span)

    def back_button(self, x, y, span):
        back_button = Button(self, bg="gray", text="Back", font=("TexGyreAdventor", 25),
                             borderwidth=10, activebackground="light grey", command=lambda: self.setupGUI())
        back_button.grid(row=x, column=y, sticky=N+S +
                         E+W, pady=5, columnspan=span)

    def countdown(self, mins, secs, x, y, span):
        if mins < 10:
            mins = f"0{mins}"
        else:
            mins = str(mins)

        if secs < 10:
            secs = f"0{secs}"
        else:
            secs = str(secs)

        timer = Label(self, text=f"{mins}:{secs}",
                      bg="white", font=("TexGyreAdventor", 45))
        timer.grid(row=x, column=y, sticky=N+S+E+W,
                   ipadx=30, pady=5, columnspan=span)

    def health(self, x, y, span):
        health = Label(self, text="[{}{}]".format(
            X*self.strikes, " "*(self.maxstrikes-self.strikes)), bg="white", font=("TexGyreAdventor", 60))
        health.grid(row=x, column=y, sticky=N+S+E+W,
                    ipadx=30, pady=5, columnspan=span)

    def location(self, x, y, span):
        location = Label(self, text=f"{self.loc}",
                         bg="white", font=("TexGyreAdventor", 45))
        location.grid(row=x, column=y, sticky=N+S+E+W,
                      ipadx=30, pady=5, columnspan=span)

    def Button1(self, x, y, span):
        button = Button(self, bg="red", text="The Button", font=("TexGyreAdventor", 25),
                        borderwidth=10, activebackground="blue", command=lambda: self.Module_The_Button())
        button.grid(row=x, column=y, sticky=N+S+E+W,
                    padx=5, pady=5, columnspan=span)

    def Button2(self, x, y, span):
        button = Button(self, bg="red", text="Strike", font=("TexGyreAdventor", 25),
                        borderwidth=10, activebackground="blue", command=lambda: self.strike())
        button.grid(row=x, column=y, sticky=N+S+E+W,
                    padx=5, pady=5, columnspan=span)

    def Button3(self, x, y, span):
        button = Button(self, bg="red", text="Module 3", font=("TexGyreAdventor", 25),
                        borderwidth=10, activebackground="blue", command=lambda: print("pushed 3"))
        button.grid(row=x, column=y, sticky=N+S+E+W,
                    padx=5, pady=5, columnspan=span)

    def Button4(self, x, y, span):
        button = Button(self, bg="red", text="Module 4", font=("TexGyreAdventor", 25),
                        borderwidth=10, activebackground="blue", command=lambda: print("pushed 4"))
        button.grid(row=x, column=y, sticky=N+S+E+W,
                    padx=5, pady=5, columnspan=span)

    def Button5(self, x, y, span):
        button = Button(self, bg="red", text="Module 5", font=("TexGyreAdventor", 25),
                        borderwidth=10, activebackground="blue", command=lambda: print("pushed 5"))
        button.grid(row=x, column=y, sticky=N+S+E+W,
                    padx=5, pady=5, columnspan=span)

    def Button6(self, x, y, span):
        button = Button(self, bg="red", text="Module 6", font=("TexGyreAdventor", 25),
                        borderwidth=10, activebackground="blue", command=lambda: print("pushed 6"))
        button.grid(row=x, column=y, sticky=N+S+E+W,
                    padx=5, pady=5, columnspan=span)

    def Module_The_Button(self):
        self.clearFrame()

        self.rows = 3
        self.cols = 3
        self.loc = "The Button"

        self.pause_button(0, 0, self.cols)
        self.countdown(self.mins, self.secs, 1, 0, 1)
        self.counter = self.after(1000, self.update_timer)

        self.location(1, 1, 1)
        self.health(1, 2, 1)

        button_colors = ["red", "blue", "yellow", "white", "dim gray"]
        button_labels = ["Abort", "Detonate", "Hold", "Press"]
        strip_color = choice(button_colors)
        button_color = choice(button_colors)
        button_label = choice(button_labels)

        button = Label(self, bg=button_color, text=button_label, font=(
            "TexGyreAdventor", 25), borderwidth=10, relief="raised")
        button.grid(row=2, column=0, sticky=N+S+E +
                    W, padx=5, pady=5, columnspan=2)

        strip = Label(self, text="", bg=strip_color,
                      borderwidth=10, relief="ridge")
        strip.grid(row=2, column=(self.cols-1), sticky=N +
                   S+E+W, padx=5, pady=5, columnspan=1)

        for row in range(0, self.rows):
            Grid.rowconfigure(self, row, weight=1)
        Grid.rowconfigure(self, 2, weight=10)

        Grid.columnconfigure(self, 0, weight=5)
        Grid.columnconfigure(self, 1, weight=5)
        Grid.columnconfigure(self, 2, weight=1)

        self.pack(fill=BOTH, expand=1)

    def Game_Over(self):
#       GPIO.cleanup()
        pass


# create the window
window = Tk()
# set the window title
window.title("Continue Speaking And Everyone Lives")
window.geometry("800x400")
# generate the GUI
p = MainGUI(window)
# display the GUI and wait for user interaction
p.mainloop()
