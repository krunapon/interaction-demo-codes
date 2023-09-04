import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from layout_colorwidget import Color
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("QVBoxLayout Demo")

        layout = QVBoxLayout()

        red_label = Color("red")
        green_label = Color("green")
        blue_label = Color("blue")

        layout.addWidget(red_label)
        layout.addWidget(green_label)
        layout.addWidget(blue_label)

        layout.setContentsMargins(0, 20, 10, 40)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()