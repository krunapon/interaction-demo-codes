from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Welcome to our first GUI app")
lbl = Label(window, text="Hello")
window.geometry('350x200')
lbl.grid(column=0, row=0)
style = Style()
style.configure('W.TButton',
                foreground = 'blue',
                background="Yellow")


def clicked():
    lbl.configure(text="Button was clicked!!")


btn = Button(text="Click me", style = "W.TButton", command=clicked)
btn.grid(column=1, row=0)
window.mainloop()
