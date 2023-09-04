from tkinter import *
window = Tk()
window.title("Welcome to our first GUI app")
lbl = Label(window, text="Hello", font=("Arial Bold", 50))
window.geometry('350x200')
lbl.grid(column=0, row=0)
window.mainloop()
