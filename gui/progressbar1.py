from tkinter import *
from tkinter import ttk
import time
class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter Progress Bar")
        self.minsize(200, 100)
        self.iconbitmap('icon.ico')
        self.buttonFrame = ttk.LabelFrame(self, text="Progress Bars")
        self.buttonFrame.grid(column=0, row=0)
        self.progressBar()

    def progressBar(self):
        self.button1 = ttk.Button(self.buttonFrame, text = "Run Progress Bar",
                                  command = self.run_progressbar)
        self.button1.grid(column =0, row = 0)
        self.button2 = ttk.Button(self.buttonFrame, text = "Start Progress Bar",
                                  command = self.start_progressbar)
        self.button2.grid(column = 0, row = 1)
        self.button3 = ttk.Button(self.buttonFrame, text="Stop Immediatly",
                                  command = self.stop_progressbar)
        self.button3.grid(column=0, row=2)
        self.progress_bar = ttk.Progressbar(self, orient = 'horizontal', length = 286,
                                mode = 'determinate')
        self.progress_bar.grid(column = 0, row = 3, pady  =2)

    def run_progressbar(self):
        self.progress_bar["maximum"] = 100
        for i in range(101):
            time.sleep(0.05)
            self.progress_bar["value"] = i
            self.progress_bar.update()
        self.progress_bar["value"] = 0


    def start_progressbar(self):
        self.progress_bar.start()


    def stop_progressbar(self):
        self.progress_bar.stop()


root = Root()
root.mainloop()
