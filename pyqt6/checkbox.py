from PyQt6.QtWidgets import QWidget, QVBoxLayout, QApplication, QMainWindow, QCheckBox
from PyQt6.QtCore import Qt
import sys

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        self.python_chkbox = QCheckBox('Python')
        self.python_chkbox.setCheckState(Qt.CheckState.Checked)
        self.java_chkbox = QCheckBox('Java')
        

        layout = QVBoxLayout()
        layout.addWidget(self.python_chkbox)
        layout.addWidget(self.java_chkbox)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


    def show_state(self, chkbox):
        if chkbox.checkState() == Qt.CheckState.Checked:
            print(f'{chkbox.text()} is checked')
        else:
            print(f'{chkbox.text()} is unchecked')

app = QApplication(sys.argv)

window = MainWindow()
window.show()
window.show_state(window.python_chkbox)
window.show_state(window.java_chkbox)
app.exec()