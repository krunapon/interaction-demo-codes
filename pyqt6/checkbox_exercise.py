from PyQt6.QtWidgets import QWidget, QVBoxLayout, QApplication, QMainWindow, QCheckBox, QLabel
from PyQt6.QtCore import Qt
import sys

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        self.orange_juice_chkbox = QCheckBox('Orange juice')
        self.orange_juice_chkbox.setCheckState(Qt.CheckState.Checked)
        self.green_tea_chkbox = QCheckBox('Green tea')
        
        self.ask_beverage_label = QLabel('What do you want to drink?')

        layout = QVBoxLayout()
        layout.addWidget(self.orange_juice_chkbox)
        layout.addWidget(self.green_tea_chkbox)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


    def show_state(self, chkbox):
        if chkbox.checkState() == Qt.CheckState.Checked:
            print(f'I want to drink {chkbox.text()}')
        else:
            print(f'I don\'t want to have {chkbox.text()} yet')

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()