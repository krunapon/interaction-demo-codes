from tkinter import *
window = Tk()
window.title("Welcome to our first GUI app")
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)
window.mainloop()
