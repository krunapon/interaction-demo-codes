import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel,QToolBar 
from PyQt6.QtCore import Qt 
from menubardemo import MenuBarDemoWindow

class ToolBarDemoWindow(MenuBarDemoWindow):
    def __init__(self):
        super(MenuBarDemoWindow, self).__init__()  
        self.setWindowTitle("Python Menus & Toolbars")
        self.resize(400, 200)
        
        self.label = QLabel("Hello!")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.label)
        self._createMenuBar()
        self._createToolBars()
       
    def _createMenuBar(self):
        self.menuBar = self.menuBar()
        self.menuBar.setNativeMenuBar(False)
        self.fileMenu = self.menuBar.addMenu("File")
        self.editMenu = self.menuBar.addMenu("Edit")
        self.helpMenu = self.menuBar.addMenu("Help")
        
    def _createToolBars(self):
        self.fileToolBar = self.addToolBar("File")
        self.editToolBar = QToolBar("Edit", self)
        self.addToolBar(self.editToolBar)
        self.helpToolBar = QToolBar("Help", self)
        self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, self.helpToolBar)

     
        
app = QApplication(sys.argv)
window = ToolBarDemoWindow()
window.show()
app.exec()