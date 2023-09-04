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

listbox = Listbox(window, selectmode=MULTIPLE)
listbox.insert(1, 'Python')
listbox.insert(2, 'JavaScript')
listbox.insert(3, 'Java')
listbox.activate(1)
listbox.activate(3)
listbox.pack()
selection = listbox.curselection()

def get_items():
    sel_items = listbox.curselection()
    print("selected items are")
    for sel_index in sel_items:
        print("{} ".format(listbox.get(sel_index)))


btn_listbox = Button(text="Choose language", command=get_items)
btn_listbox.pack()

selected = IntVar()
morning_rb = Radiobutton(window, text='Morning', value=1, variable=selected)
evening_rb = Radiobutton(window, text='Evening', value=2, variable=selected)
morning_rb.pack()
evening_rb.pack()


def get_period():
    selected_result = selected.get()
    text = period_lbl.cget("text")
    if selected_result == 1:
        period_lbl.config(text = text + "Morning")
    else:
        period_lbl.config(text = text + "Evening")


btn_radiobutton = Button(text="Choose period", command=get_period)
btn_radiobutton.pack()
period_lbl = Label(window, text = "You choose ")
period_lbl.pack()

window.geometry('300x400')
window.mainloop()
