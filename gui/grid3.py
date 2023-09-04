from tkinter import *
from PIL import ImageTk,Image

master = Tk()
Label(master, text="Height").grid(row=0, sticky=E)
Label(master, text="Width").grid(row=1, sticky=E)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
canvas = Canvas(master, width = 150, height = 200)
img = ImageTk.PhotoImage(Image.open("kku.jpg"))
canvas.create_image(20, 20, anchor=NW, image=img)
canvas.grid(row=0, column=2, columnspan=2, rowspan=2,
           sticky=W+E+N+S, padx=5, pady=5)
Button(master, text="Zoom in").grid(row=2, column=2)
Button(master, text="Zoom out").grid(row=2, column=3)
master.mainloop()
