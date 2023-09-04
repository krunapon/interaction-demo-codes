from tkinter import *

window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
spin1 = Spinbox(window, from_=0, to=10, width=5)
spin2 = Spinbox(window, values=(3, 8, 11), width=5)
var = IntVar()
var.set(36)
spin3 = Spinbox(window, from_=0, to=100, width=5, textvariable=var)
spin1.grid(column=0,row=0)
spin2.grid(column=0, row=1)
spin3.grid(column=0, row=2)
window.mainloop()
