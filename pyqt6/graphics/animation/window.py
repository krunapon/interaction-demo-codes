from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtCore import QPropertyAnimation, QPoint, QEasingCurve
import sys
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)
        self.setWindowTitle("Simple Animation on Position")
        self.child = QWidget(self)
        self.child.setStyleSheet("background-color:red;border-radius:15px;")
        self.child.resize(100, 100)
        
        self.anim = QPropertyAnimation(self.child, b"pos")
        self.anim.setEasingCurve(QEasingCurve.Type.OutBounceCubic)
        self.anim.setEndValue(QPoint(400, 400))
        self.anim.setDuration(1500)
        self.anim.start()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()