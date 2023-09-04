import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Prob1(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        label_title = QLabel("Simple Form")
        title_font = QFont('Times', 18)
        title_font.setBold(True)
        label_title.setFont(title_font)
        label_title.move(20, 2)
        label_title.setStyleSheet("color: blue")

        label_name = QLabel("Name")
        edit_name = QLineEdit()
        edit_name.setMinimumSize(200,20)

        fbox = QFormLayout()
        fbox.addWidget(label_title)
        fbox.addRow(label_name, edit_name)

        gender = QHBoxLayout()
        radio_male = QRadioButton("Male")
        radio_female = QRadioButton("Female")
        gender.addWidget(radio_male)
        gender.addWidget(radio_female)
        gender.addStretch()
        fbox.addRow(QLabel("Gender"), gender)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(QPushButton("Submit"))
        hbox.addWidget(QPushButton("Cancel"))
        fbox.addRow(hbox)

        self.sizeHint()
        self.setLayout(fbox)
        self.setWindowTitle("Problem 1")
        self.show()



def main():
    app = QApplication(sys.argv)
    form_layout = Prob1()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
