import sys
import os
from PyQt6.QtGui import QKeySequence
from PyQt6.QtWidgets import QApplication
print("Current working directory: ", os.path.dirname(__file__))
print("Parent dir is " + os.pardir)
print("Parent of current working directory: ", os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from menus.toolbaraction import ToolbarAction

class ToolbarIcons(ToolbarAction):
    def __init__(self):
        super(ToolbarIcons, self).__init__()  
        self.setWindowTitle("Python Toolbar Icons")
        self.label.setText("Hello, Toolbar Icons")
 
       
if __name__ == "__main__":   
    app = QApplication(sys.argv)
    window = ToolbarIcons() 
    window.show()
    app.exec()