import sys
from PyQt6.QtWidgets import *
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Quit button with tooltips')
        self.button = QPushButton("Quit")
        self.button.clicked.connect(QApplication.instance().quit)
        self.button.setToolTip("This is a <b>QPushButton</b> widget")
        
        layout = QVBoxLayout()
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
        self.show()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
