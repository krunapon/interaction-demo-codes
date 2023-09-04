import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedLayout
from layout_colorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("StackedLayout Demo")

        layout = QStackedLayout()

        layout.addWidget(Color("red"))  
        layout.addWidget(Color("green"))    
        layout.addWidget(Color("purple"))
        layout.addWidget(Color("yellow"))

        layout.setCurrentIndex(1)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()