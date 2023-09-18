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
        from random import randint
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)

        pen = QtGui.QPen()
        pen.setWidth(1)
        pen.setColor(QtGui.QColor('green'))
        painter.setPen(pen)

        font = QtGui.QFont()
        font.setFamily('Times')
        font.setBold(True)
        font.setPointSize(40)
        painter.setFont(font)

        painter.drawText(100, 100, 'Hello, world!')
        pen.setColor(QtGui.QColor('blue'))
        painter.setPen(pen)
        painter.drawText(200, 200, 100, 100, Qt.AlignmentFlag.AlignHCenter, 'Hi, World!')
        painter.end()
        self.label.setPixmap(canvas)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()