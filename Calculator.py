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
label_widget.grid(row=0, column=0, ipady=16, ipadx=110, padx=18, pady=30)


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


def but_AC():
    print("")


button1 = Button(window, text="AC", command=but_AC(), fg='black', bg='#92a19f')
button1.place(x=20, y=110, height=60, width=150)

window = mainloop()
