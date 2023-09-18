import sys
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import Qt


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

    def draw_something(self):
        from random import randint, choice
        colors = ['#FFD141', '#376F9F', '#0D1F2D', '#E9EBEF', '#EB5160']
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(15)
        pen.setColor(QtGui.QColor('blue'))
        painter.setPen(pen)
        painter.drawLine(
            QtCore.QPoint(100, 100),
            QtCore.QPoint(300, 200) 
        )
        painter.end()
        self.label.setPixmap(canvas)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()