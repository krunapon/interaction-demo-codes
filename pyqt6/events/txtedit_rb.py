from PyQt6.QtWidgets import QWidget, QVBoxLayout, QApplication, QMainWindow, QCheckBox, QLineEdit, QTextEdit, QRadioButton
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
        self.morning_rb = QRadioButton("Morning")
        self.afternoon_rb = QRadioButton("Afternoon")
        self.morning_rb.toggled.connect(self.rb_changed)
        self.afternoon_rb.toggled.connect(self.rb_changed)
        self.result = QTextEdit()
        
        layout = QVBoxLayout()
        layout.addWidget(self.python_chkbox)
        layout.addWidget(self.java_chkbox)
        layout.addWidget(self.name)
        layout.addWidget(self.morning_rb)
        layout.addWidget(self.afternoon_rb)
        layout.addWidget(self.result)   

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def text_changed(self):
        self.result.append(f'Name changed to {self.name.text()}')

    def state_changed(self, value):
        state = Qt.CheckState(value)
        if state == Qt.CheckState.Checked:
            self.result.append(f'{self.sender().text()} is checked')
            
    def rb_changed(self):
        name = self.sender().text()
        if self.sender().isChecked():
            self.result.append(f'{name} is checked')

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()