import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt 

class MenuBarDemoWindow(QMainWindow):
    def __init__(self):
        super(MenuBarDemoWindow, self).__init__()  
        self.setWindowTitle("Python Menus & Toolbars")
        self.resize(400, 200)
        
        self.label = QLabel("Hello!")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.label)
        self._createMenuBar()

    def _createMenuBar(self):
        self.menuBar = self.menuBar()
        self.menuBar.setNativeMenuBar(False)
        self.fileMenu = self.menuBar.addMenu("File")
        self.editMenu = self.menuBar.addMenu("Edit")
        self.helpMenu = self.menuBar.addMenu("Help")

    def _addEditMenu(self):
        self.copyAction = QAction("Copy", self)
        self.pasteAction = QAction("Paste", self)
        self.cutAction = QAction("Cut", self)
        self.editMenu.addAction(self.copyAction)
        self.editMenu.addAction(self.pasteAction)
        self.editMenu.addAction(self.cutAction)
        
    def _addHelpMenu(self):
        self.aboutAction = QAction("About", self)
        self.helpMenu.addAction(self.aboutAction)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MenuBarDemoWindow()
    window.show()
    app.exec()