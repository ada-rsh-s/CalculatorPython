import math
from tkinter import *


class calc:
    def getandreplace(self):
        self.newtext = self.e.get().replace('x', '*')

    def equals(self):
        self.getandreplace()
        try:
            self.value = eval(self.newtext)
        except (SyntaxError, ZeroDivisionError):
            self.e.delete(0, END)
            self.e.insert(0, 'Invalid Input!')
        else:
            self.e.delete(0, END)
            self.e.insert(0, self.value)

    def squareroot(self):
        self.getandreplace()
        try:
            self.value = eval(self.newtext)
            if float(self.newtext) < 0:
                raise ValueError
            self.e.delete(0, END)
            self.e.insert(0, math.sqrt(self.value))
        except (SyntaxError, ValueError):
            self.e.delete(0, END)
            self.e.insert(0, 'Invalid Input!')

    def clearall(self):
        self.e.delete(0, END)

    def clearnow(self):
        self.e.delete(0, END)
        self.e.insert(0, self.e.get()[:-1])

    def action(self, argi):
        self.e.insert(END, argi)

    def create_button(self, window, text, command, x, y, w=90, h=70):
        Button(window, text=text, font=("Times New Roman bold", 16), fg='black', bg='#9da39d',
               command=command, cursor="hand2").place(x=x, y=y, width=w, height=h)

    def __init__(self, window):
        window.geometry("526x520+{}+{}".format(int(window.winfo_screenwidth() / 2.25), int(window.winfo_screenheight() / 2.7)))
        window.title("CALCULATOR")
        window.configure(bg="#A37B5C")
        window.resizable(0, 0)

        self.e = Entry(window, justify=RIGHT, bg="light grey", fg="black", font=("Times New Roman bold", 25), relief="sunken")
        self.e.configure(highlightbackground="red", borderwidth=8)
        self.e.grid(row=0, column=0, ipady=10, ipadx=65, padx=18, pady=20)

        button_config = [
            ("AC", self.clearall, 20, 110, 150, 60), ("CE", self.clearnow, 180, 110, 150, 60),
            ("7", lambda: self.action('7'), 20, 180), ("8", lambda: self.action('8'), 130, 180),
            ("9", lambda: self.action('9'), 240, 180), ("4", lambda: self.action('4'), 20, 262),
            ("5", lambda: self.action('5'), 130, 262), ("6", lambda: self.action('6'), 240, 262),
            ("1", lambda: self.action('1'), 20, 344), ("2", lambda: self.action('2'), 130, 344),
            ("3", lambda: self.action('3'), 240, 344), ("0", lambda: self.action('0'), 20, 426),
            ("00", lambda: self.action('00'), 130, 426), (".", lambda: self.action('.'), 240, 426),
            ("+", lambda: self.action('+'), 345, 262, 60, 153), ("=", self.equals, 345, 428, 162, 70),
            ("-", lambda: self.action('-'), 345, 110, 60, 140), ("/", lambda: self.action('/'), 419, 344, 87, 70),
            ("*", lambda: self.action('*'), 419, 262, 87, 70), ("π", lambda: self.action('3.14'), 419, 110, 87, 60),
            ("√", self.squareroot, 419, 180, 87, 70)
        ]

        for config in button_config:
            self.create_button(window, *config)


window = Tk()
calc(window)
window.mainloop()
