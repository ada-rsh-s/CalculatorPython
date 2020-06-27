from tkinter import *

window = Tk()
windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()
positionRight = int(window.winfo_screenwidth() / 2.25 - windowWidth / 1)
positionDown = int(window.winfo_screenheight() / 2.4 - windowHeight / 1)
window.geometry("+{}+{}".format(positionRight, positionDown))
window.geometry("500x450")
window.title("CALCULATOR")
window.configure(bg="#dedede")
label_widget = Entry(window, bg="white", fg="black", font=("Times New Roman bold", 20), borderwidth=8,
                     relief="sunken")
label_widget.grid(row=0, column=0, ipady=5, ipadx=84, padx=18, pady=30)


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


def but_C():
    print("")


buttonAC = Button(window, font=("Times New Roman bold", 16,), text="AC", command=but_AC(), fg='black', bg='#9da39d',
                  cursor="hand2")
buttonAC.place(x=20, y=110, height=60, width=150)
buttonAC = Button(window, font=("Times New Roman bold", 16,), text="CE", command=but_C(), fg='black', bg='#9da39d',
                  cursor="hand2")
buttonAC.place(x=180, y=110, height=60, width=150)
button7 = Button(window, font=("Times New Roman bold", 16,), text="7", command=but7(), fg='black', bg='#9da39d',
                 cursor="hand2")
button7.place(x=20, y=180, height=70, width=90)
button8 = Button(window, font=("Times New Roman bold", 16,), text="8", command=but8(), fg='black', bg='#9da39d',
                 cursor="hand2")
button8.place(x=130, y=180, height=70, width=90)
button9 = Button(window, font=("Times New Roman bold", 16,), text="9", command=but9(), fg='black', bg='#9da39d',
                 cursor="hand2")
button9.place(x=240, y=180, height=70, width=90)
button6 = Button(window, font=("Times New Roman bold", 16,), text="6", command=but6(), fg='black', bg='#9da39d',
                 cursor="hand2")
button6.place(x=240, y=262, height=70, width=90)
button5 = Button(window, font=("Times New Roman bold", 16,), text="5", command=but5(), fg='black', bg='#9da39d',
                 cursor="hand2")
button5.place(x=130, y=262, height=70, width=90)
button4 = Button(window, font=("Times New Roman bold", 16,), text="4", command=but4(), fg='black', bg='#9da39d',
                 cursor="hand2")
button4.place(x=20, y=262, height=70, width=90)
button1 = Button(window, font=("Times New Roman bold", 16,), text="1", command=but1(), fg='black', bg='#9da39d',
                 cursor="hand2")
button1.place(x=20, y=344, height=70, width=90)
button2 = Button(window, font=("Times New Roman bold", 16,), text="2", command=but2(), fg='black', bg='#9da39d',
                 cursor="hand2")
button2.place(x=130, y=344, height=70, width=90)
button3 = Button(window, font=("Times New Roman bold", 16,), text="3", command=but3(), fg='black', bg='#9da39d',
                 cursor="hand2")
button3.place(x=240, y=344, height=70, width=90)
window = mainloop()
