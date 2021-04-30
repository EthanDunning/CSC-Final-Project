from Game import Game
from tkinter import *
from random import *


class Module_Keypad(Game):
    def __init__(self,other):
        super().__init__()
        self.other = other

        self.name = "Keypad"

        self.other.loc = "Keypad"

        self.Module_Started = False
        self.Module_Done = False

        self.main(self.Module_Started)

    def main(self, started):

        self.other.clearFrame()

        self.other.rows = 6
        self.other.cols = 6
        self.other.pause_button(0, 0, 3)
        self.other.back_button(0, 3, 3)
        self.other.countdown(1, 0, 2)
        self.other.location(1, 2, 2)
        self.other.health(1, 4, 2)

        symbols = {1:"a", 2:"n", 3:"R", 4:"D", 5:".", 6:"C", 7:"b", 8:"e", 9:"c", 10:"d", 11:"S", 12:"l", 13:"N", 14:"f", 15:"-", 16:"A", 17:"o", 18:"J", 19:"M", 20:"E", 21:",", 22:"F", 23:"g", 24:"m", 25:"T", 26:"L", 27:"/"}
        column1 = [1,2,3,13,5,6,7]
        column2 = [8,1,7,22,10,6,11]
        column3 = [12,4,9,14,15,3,10]
        column4 = [16,17,18,5,14,11,19]
        column5 = [20,19,18,21,17,9,23]
        column6 = [16,8,24,25,20,26,27]

        column = choice([column1, column2, column3, column4, column5, column6])
        #print(column1,column2,column3,column4,column5,column6)
        #print(column)
        if started == False:
            
            self.keypad_correct = 0
            
            self.keys = sample(column,4)
            #print(keys)
            self.symbol_1 = symbols[self.keys[0]]
            self.symbol_2 = symbols[self.keys[1]]
            self.symbol_3 = symbols[self.keys[2]]
            self.symbol_4 = symbols[self.keys[3]]

            self.label_1_color = "dim gray"
            self.label_2_color = "dim gray"
            self.label_3_color = "dim gray"
            self.label_4_color = "dim gray"

            self.key_order = []
            for i in column:
                for j in self.keys:
                    if i == j:
                        self.key_order.append(symbols[j])
            #print(self.key_order)
            #print(column)
            self.Module_Started = True

        

        keypad_1 = Button(self.other, bg="lemon chiffon", text=self.symbol_1, font=("Wingdings", 35),
                        borderwidth=10, command=lambda: keypad_check(self.symbol_1))
        keypad_1.grid(row=3, column=0, sticky=N+S+E+W,
                    padx=5, pady=5, columnspan=3)
        
        keypad_2 = Button(self.other, bg="lemon chiffon", text=self.symbol_2, font=("Wingdings", 35),
                        borderwidth=10, command=lambda: keypad_check(self.symbol_2))
        keypad_2.grid(row=3, column=3, sticky=N+S+E+W,
                    padx=5, pady=5, columnspan=3)
                    
        keypad_3 = Button(self.other, bg="lemon chiffon", text=self.symbol_3, font=("Wingdings", 35),
                        borderwidth=10, command=lambda: keypad_check(self.symbol_3))
        keypad_3.grid(row=5, column=0, sticky=N+S+E+W,
                    padx=5, pady=5, columnspan=3)

        keypad_4 = Button(self.other, bg="lemon chiffon", text=self.symbol_4, font=("Wingdings", 35),
                        borderwidth=10, command=lambda: keypad_check(self.symbol_4))
        keypad_4.grid(row=5, column=3, sticky=N+S+E+W,
                    padx=5, pady=5, columnspan=3)

        label_1 = Label(self.other, text="", bg=self.label_1_color,
                      borderwidth=10, relief="ridge")
        label_1.grid(row=2, column=0, sticky=N+S+E+W, padx=5, pady=5, columnspan=3)
        
        label_2 = Label(self.other, text="", bg=self.label_2_color,
                      borderwidth=10, relief="ridge")
        label_2.grid(row=2, column=3, sticky=N+S+E+W, padx=5, pady=5, columnspan=3)

        label_3 = Label(self.other, text="", bg=self.label_3_color,
                      borderwidth=10, relief="ridge")
        label_3.grid(row=4, column=0, sticky=N+S+E+W, padx=5, pady=5, columnspan=3)

        label_4 = Label(self.other, text="", bg=self.label_4_color,
                      borderwidth=10, relief="ridge")
        label_4.grid(row=4, column=3, sticky=N+S+E+W, padx=5, pady=5, columnspan=3)

        for col in range(self.other.cols):
            Grid.columnconfigure(self.other, col, weight=3)
        
        Grid.rowconfigure(self.other, 0, weight=0)
        Grid.rowconfigure(self.other, 1, weight=0)
        Grid.rowconfigure(self.other, 2, weight=5)
        Grid.rowconfigure(self.other, 3, weight=10)
        Grid.rowconfigure(self.other, 4, weight=5)
        Grid.rowconfigure(self.other, 5, weight=10)

        self.other.pack(fill=BOTH, expand=True)

        def keypad_check(input):
            if self.keypad_correct <= 3:
                if input == self.key_order[self.keypad_correct]:
                    self.keypad_correct += 1
                    if input == self.symbol_1:
                        self.label_1_color = "lime green"
                    elif input == self.symbol_2:
                        self.label_2_color = "lime green"
                    elif input == self.symbol_3:
                        self.label_3_color = "lime green"
                    elif input == self.symbol_4:
                        self.label_4_color = "lime green"
                    self.main(self.Module_Started)
                else:
                    self.keypad_correct = 0
                    
                    self.label_1_color = "dim gray"
                    self.label_2_color = "dim gray"
                    self.label_3_color = "dim gray"
                    self.label_4_color = "dim gray"
                    self.main(self.Module_Started)
                    self.other.strike()

        if self.keypad_correct >= 4:
            self.keypad_correct = 4
            self.Module_Done = True
            self.other.MainMenu() 