import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QStackedLayout, QPushButton, QHBoxLayout
from layout_colorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tablike Demo")

        pagelayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stacklayout = QStackedLayout()

        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.stacklayout)

        red_btn = QPushButton("Red")   
        red_btn.pressed.connect(self.btn_red_pressed)
        button_layout.addWidget(red_btn)
        self.stacklayout.addWidget(Color("red"))

        green_btn = QPushButton("Green")
        green_btn.pressed.connect(self.btn_green_pressed)
        button_layout.addWidget(green_btn)
        self.stacklayout.addWidget(Color("green"))

        yellow_btn = QPushButton("Yellow")
        yellow_btn.pressed.connect(self.btn_yellow_pressed)
        button_layout.addWidget(yellow_btn)
        self.stacklayout.addWidget(Color("yellow"))

        container = QWidget()
        container.setLayout(pagelayout)
        self.setCentralWidget(container)

    def btn_red_pressed(self):
        self.stacklayout.setCurrentIndex(0)

    def btn_green_pressed(self):
        self.stacklayout.setCurrentIndex(1)

    def btn_yellow_pressed(self):
        self.stacklayout.setCurrentIndex(2)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

