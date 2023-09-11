from PyQt6.QtWidgets import (QWidget, QPushButton, 
                             QLabel,
        QInputDialog, QApplication, QHBoxLayout)
import sys

class InputDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        self.label.setText("Hello World!")
        self.btn = QPushButton('Get name', self)
        self.btn.clicked.connect(self.showDialog)
        
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.btn)
        self.setWindowTitle('Input dialog')
        self.setLayout(self.layout)

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 
                    'Input Dialog',
                    'Enter your name:')
        if ok:
            self.label.setText(str(text))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = InputDialog()
    ex.show()
    sys.exit(app.exec())