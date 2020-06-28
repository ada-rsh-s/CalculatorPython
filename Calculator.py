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
            self.value = eval(self.newtext)
        except (SyntaxError, NameError, ZeroDivisionError):
            self.e.delete(0, END)
            self.e.insert(0, 'Invalid Input!')
        else:
            self.e.delete(0, END)
            self.e.insert(0, self.value)

    def squareroot(self):
        self.getandreplace()
        try:
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
        positionDown = int(window.winfo_screenheight() / 2.7 - windowHeight / 1)
        window.geometry("+{}+{}".format(positionRight, positionDown))
        window.geometry("512x520")
        window.title("CALCULATOR")
        window.configure(bg="#A37B5C")
        window.resizable(0, 0)
        self.e = Entry(window, state=NORMAL, justify=RIGHT, bg="light grey", fg="black",
                       font=("Times New Roman bold", 20),

                       relief="sunken")
        self.e.configure(highlightbackground="red", borderwidth=8)
        self.e.bind("<a>", "no")
        self.e.bind("<b>", "no")
        self.e.bind("<c>", "no")
        self.e.bind("<d>", "no")
        self.e.bind("<e>", "no")
        self.e.bind("<f>", "no")
        self.e.bind("<g>", "no")
        self.e.bind("<h>", "no")
        self.e.bind("<i>", "no")
        self.e.bind("<j>", "no")
        self.e.bind("<k>", "no")
        self.e.bind("<l>", "no")
        self.e.bind("<m>", "no")
        self.e.bind("<n>", "no")
        self.e.bind("<o>", "no")
        self.e.bind("<p>", "no")
        self.e.bind("<q>", "no")
        self.e.bind("<r>", "no")
        self.e.bind("<s>", "no")
        self.e.bind("<t>", "no")
        self.e.bind("<u>", "no")
        self.e.bind("<v>", "no")
        self.e.bind("<w>", "no")
        self.e.bind("<x>", "no")
        self.e.bind("<y>", "no")
        self.e.bind("<z>", "no")
        self.e.bind("<A>", "no")
        self.e.bind("<B>", "no")
        self.e.bind("<C>", "no")
        self.e.bind("<D>", "no")
        self.e.bind("<E>", "no")
        self.e.bind("<F>", "no")
        self.e.bind("<G>", "no")
        self.e.bind("<H>", "no")
        self.e.bind("<I>", "no")
        self.e.bind("<J>", "no")
        self.e.bind("<K>", "no")
        self.e.bind("<L>", "no")
        self.e.bind("<M>", "no")
        self.e.bind("<N>", "no")
        self.e.bind("<O>", "no")
        self.e.bind("<P>", "no")
        self.e.bind("<Q>", "no")
        self.e.bind("<R>", "no")
        self.e.bind("<S>", "no")
        self.e.bind("<T>", "no")
        self.e.bind("<U>", "no")
        self.e.bind("<V>", "no")
        self.e.bind("<W>", "no")
        self.e.bind("<X>", "no")
        self.e.bind("<Y>", "no")
        self.e.bind("<Z>", "no")
        self.e.bind("!", "no")
        self.e.bind("@", "no")
        self.e.bind("$", "no")
        self.e.bind("#", "no")
        self.e.bind("^", "no")
        self.e.bind("&", "no")
        self.e.bind("_", "no")
        self.e.bind("?", "no")
        self.e.bind(":", "no")
        self.e.bind(">", "no")
        self.e.bind(";", "no")
        self.e.bind(",", "no")
        self.e.bind("'", "no")
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
               cursor="hand2").place(x=345, y=110,
                                     height=140,
                                     width=45)
        Button(window, font=("Times New Roman bold", 16,), text="/", command=lambda: self.action('/'), fg='black',
               bg='#9da39d',
               cursor="hand2").place(x=405, y=344,
                                     height=70,
                                     width=87)
        Button(window, font=("Times New Roman bold", 16,), text="x", command=lambda: self.action("*"),
               fg='black',
               bg='#9da39d',
               cursor="hand2").place(x=405, y=262, height=70, width=87)
        Button(window, font=("Times New Roman bold", 16,), text="π", command=lambda: self.action('3.14'),
               fg='black',
               bg='#9da39d',
               cursor="hand2").place(x=405, y=110, height=60, width=87)
        Button(window, font=("Times New Roman bold", 16,), text="√", command=lambda: self.squareroot(),
               fg='black',
               bg='#9da39d',
               cursor="hand2").place(x=405, y=180, height=70, width=87)


window = Tk()
obj = calc(window)

window.mainloop()
