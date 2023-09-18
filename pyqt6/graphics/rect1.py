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
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor("#EB5160"))
        painter.setPen(pen)
        painter.drawRect(50, 50, 100, 100)
        pen.setColor(QtGui.QColor("#FFD141"))
        painter.setPen(pen)
        painter.drawRects(
            QtCore.QRect(60, 60, 100, 100),
            QtCore.QRect(80, 80, 150, 100),
            QtCore.QRect(90, 90, 100, 150),
        )
        painter.end()
        self.label.setPixmap(canvas)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()