import sys
from PyQt6.QtWidgets import QWidget, QLabel, QApplication


class AbsoluteLayout(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hello_label = QLabel('Hello', self)
        hello_label.move(15, 10)

        dme_label = QLabel('DME', self)
        dme_label.move(35, 40)

        students_label = QLabel('students', self)
        students_label.move(55, 70)

        self.setGeometry(700, 300, 200, 100)
        self.setWindowTitle('Absolute')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AbsoluteLayout()
    sys.exit(app.exec())
