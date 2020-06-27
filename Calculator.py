from tkinter import *

window = Tk()
window.geometry("500x540")
window.title("CALCULATOR")
window.configure(bg="lightgrey")
label_widget = Label(window, text="A Label", font=("Helvetica", 16), width=540, height=2)
label_widget.pack()
window = mainloop()
