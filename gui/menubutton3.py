from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
top = Tk()
mb = Menubutton(top, text="File")
mb.grid()
mb.menu =  Menu( mb, tearoff = 0 )
mb["menu"] =  mb.menu
open_menu = IntVar()
exit_menu = IntVar()
def open_file():
    file = askopenfile(mode ='r', filetypes =[('Python Files', '*.py')])
    if file is not None:
        content = file.read()
        print(content)
mb.menu.add_checkbutton ( label="Open",
                          variable=open_menu, command=open_file)
mb.menu.add_checkbutton ( label="Exit",
                          variable=exit_menu, command=top.quit)
mb.pack()
top.mainloop()
