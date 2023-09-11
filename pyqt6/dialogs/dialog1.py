import sys

from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self):
        dlg = QDialog(self)
        dlg.setWindowTitle("HELLO!")
        dlg.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)    
    window = MainWindow()
    window.show()
    app.exec()