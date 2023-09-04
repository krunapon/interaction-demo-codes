from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_value = 50
        self.slider = QSlider(Qt.Horizontal, self)
        self.label = QLabel(self)
        self.init_ui()

    def init_ui(self):
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(50)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(5)
        self.slider.setGeometry(30, 40, 300, 50)
        self.slider.valueChanged[int].connect(self.change_value)

        self.label.setText(str(self.init_value))
        self.label.setFont(QFont("Arial", 20))
        self.label.setStyleSheet("color: blue")
        self.label.setGeometry(170, 20, 80, 30)

        self.adjustSize()
        self.setWindowTitle('QSlider')
        self.show()

    def change_value(self, value):
        updated_value = value
        self.label.setText(str(updated_value))



def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
