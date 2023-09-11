import sys
import os
from PyQt6.QtGui import QKeySequence
from PyQt6.QtWidgets import QApplication
from toolbaricons import ToolbarIcons  
        
class StatusShortcuts(ToolbarIcons):  
    def __init__(self):
        super(StatusShortcuts, self).__init__()  
        self.setWindowTitle("Python Status Bar & Shortcuts")
        self.statusBar = self.statusBar()
        self.openAction.setStatusTip("Open File")
        self.statusBar.showMessage("Ready")
        self.openAction.setShortcut(QKeySequence("Ctrl+O"))
        self.openAction.triggered.connect(self._openFile)
        self._addMenu()
        
    def _openFile(self):
        self.label.setText("Open File Clicked")
        self.statusBar.showMessage("Open File Clicked")
    
    def _addMenu(self):
        self.menuBar = self.menuBar()
        self.menuBar.setNativeMenuBar(False)
        self.fileMenu = self.menuBar.addMenu("File")
        self.fileMenu.addAction(self.newAction)
        self.fileMenu.addAction(self.openAction)
        
if __name__ == "__main__":   
    app = QApplication(sys.argv)
    window = StatusShortcuts() 
    window.show()
    app.exec()