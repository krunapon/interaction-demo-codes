import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QStackedLayout, QPushButton, QHBoxLayout
from layout_colorwidget import Color

class MainWindow(QMainWindow):
    def crt_add_btn(self, btn_name, btn_layout):
        btn = QPushButton(btn_name)
        btn.pressed.connect(self.btn_pressed)
        btn_layout.addWidget(btn)
        self.stacklayout.addWidget(Color(btn_name))

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Factoring Tablike Demo")

        pagelayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stacklayout = QStackedLayout()

        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.stacklayout)

        self.crt_add_btn("Red", button_layout)   
        self.crt_add_btn("Green", button_layout)
        self.crt_add_btn("Yellow", button_layout)
       
        container = QWidget()
        container.setLayout(pagelayout)
        self.setCentralWidget(container)

    def btn_pressed(self):
        if self.sender().text() == "Red":
            self.stacklayout.setCurrentIndex(0)
        elif self.sender().text() == "Green":
            self.stacklayout.setCurrentIndex(1)
        elif self.sender().text() == "Yellow":
            self.stacklayout.setCurrentIndex(2)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

