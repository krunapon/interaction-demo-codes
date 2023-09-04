import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        btn = QPushButton('Quit', self)
        btn.clicked.connect(QApplication.instance().quit)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Quit button with tooltips')
        self.show()


def main():

    app = QApplication(sys.argv)
    Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main() 
