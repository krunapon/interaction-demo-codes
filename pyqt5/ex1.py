import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Exercise1(QWidget):
    def __init__(self, name):
        super().__init__()
        self.init_ui(name)

    def init_ui(self, name):
        btn = QPushButton('Quit', self)
        btn.clicked.connect(QApplication.instance().quit)
        btn.setToolTip('Click to exit')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        label = QLabel('My name is ' + name, self)
        label.move(30,30)
        label.show()

     
        self.setWindowTitle('Exercise 1')
        self.show()
 
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
	    qr = self.frameGeometry()
	    cp = QDesktopWidget().availableGeometry().center()
	    qr.moveCenter(cp)
	    self.move(qr.topLeft())


def main():
    app = QApplication(sys.argv)
    ex1 = Exercise1(sys.argv[1])
    sys.exit(app.exec_())


if __name__ == '__main__':
    main() 
