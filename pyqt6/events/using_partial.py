from PyQt6.QtWidgets import (QMainWindow, QPushButton, QHBoxLayout, QWidget, QApplication)
import sys
from functools import partial
    
class MyForm(QMainWindow):
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        button1 = QPushButton('Button 1')
        button2 = QPushButton('Button 2')
        button1.clicked.connect(partial(self.on_button,1))
        button2.clicked.connect(partial(self.on_button,2))

        layout = QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)

        main_frame = QWidget()
        main_frame.setLayout(layout)

        self.setCentralWidget(main_frame)

    def on_button(self, n):
        print(f'Button {n} clicked')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    app.exec()