#!/usr/bin/python

from PyQt6.QtWidgets import QWidget, QApplication, QFrame, QPushButton
from PyQt6.QtCore import QRect, QPropertyAnimation
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.button = QPushButton("Start", self)
        self.button.clicked.connect(self.doAnim)
        self.button.move(30, 30)

        self.frame = QFrame(self)
        self.frame.setFrameStyle(QFrame.Shape.Panel | QFrame.Shadow.Raised)
        self.frame.setStyleSheet("background-color:red")
        self.frame.setGeometry(150, 30, 100, 100)

        self.setGeometry(300, 300, 380, 300)
        self.setWindowTitle('Animation')
        self.show()

    def doAnim(self):

        self.anim = QPropertyAnimation(self.frame, b"geometry")
        self.anim.setDuration(10000)
        self.anim.setStartValue(QRect(150, 30, 100, 100))
        self.anim.setEndValue(QRect(150, 30, 200, 200))
        self.anim.start()

if __name__ == "__main__":
    app = QApplication([])
    Example()
    sys.exit(app.exec())