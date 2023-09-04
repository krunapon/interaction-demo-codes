from PyQt6.QtWidgets import QWidget, QVBoxLayout, QApplication, QMainWindow, QCheckBox
from PyQt6.QtCore import Qt
import sys

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        self.python_chkbox = QCheckBox('Python')
        self.java_chkbox = QCheckBox('Java')
        self.python_chkbox.stateChanged.connect(self.state_changed)
        self.java_chkbox.stateChanged.connect(self.state_changed)

        layout = QVBoxLayout()
        layout.addWidget(self.python_chkbox)
        layout.addWidget(self.java_chkbox)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


    def state_changed(self, value):
        state = Qt.CheckState(value)
        if state == Qt.CheckState.Checked:
            print(f'{self.sender().text()} is checked')

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()