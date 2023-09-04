import sys
from PyQt5.QtWidgets import *


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Absolute positioning'
        self.setGeometry(10, 10, 300, 200)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)

        label_python = QLabel('Python', self)
        label_python.move(30,30)

        label_pyqt5 = QLabel('PyQt5', self)
        label_pyqt5.move(120,80)

        label_examples = QLabel('Examples', self)
        label_examples.move(200,150)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
