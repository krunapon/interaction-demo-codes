import sys
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        font = self.label.font()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter 
                           | Qt.AlignmentFlag.AlignVCenter)
        self.setCentralWidget(self.label)


    def mousePressEvent(self, e):
        self.label.setText("mousePressEvent")

    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()