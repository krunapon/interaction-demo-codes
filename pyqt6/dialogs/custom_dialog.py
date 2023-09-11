import sys

from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QDialogButtonBox, QLabel, QVBoxLayout

class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)  
        
        self.setWindowTitle("HELLO!")
        
        qBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        
        self.buttonBox = QDialogButtonBox(qBtn)
        self.buttonBox.accepted.connect(self.accept)    
        self.buttonBox.rejected.connect(self.reject)
        
        self.layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self):
        dlg = CustomDialog(self)
        dlg.setWindowTitle("HELLO!")
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)    
    window = MainWindow()
    window.show()
    app.exec()