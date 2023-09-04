import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QMenuBar, QToolBar, QStatusBar
from PyQt6.QtCore import Qt 
from PyQt6.QtGui import QIcon, QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()  
        self.setWindowTitle("Python Menus & Toolbars")
        self.resize(400, 200)
        
        self.label = QLabel("Hello!")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.label)
        self._createMenuBar()

    def _createMenuBar(self):
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()