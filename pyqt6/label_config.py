from PyQt6.QtWidgets import QLabel, QMainWindow, QApplication  
from PyQt6.QtCore import Qt

import sys
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My App")
        label = QLabel("Hello")
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter 
                           | Qt.AlignmentFlag.AlignVCenter)

        self.setCentralWidget(label)

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()