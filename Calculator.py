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
label_widget.grid(ipady=16, ipadx=110,padx=18,pady=30)
window = mainloop()
