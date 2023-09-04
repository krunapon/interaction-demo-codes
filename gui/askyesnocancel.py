from tkinter import *

from tkinter import messagebox

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x200')

def clicked():
 res = messagebox.askyesnocancel('Message title','Message content')
 print("You answer is {}".format(res))

btn = Button(window,text='Click here', command=clicked)

btn.grid(column=0,row=0)

window.mainloop()

