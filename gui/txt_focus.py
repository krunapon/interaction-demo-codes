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

txt = Entry(window, width=10)
txt.grid(column=1, row=0)
txt.focus()

def clicked():
    res = txt.get()
    lbl.configure(text="Welcome to " + res)
    txt.focus()
    txt.delete(0, len(res))
    txt.icursor(0)

btn = Button(text="Click me", style = "W.TButton", command=clicked)
btn.grid(column=2, row=0)
window.mainloop()
