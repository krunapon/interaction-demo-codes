from PyQt6.QtWidgets import QWidget, QVBoxLayout, QApplication, QMainWindow, QCheckBox, QLineEdit
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
        self.name = QLineEdit()
        self.name.returnPressed.connect(self.text_changed)
        
        layout = QVBoxLayout()
        layout.addWidget(self.python_chkbox)
        layout.addWidget(self.java_chkbox)
        layout.addWidget(self.name)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def text_changed(self):
        print(f'Name changed to {self.name.text()}')

    def state_changed(self, value):
        state = Qt.CheckState(value)
        if state == Qt.CheckState.Checked:
            print(f'{self.sender().text()} is checked')

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()