from tkinter import *
#import RPi.GPIO as GPIO
from random import *
from math import *
from Keypad import *
from The_Button import *

# the main GUI

class MainGUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg="white")
        parent.attributes("-fullscreen", False)
        self.rows=1
        self.cols=1
        self.pack(fill=BOTH, expand=True)
        self.reset()

    def reset(self):
        GPIO.cleanup()
        self.Alive = True
        self.maxstrikes = 2
        self.startmins = IntVar()
        self.startsecs = IntVar()
        self.startmins = 10
        self.startsecs = 0
        self.timer_pause = False
        self.timer = None
        self.mins = IntVar()
        self.secs = IntVar()
        self.time = StringVar()
        self.mins = self.startmins
        self.secs = self.startsecs
        if self.mins < 10:
            if self.secs < 10:
                self.time.set(f"0{self.mins}:0{ceil(self.secs)}")
            else:
                self.time.set(f"0{self.mins}:{ceil(self.secs)}")
        else:
            if self.secs < 10:
                self.time.set(f"{self.mins}:0{ceil(self.secs)}")
            else:
                self.time.set(f"{self.mins}:{ceil(self.secs)}")

        self.strikes = 0
        self.hp = StringVar()
        self.hp.set("[{}{}]".format("X"*self.strikes, " "*(self.maxstrikes-self.strikes)))
        self.loc = "Home"
        self.counter = None

        self.Module_1_Started = False
        self.Module_2_Started = False
        self.Module_3_Started = False
        self.Module_4_Started = False
        self.Module_5_Started = False
        self.Module_6_Started = False
        self.Module_1_Done = False
        self.Module_2_Done = False
        self.Module_3_Done = False
        self.Module_4_Done = False
        self.Module_5_Done = False
        self.Module_6_Done = False
        self.Modules = [self.Module_1_Done, self.Module_2_Done, self.Module_3_Done, self.Module_4_Done, self.Module_5_Done, self.Module_6_Done]

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

        self.Module_1 = Module_The_Button(self)
        self.Module_2 = None
        self.Module_3 = None
        self.Module_4 = Module_Keypad(self)
        self.Module_5 = None
        self.Module_6 = None

        self.start_screen()

    def start_screen(self):
        GPIO.cleanup()
        self.clearFrame()
        self.rows = 2
        self.cols = 1
        self.loc = "Home"
        button = Button(self, bg="red", text="Push to Start", font=(
            "TexGyreAdventor", 25), borderwidth=10, activebackground="blue", command=lambda: self.MainMenu())
        button.grid(row=0, column=0, sticky=N+S+E+W, padx=5, pady=5)

        quit = Button(self, bg="dim gray", text="Quit", font=("TexGyreAdventor", 25),
                      borderwidth=10, activebackground="light grey", command=lambda: self.quit())
        quit.grid(row=1, column=0, sticky=N+S+E+W, padx=5, pady=5)

        Grid.rowconfigure(self, 0, weight=3)
        Grid.rowconfigure(self, 1, weight=1)

        Grid.columnconfigure(self, 0, weight=1)

        self.pack(fill=BOTH, expand=True)

    def MainMenu(self):
        GPIO.cleanup()
        self.clearFrame()
        self.loc="Home"
        self.rows = 4
        self.cols = 3
        self.pause_button(0, 0, 3)
        self.countdown(1, 0, 1)
        self.location(1, 1, 1)
        self.health(1, 2, 1)
        self.Button1(2, 0, 1)
        self.Button2(2, 1, 1)
        self.Button3(2, 2, 1)
        self.Button4(3, 0, 1)
        self.Button5(3, 1, 1)
        self.Button6(3, 2, 1)

        Grid.rowconfigure(self, 0, weight=0)
        Grid.rowconfigure(self, 1, weight=0)

        for row in range(2, self.rows):
            Grid.rowconfigure(self, row, weight=3)
        for col in range(self.cols):
            Grid.columnconfigure(self, col, weight=3)

        if (self.Module_1_Done==True and self.Module_2_Done==True and self.Module_3_Done==True and self.Module_4_Done==True and self.Module_5_Done==True and self.Module_6_Done==True):
            self.Game_Win()

        self.pack(fill=BOTH, expand=True)

    def clearFrame(self):
        GPIO.cleanup()
        if self.counter is not None:
            self.after_cancel(self.counter)
            self.counter = None
        # destroy all widgets from frame
        for widget in self.winfo_children():
            widget.destroy()

        for row in range(self.rows):
            Grid.rowconfigure(self, row, weight=0)
            
        for col in range(self.cols):
            Grid.columnconfigure(self, col, weight=0)

        self.pack_forget()
            
    def pause(self):
        self.clearFrame()
        self.rows = 3
        self.cols = 1

        resume = Button(self, bg="red", text="Resume", font=("TexGyreAdventor", 25), borderwidth=10, activebackground="blue", command=lambda: self.resume())
        resume.grid(row=0, column=0, sticky=N+S+E+W, padx=5, pady=5, columnspan=1)

        reset = Button(self, bg="green", text="Reset", font=("TexGyreAdventor", 25), borderwidth=10, activebackground="forest green", command=lambda: self.reset())
        reset.grid(row=1, column=0, sticky=N+S+E+W, padx=5, pady=5, columnspan=1)

        _quit = Button(self, bg="dim gray", text="Quit", font=("TexGyreAdventor", 25),
                      borderwidth=10, activebackground="light grey", command=lambda: self.quit())
        _quit.grid(row=2, column=0, sticky=N+S+E+W, padx=5, pady=5, columnspan=1)

        Grid.rowconfigure(self, 0, weight=1)
        Grid.rowconfigure(self, 1, weight=1)
        Grid.rowconfigure(self, 2, weight=1)
        Grid.columnconfigure(self, 0, weight=1)

        self.pack(fill=BOTH, expand=True)

    def resume(self):
        if self.loc == "Home":
            self.MainMenu()
        elif self.loc == "The Button":
            self.Module_The_Button(self.Module_1_Started)
        elif self.loc == "Keypad":
            self.Module_Keypad(self.Module_4_Started)

    def update_timer(self):
        tick = 500
        if self.timer_pause==False:
            
            if self.strikes == 0:
                self.counter = self.after(tick, self.update_timer)
            elif self.strikes == 1:
                self.counter = self.after(int((tick/4)*3), self.update_timer)
            elif self.strikes == 2:
                self.counter = self.after(int(tick/2), self.update_timer)
            else:
                self.counter = self.after(int(tick/2), self.update_timer)

            self.secs -= (tick/1000)
            if self.secs < 0:
                self.secs = 59
                self.mins -= 1
                if self.mins < 0:
                    self.secs = 0
                    self.mins = 0
                    self.Game_Over()

        if self.mins < 10:
            if ceil(self.secs) < 10:
                self.time.set(f"0{self.mins}:0{ceil(self.secs)}")
            else:
                self.time.set(f"0{self.mins}:{ceil(self.secs)}")
        else:
            if self.secs < 10:
                self.time.set(f"{self.mins}:0{ceil(self.secs)}")
            else:
                self.time.set(f"{self.mins}:{ceil(self.secs)}")

        if (self.mins < 1) and (self.secs <= 30):
            if float(self.secs).is_integer()==False:
               self.timer.config(fg="white")
            else:
                self.timer.config(fg="red")
        else:
            if self.Alive==True:
                pass
        
        self.update()

    def countdown(self, x, y, span):
        self.timer = Label(self, textvariable=self.time,
                      bg="white", font=("TexGyreAdventor", 35), relief="groove", borderwidth=10)
        self.timer.grid(row=x, column=y, sticky=N+S+E+W,
                   padx=5, pady=5, columnspan=span)
        if self.counter is None:
            self.counter = self.after(1000, self.update_timer)
        
    def strike(self):
        self.strikes += 1
        self.hp.set("[{}{}]".format("X"*self.strikes, " "*(self.maxstrikes-self.strikes)))
        if self.strikes > self.maxstrikes:
            self.Game_Over()
        self.update()

    def health(self, x, y, span):
        self.healthlabel = Label(self, textvariable=self.hp, bg="white", font=("TexGyreAdventor", 35), relief="groove", borderwidth=10)
        self.healthlabel.grid(row=x, column=y, sticky=N+S+E+W, padx=5,
                    pady=5, columnspan=span)

    def pause_button(self, x, y, span):
        button = Button(self, bg="gray", text="Pause", font=("TexGyreAdventor", 25),
                        borderwidth=10, activebackground="light grey", command=lambda: self.pause())
        button.grid(row=x, column=y, sticky=N+S+E+W, pady=5, columnspan=span)

    def back_button(self, x, y, span):
        back_button = Button(self, bg="gray", text="Back", font=("TexGyreAdventor", 25),
                             borderwidth=10, activebackground="light grey", command=lambda: self.MainMenu())
        back_button.grid(row=x, column=y, sticky=N+S+E+W, pady=5, columnspan=span)

    def location(self, x, y, span):
        location = Label(self, text=f"{self.loc}",
                         bg="white", font=("TexGyreAdventor", 35), relief="groove", borderwidth=10)
        location.grid(row=x, column=y, sticky=N+S+E+W,
                      padx=5, pady=5, columnspan=span)

    def Button1(self, x, y, span):
        try:
            if self.Module_1.Module_Done == True:
                button_color = "lime green"
                background = "lime green"
            else:
                button_color = "tomato"
                background = "slate blue"
        except:
            button_color = "tomato"
            background = "slate blue"

        if self.Module_1 == None:
            button_color = "lime green"
            background = "lime green"
            self.Module_1_Done = True

        try:
            button = Button(self, bg=button_color, text=self.Module_1.name, font=("TexGyreAdventor", 25),
                            borderwidth=10, activebackground=background, command=lambda: self.Module_Setup("Module_1"))
        except:
            button = Button(self, bg=button_color, text="None", font=("TexGyreAdventor", 25),
                            borderwidth=10, activebackground=background, command=lambda: self.Module_Setup("Module_1"))
        button.grid(row=x, column=y, sticky=N+S+E+W,
                    padx=5, pady=5, columnspan=span)

    def Button2(self, x, y, span):
        try:
            if self.Module_2.Module_Done == True:
                button_color = "lime green"
                background = "lime green"
            else:
                button_color = "tomato"
                background = "slate blue"
        except:
            button_color = "tomato"
            background = "slate blue"

        if self.Module_2 == None:
            button_color = "lime green"
            background = "lime green"
            self.Module_2_Done = True

        try:
            button = Button(self, bg=button_color, text=self.Module_2.name, font=("TexGyreAdventor", 25),
                            borderwidth=10, activebackground=background, command=lambda: self.Module_Setup("Module_2"))
        except:
            button = Button(self, bg=button_color, text="Strike", font=("TexGyreAdventor", 25),
                            borderwidth=10, activebackground=background, command=lambda: self.strike())
        button.grid(row=x, column=y, sticky=N+S+E+W,
                    padx=5, pady=5, columnspan=span)

    def Button3(self, x, y, span):
        try:
            if self.Module_3.Module_Done == True:
                button_color = "lime green"
                background = "lime green"
            else:
                button_color = "tomato"
                background = "slate blue"
        except:
            button_color = "tomato"
            background = "slate blue"

        if self.Module_3 == None:
            button_color = "lime green"
            background = "lime green"
            self.Module_3_Done = True

        try:
            button = Button(self, bg=button_color, text=self.Module_3.name, font=("TexGyreAdventor", 25),
                            borderwidth=10, activebackground=background, command=lambda: self.Module_Setup("Module_3"))
        except:
            button = Button(self, bg=button_color, text="None", font=("TexGyreAdventor", 25),
                            borderwidth=10, activebackground=background, command=lambda: self.Module_Setup("Module_3"))
        button.grid(row=x, column=y, sticky=N+S+E+W,
                    padx=5, pady=5, columnspan=span)

    def Button4(self, x, y, span):
        try:
            if self.Module_4.Module_Done == True:
                button_color = "lime green"
                background = "lime green"
            else:
                button_color = "tomato"
                background = "slate blue"
        except:
            button_color = "tomato"
            background = "slate blue"

        if self.Module_4 == None:
            button_color = "lime green"
            background = "lime green"
            self.Module_4_Done = True

        try:
            button = Button(self, bg=button_color, text=self.Module_4.name, font=("TexGyreAdventor", 25),
                            borderwidth=10, activebackground=background, command=lambda: self.Module_Setup("Module_4"))
        except:
            button = Button(self, bg=button_color, text="None", font=("TexGyreAdventor", 25),
                            borderwidth=10, activebackground=background, command=lambda: self.Module_Setup("Module_4"))
        button.grid(row=x, column=y, sticky=N+S+E+W,
                    padx=5, pady=5, columnspan=span)

    def Button5(self, x, y, span):
        try:
            if self.Module_5.Module_Done == True:
                button_color = "lime green"
                background = "lime green"
            else:
                button_color = "tomato"
                background = "slate blue"
        except:
            button_color = "tomato"
            background = "slate blue"

        if self.Module_5 == None:
            button_color = "lime green"
            background = "lime green"
            self.Module_5_Done = True

        try:
            button = Button(self, bg=button_color, text=self.Module_5.name, font=("TexGyreAdventor", 25),
                            borderwidth=10, activebackground=background, command=lambda: self.Module_Setup("Module_5"))
        except:
            button = Button(self, bg=button_color, text="None", font=("TexGyreAdventor", 25),
                            borderwidth=10, activebackground=background, command=lambda: self.Module_Setup("Module_5"))
        button.grid(row=x, column=y, sticky=N+S+E+W,
                    padx=5, pady=5, columnspan=span)

    def Button6(self, x, y, span):
        try:
            if self.Module_6.Module_Done == True:
                button_color = "lime green"
                background = "lime green"
            else:
                button_color = "tomato"
                background = "slate blue"
        except:
            button_color = "tomato"
            background = "slate blue"

        if self.Module_6 == None:
            button_color = "lime green"
            background = "lime green"
            self.Module_6_Done = True

        try:
            button = Button(self, bg=button_color, text=self.Module_6.name, font=("TexGyreAdventor", 25),
                            borderwidth=10, activebackground=background, command=lambda: self.Module_Setup("Module_6"))
        except:
            button = Button(self, bg=button_color, text="None", font=("TexGyreAdventor", 25),
                            borderwidth=10, activebackground=background, command=lambda: self.Module_Setup("Module_6"))
        button.grid(row=x, column=y, sticky=N+S+E+W,
                    padx=5, pady=5, columnspan=span)

    
    def Module_Setup(self, Button):
        try:
            if Button == "Module_1":
                if self.Module_1_Started == False:
                    self.Module_1_Started = True
                self.Module_1.main(self.Module_1_Started)

            elif Button == "Module_2":
                if self.Module_2_Started == False:
                    self.Module_2_Started = True
                self.Module_2.main(self.Module_2_Started)

            elif Button == "Module_3":
                if self.Module_3_Started == False:
                    self.Module_3_Started = True
                self.Module_3.main(self.Module_3_Started)

            elif Button == "Module_4":
                if self.Module_4_Started == False:
                    self.Module_4_Started = True
                self.Module_4.main(self.Module_4_Started)
                    
            elif Button == "Module_5":
                if self.Module_5_Started == False:
                    self.Module_5_Started = True
                self.Module_5.main(self.Module_5_Started)

            elif Button == "Module_6":
                if self.Module_6_Started == False:
                    self.Module_6_Started = True
                self.Module_6.main(self.Module_6_Started)
        except:
            pass

    def Game_Over(self):
        GPIO.cleanup()
        self.Alive = False
        self.clearFrame()
        self.rows = 3
        self.cols = 3

        Time_Left = Label(self, text=f"Time Left:",
                         bg="white", font=("TexGyreAdventor", 35), relief="groove", borderwidth=10)
        Time_Left.grid(row=0, column=0, sticky=N+S+E+W,
                      padx=5, pady=5, columnspan=1, rowspan=1)

        Lose = Label(self, text=f"You Lose!",
                         bg="white", font=("TexGyreAdventor", 35), relief="groove", borderwidth=10)
        Lose.grid(row=0, column=1, sticky=N+S+E+W,
                      padx=5, pady=5, columnspan=1, rowspan=2)

        Strikes = Label(self, text=f"Strikes:",
                         bg="white", font=("TexGyreAdventor", 35), relief="groove", borderwidth=10)
        Strikes.grid(row=0, column=2, sticky=N+S+E+W,
                      padx=5, pady=5, columnspan=1, rowspan=1)
        
        self.countdown(1, 0, 1)
        self.health(1, 2, 1)

        start_over = Button(self, bg="red", text="Start Over", font=(
            "TexGyreAdventor", 25), borderwidth=10, activebackground="blue", command=lambda: self.reset())
        start_over.grid(row=2, column=0, sticky=N+S+E+W, padx=5, pady=5, columnspan=3)

        quit = Button(self, bg="dim gray", text="Quit", font=("TexGyreAdventor", 25),
                      borderwidth=10, activebackground="light grey", command=lambda: self.quit())
        quit.grid(row=3, column=0, sticky=N+S+E+W, padx=5, pady=5, columnspan=3)

        for row in range(self.rows):
            Grid.rowconfigure(self, row, weight=1)

        Grid.columnconfigure(self, 0, weight=1)
        Grid.columnconfigure(self, 1, weight=5)
        Grid.columnconfigure(self, 2, weight=1)


        self.pack(fill=BOTH, expand=True)

    def Game_Win(self):
        GPIO.cleanup()
        self.clearFrame()
        self.rows = 3
        self.cols = 3

        Time_Left = Label(self, text=f"Time Left:",
                         bg="white", font=("TexGyreAdventor", 35), relief="groove", borderwidth=10)
        Time_Left.grid(row=0, column=0, sticky=N+S+E+W,
                      padx=5, pady=5, columnspan=1, rowspan=1)

        Win = Label(self, text=f"You Win!",
                         bg="white", font=("TexGyreAdventor", 35), relief="groove", borderwidth=10)
        Win.grid(row=0, column=1, sticky=N+S+E+W,
                      padx=5, pady=5, columnspan=1, rowspan=2)

        Strikes = Label(self, text=f"Strikes:",
                         bg="white", font=("TexGyreAdventor", 35), relief="groove", borderwidth=10)
        Strikes.grid(row=0, column=2, sticky=N+S+E+W,
                      padx=5, pady=5, columnspan=1, rowspan=1)

        self.countdown(1, 0, 1)
        self.health(1, 2, 1)

        start_over = Button(self, bg="red", text="Start Over", font=(
            "TexGyreAdventor", 25), borderwidth=10, activebackground="blue", command=lambda: self.reset())
        start_over.grid(row=2, column=0, sticky=N+S+E+W, padx=5, pady=5, columnspan=3)

        quit = Button(self, bg="dim gray", text="Quit", font=("TexGyreAdventor", 25),
                      borderwidth=10, activebackground="light grey", command=lambda: self.quit())
        quit.grid(row=3, column=0, sticky=N+S+E+W, padx=5, pady=5, columnspan=3)

        for row in range(self.rows):
            Grid.rowconfigure(self, row, weight=1)

        Grid.columnconfigure(self, 0, weight=1)
        Grid.columnconfigure(self, 1, weight=5)
        Grid.columnconfigure(self, 2, weight=1)

        self.pack(fill=BOTH, expand=True)



# create the window
window = Tk()
# set the window title
window.title("Continue Speaking And Everyone Lives")
window.geometry("800x400")
# generate the GUI
p = MainGUI(window)
# display the GUI and wait for user interaction
p.mainloop()
