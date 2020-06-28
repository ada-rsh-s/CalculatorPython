import math
from tkinter import *


class calc:
    def getandreplace(self):

        self.expression = self.e.get()
        self.newtext = self.expression.replace('/', '/')
        self.newtext = self.newtext.replace('x', '*')

    def equals(self):
        self.getandreplace()
        try:
            # evaluate the expression using the eval function
            self.value = eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0, END)
            self.e.insert(0, 'Invalid Input!')
        else:
            self.e.delete(0, END)
            self.e.insert(0, self.value)

    def squareroot(self):
        self.getandreplace()
        try:
            # evaluate the expression using the eval function
            self.value = eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0, END)
            self.e.insert(0, 'Invalid Input!')
        else:
            self.sqrtval = math.sqrt(self.value)
            self.e.delete(0, END)
            self.e.insert(0, self.sqrtval)

    def clearall(self):
        self.e.delete(0, END)

    def clearnow(self):
        self.txt = self.e.get()[:-1]
        self.e.delete(0, END)
        self.e.insert(0, self.txt)

    def action(self, argi):
        self.e.insert(END, argi)

    def __init__(self, window):
        windowWidth = window.winfo_reqwidth()
        windowHeight = window.winfo_reqheight()
        positionRight = int(window.winfo_screenwidth() / 2.25 - windowWidth / 1)
        positionDown = int(window.winfo_screenheight() / 2.4 - windowHeight / 1)
        window.geometry("+{}+{}".format(positionRight, positionDown))
        window.geometry("512x520")
        window.title("CALCULATOR")
        window.configure(bg="#dedede")
        self.e = Entry(window, justify=RIGHT, bg="white", fg="black", font=("Times New Roman bold", 20),
                       borderwidth=8,
                       relief="sunken")
        self.e.grid(row=0, column=0, ipady=5, ipadx=88, padx=18, pady=30)
        self.e.focus_set()

        Button(window, font=("Times New Roman bold", 16,), text="AC", command=lambda: self.clearall(),
               fg='black',
               bg='#9da39d',
               cursor="hand2").place(x=20, y=110, height=60, width=150)

        Button(window, font=("Times New Roman bold", 16,), text="CE", command=lambda: self.clearnow(),
               fg='black',
               bg='#9da39d',
               cursor="hand2").place(x=180, y=110, height=60, width=150)

        Button(window, font=("Times New Roman bold", 16,), text="7", command=lambda: self.action('7'),
               fg='black', bg='#9da39d',
               cursor="hand2").place(x=20, y=180, height=70, width=90)
        Button(window, font=("Times New Roman bold", 16,), text="8", command=lambda: self.action('8'),
               fg='black', bg='#9da39d',
               cursor="hand2").place(x=130, y=180, height=70, width=90)
        Button(window, font=("Times New Roman bold", 16,), text="9", command=lambda: self.action('9'),
               fg='black', bg='#9da39d',
               cursor="hand2").place(x=240, y=180, height=70, width=90)
        Button(window, font=("Times New Roman bold", 16,), text="6", command=lambda: self.action('6'),
               fg='black', bg='#9da39d',
               cursor="hand2").place(x=240, y=262, height=70, width=90)

        Button(window, font=("Times New Roman bold", 16,), text="5", command=lambda: self.action('5'),
               fg='black', bg='#9da39d',
               cursor="hand2").place(x=130, y=262, height=70, width=90)
        Button(window, font=("Times New Roman bold", 16,), text="4", command=lambda: self.action('4'),
               fg='black', bg='#9da39d',
               cursor="hand2").place(x=20, y=262, height=70, width=90)
        Button(window, font=("Times New Roman bold", 16,), text="1", command=lambda: self.action('1'),
               fg='black', bg='#9da39d',
               cursor="hand2").place(x=20, y=344, height=70, width=90)
        Button(window, font=("Times New Roman bold", 16,), text="2", command=lambda: self.action('2'),
               fg='black', bg='#9da39d',
               cursor="hand2").place(x=130, y=344, height=70, width=90)
        Button(window, font=("Times New Roman bold", 16,), text="3", command=lambda: self.action('3'),
               fg='black', bg='#9da39d',
               cursor="hand2").place(x=240, y=344, height=70, width=90)
        Button(window, font=("Times New Roman bold", 16,), text="0", command=lambda: self.action('0'),
               fg='black',
               bg='#9da39d',
               cursor="hand2").place(x=20, y=426, height=70, width=90)

        Button(window, font=("Times New Roman bold", 16,), text="00",
               command=lambda: self.action('00'), fg='black',
               bg='#9da39d',
               cursor="hand2").place(x=130, y=426, height=70, width=90)
        Button(window, font=("Times New Roman bold", 16,), text=".", command=lambda: self.action('.'),
               fg='black',
               bg='#9da39d',
               cursor="hand2").place(x=240, y=426, height=70, width=90)
        Button(window, font=("Times New Roman bold", 16,),
               text="+", command=lambda: self.action('+'), fg='black', bg='#9da39d', cursor="hand2").place(x=345, y=262,
                                                                                                           height=153,
                                                                                                           width=45)
        Button(window, font=("Times New Roman bold", 16,), text="=", command=lambda: self.equals(),
               fg='black',
               bg='#9da39d',
               cursor="hand2").place(x=345, y=428, height=70, width=150)

        Button(window, font=("Times New Roman bold", 16,), text="-", command=lambda: self.action('-'), fg='black',
               bg='#9da39d',
               cursor="hand2").place(x=405, y=344,
                                     height=70,
                                     width=87)
        Button(window, font=("Times New Roman bold", 16,), text="/", command=lambda: self.action('/'), fg='black',
               bg='#9da39d',
               cursor="hand2").place(x=405, y=262,
                                     height=70,
                                     width=87)
        Button(window, font=("Times New Roman bold", 16,), text="*", command=lambda: self.action('x'),
               fg='black',
               bg='#9da39d',
               cursor="hand2").place(x=405, y=180, height=70, width=87)
        Button(window, font=("Times New Roman bold", 16,), text="%", command=lambda: self.action('%'),
               fg='black',
               bg='#9da39d',
               cursor="hand2").place(x=345, y=180, height=70, width=45)
        Button(window, font=("Times New Roman bold", 16,), text="π", command=lambda: self.action('3.14'),
               fg='black',
               bg='#9da39d',
               cursor="hand2").place(x=345, y=110, height=60, width=45)
        Button(window, font=("Times New Roman bold", 16,), text="√", command=lambda: self.squareroot(),
               fg='black',
               bg='#9da39d',
               cursor="hand2").place(x=405, y=110, height=60, width=87)


window = Tk()
obj = calc(window)

window.mainloop()
