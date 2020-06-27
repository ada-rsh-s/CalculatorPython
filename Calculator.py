from tkinter import *

window = Tk()

windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()
print("Width", windowWidth, "Height", windowHeight)

positionRight = int(window.winfo_screenwidth() / 2.25 - windowWidth / 1)
positionDown = int(window.winfo_screenheight() / 2.8 - windowHeight / 1)

window.geometry("+{}+{}".format(positionRight, positionDown))
window.geometry("500x540")
window.title("CALCULATOR")
window.configure(bg="lightgrey")
label_widget = Label(window, text="A Label", font=("Helvetica", 16), width=540, height=2)
label_widget.pack()
window = mainloop()
