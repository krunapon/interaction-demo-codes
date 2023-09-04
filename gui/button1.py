from tkinter import *
window = Tk()
window.title("Welcome to our first GUI app")
lbl = Label(window, text="Hello")
window.geometry('350x200')
lbl.grid(column=0, row=0)
btn = Button(window, text="Click Me")
btn.grid(column=1, row=0)
window.mainloop()
