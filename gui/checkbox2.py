from tkinter import *
master = Tk()

def var_states():
   print("male: %d,\nfemale: %d" % (male_var.get(), female_var.get()))

def clear():
    male_var.set(0)
    female_var.set(0)

Label(master, text="Your gender:").grid(row=0, sticky=W)
male_var = IntVar()
Checkbutton(master, text="male", variable=male_var).grid(row=1, sticky=W)
female_var = IntVar()
Checkbutton(master, text="female", variable=female_var).grid(row=2, sticky=W)
Button(master, text='Show', command=var_states).grid(row=3, sticky=W, pady=4)
Button(master, text="Clear", command=clear).grid(row=4, sticky=W)
Button(master, text='Quit', command=master.quit).grid(row=5, sticky=W, pady=4)
mainloop()
