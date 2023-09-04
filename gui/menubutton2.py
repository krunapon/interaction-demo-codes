from tkinter import *
import tkinter
top = Tk()
mb = Menubutton( top, text="Sport", relief=RAISED )
mb.grid()
mb.menu =  Menu( mb, tearoff = 0 )
mb["menu"] =  mb.menu
badmintonVar = IntVar()
runningVar = IntVar()
mb.menu.add_checkbutton ( label="Badminton",
                          variable=badmintonVar )
mb.menu.add_checkbutton ( label="Running",
                          variable=runningVar )
mb.pack()
def clicked():
    print("Badminton value is {}".format(badmintonVar.get()))
    print("Running value is {}".format(runningVar.get()))
btn_show = Button(text="Show",command=clicked)
btn_show.pack()
btn_quit = Button(text="Quit", command=top.quit)
btn_quit.pack()
top.mainloop()
