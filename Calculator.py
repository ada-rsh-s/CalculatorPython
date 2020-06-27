from tkinter import *

window = Tk()

windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()
positionRight = int(window.winfo_screenwidth() / 2.25 - windowWidth / 1)
positionDown = int(window.winfo_screenheight() / 2.8 - windowHeight / 1)
window.geometry("+{}+{}".format(positionRight, positionDown))
window.geometry("500x540")
window.title("CALCULATOR")
window.configure(bg="light grey")
label_widget = Entry(window, bg="#7f8785", fg="white", font=("Helvetica", 16))
label_widget.grid(ipady=16, ipadx=110, padx=18, pady=30)


def but1():
    print("1")


def but2():
    print("2")


def but3():
    print("3")


def but4():
    print("4")


def but5():
    print("5")


def but6():
    print("6")


def but7():
    print("7")


def but8():
    print("8")


def but9():
    print("9")


def but0():
    print("0")


def but_point():
    print(".")


def but_plus():
    print("+")


def but_minus():
    print("-")


def but_multiply():
    print("X")


def but_div():
    print("/")


button1 = Button(window, text="1", command=but1(), fg='black', bg='#92a19f')
button1.grid(row=1, column=1, ipady=12, ipadx=16)

button2 = Button(window, text="2", command=but2(), fg='black', bg='#92a19f')
button2.grid(row=1, column=1, ipady=12, ipadx=16)

button3 = Button(window, text="3", command=but3(), fg='black', bg='#92a19f')
button3.grid(row=1, column=1, ipady=12, ipadx=16)

button4 = Button(window, text="4", command=but4(), fg='black', bg='#92a19f')
button4.grid(row=1, column=1, ipady=12, ipadx=16)

button5 = Button(window, text="5", command=but5(), fg='black', bg='#92a19f')
button5.grid(row=1, column=1, ipady=12, ipadx=16)

button6 = Button(window, text="6", command=but6(), fg='black', bg='#92a19f')
button6.grid(row=1, column=1, ipady=12, ipadx=16)

button7 = Button(window, text="7", command=but7(), fg='black', bg='#92a19f')
button7.grid(row=1, column=1, ipady=12, ipadx=16)

button8 = Button(window, text="8", command=but8(), fg='black', bg='#92a19f')
button8.grid(row=1, column=1, ipady=12, ipadx=16)

button9 = Button(window, text="9", command=but9(), fg='black', bg='#92a19f')
button1.grid(row=1, column=1, ipady=12, ipadx=16)

button0 = Button(window, text="0", command=but0(), fg='black', bg='#92a19f')
button1.grid(row=1, column=1, ipady=12, ipadx=16)

buttonpoint = Button(window, command=but_point(), fg='black', bg='#92a19f')
button1.grid(row=1, column=1, ipady=12, ipadx=16)

buttonplus = Button(window, command=but_plus(), fg='black', bg='#92a19f')
button1.grid(row=1, column=1, ipady=12, ipadx=16)

buttonminus = Button(window, command=but_minus(), fg='black', bg='#92a19f')
button1.grid(row=1, column=1, ipady=12, ipadx=16)

buttonmultiply = Button(window, command=but_multiply(), fg='black', bg='#92a19f')
button1.grid(row=1, column=1, ipady=12, ipadx=16)

buttondivision = Button(window, command=but_div(), fg='black', bg='#92a19f')
button1.grid(row=1, column=1, ipady=12, ipadx=16)

window = mainloop()
