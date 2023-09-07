import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import Qt 
from PyQt6.QtGui import QAction, QIcon

class ToolbarAction(QMainWindow):
    def __init__(self):
        super(ToolbarAction, self).__init__()  
        self.setWindowTitle("Python Menus & Toolbars")
        self.resize(400, 200)
        self.label = QLabel("Hello!")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.label)
        self._createActions()
        self._createToolBars()
        
    def _createActions(self):
        # File actions
        self.newAction = QAction(self)
        self.newAction.setText("New")
        path = os.path.dirname(__file__)
        os.chdir(path)
        self.newAction.setIcon(QIcon("images/file-new.svg"))
        self.openAction = QAction(QIcon("images/file-open.svg"),
                                  "Open", self)
  
    def _createToolBars(self):
        # File toolbar
        fileToolBar = self.addToolBar("File")
        fileToolBar.addAction(self.newAction)
        fileToolBar.addAction(self.openAction)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToolbarAction() 
    window.show()
    app.exec()