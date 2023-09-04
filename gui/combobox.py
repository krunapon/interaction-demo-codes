from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Welcome to our first GUI app")
lbl = Label(window, text="Hello")

lbl.pack()
style = Style()
style.configure('W.TButton',
                foreground = 'blue',
                background="Yellow")

txt = Entry(window, width=10)
txt.pack()
txt.focus()

def clicked():
    res = txt.get()
    lbl.configure(text="Welcome to " + res)
    txt.focus()
    txt.delete(0, len(res))
    txt.icursor(0)

btn = Button(text="Click me", style = "W.TButton", command=clicked)
btn.pack()

combobox = Combobox(window)
combobox['values']= (1, 2, 3, 4, 5, "Text")
combobox.current(2) #set the selected item
combobox.pack()
print("{} is selected".format(combobox.get()))

window.geometry('300x500')
window.mainloop()
