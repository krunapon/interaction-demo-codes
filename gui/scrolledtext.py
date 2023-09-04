from tkinter import *

from tkinter import scrolledtext

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x200')

txt = scrolledtext.ScrolledText(window,width=40,height=10)
txt.insert(INSERT, "Khon Kaen University")
txt.delete(1.0, END)
txt.insert(CURRENT, "Hello")


txt.grid(column=0,row=0)

window.mainloop()
