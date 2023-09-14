import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QColorDialog, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QColor

class ColorDialog(QWidget):
    def __init__(self):
        super().__init__()
        col = QColor(0,255,0)
        self.setWindowTitle("Color dialog")
        self.button = QPushButton("Press me for a dialog!")
        self.button.clicked.connect(self.button_clicked)
        self.label = QLabel("Hello World")
        self.label.setStyleSheet(f"background-color:{col.name()}")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)   
        self.setLayout(self.layout)

    def button_clicked(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.label.setStyleSheet(f"background-color:{col.name()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)    
    window = ColorDialog()
    window.show()
    app.exec()