import sys
import os
from PyQt6.QtGui import QKeySequence
from PyQt6.QtWidgets import QApplication
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from menus.toolbaraction import ToolbarAction

class ToolbarIcons(ToolbarAction):
    def __init__(self):
        super(ToolbarIcons, self).__init__()  
        self.setWindowTitle("Python Toolbar Icons")
        self.label.setText("Hello, Toolbar Icons")
        self.statusBar = self.statusBar()
        self.openAction.setStatusTip("Open File")
        self.statusBar.showMessage("Ready")
        self.openAction.setShortcut(QKeySequence("Ctrl+O"))
        self.openAction.triggered.connect(self._openFile)
        
    def _openFile(self):
        self.label.setText("Open File Clicked")
        self.statusBar.showMessage("Open File Clicked") 
       
if __name__ == "__main__":   
    app = QApplication(sys.argv)
    window = ToolbarIcons() 
    window.show()
    app.exec()