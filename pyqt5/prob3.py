import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class Prob3(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        label_name = QLabel("Name")
        edit_name = QLineEdit()
        edit_name.setMinimumSize(200,20)
        fbox = QFormLayout()
        fbox.addRow(label_name, edit_name)

        languages = QHBoxLayout()
        chbox_pyqt = QCheckBox("PyQt")
        chbox_pyqt.setChecked(True)
        chbox_pygame = QCheckBox("PyGame")
        chbox_pytorch = QCheckBox("PyTorch")
        languages.addWidget(chbox_pyqt)
        languages.addWidget(chbox_pygame)
        languages.addWidget(chbox_pytorch)
        languages.addStretch()
        chbox_pyqt.stateChanged.connect(
            lambda:self.display_selected_lang(chbox_pyqt))
        chbox_pygame.stateChanged.connect(
            lambda:self.display_selected_lang(chbox_pygame))
        chbox_pytorch.stateChanged.connect(
            lambda:self.display_selected_lang(chbox_pytorch))
        fbox.addRow(QLabel("Library"), languages)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        submit = QPushButton("Submit")
        submit.clicked.connect(
            lambda:self.display_name(edit_name))
        hbox.addWidget(submit)
        hbox.addWidget(QPushButton("Cancel"))
        fbox.addRow(hbox)

        self.sizeHint()
        self.setLayout(fbox)
        self.setWindowTitle("Problem 3")
        self.show()


    def display_selected_lang(self, chkbox):
        if chkbox.isChecked() == True:
            print(chkbox.text() + " is selected")
        else:
            print(chkbox.text() + " is deselected")

    def display_name(self, edit_name):
        name = edit_name.text()
        print(f"Name is {name}")

def main():
    app = QApplication(sys.argv)
    form_layout = Prob3()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
