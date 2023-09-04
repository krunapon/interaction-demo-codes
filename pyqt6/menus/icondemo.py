import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QToolBar
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QIcon 
from pathlib import Path
import os

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My Awesome App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        #icon_path = str(Path(__file__).parent / "file-save.png")
        path = os.path.dirname(__file__)
        os.chdir(path)
        #button_action = QAction(QIcon(icon_path), "Your button", self)
        button_action = QAction(QIcon("images/file-save.png"), "Your button", self) 
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)


    def onMyToolBarButtonClick(self, s):
        print("click", s)
        
app = QApplication(sys.argv)
window = MainWindow() 
window.show()
app.exec()