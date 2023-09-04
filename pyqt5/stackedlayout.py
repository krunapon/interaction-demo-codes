import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class StackedExample(QWidget):

    def __init__(self):
        super(StackedExample, self).__init__()
        self.leftlist = QListWidget()

        self.leftlist.insertItem(0, 'Contact')
        self.leftlist.insertItem(1, 'Personal')
        self.leftlist.insertItem(2, 'Educational')

        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()

        self.contact_ui()
        self.personal_ui()
        self.educational_ui()

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.stack1)
        self.Stack.addWidget(self.stack2)
        self.Stack.addWidget(self.stack3)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.leftlist)
        hbox.addWidget(self.Stack)

        self.setLayout(hbox)
        self.leftlist.currentRowChanged.connect(self.display)
        self.setGeometry(300, 50, 10, 10)
        self.setWindowTitle('StackedLayout')
        self.show()


    def contact_ui(self):
        layout = QFormLayout()
        layout.addRow("Name", QLineEdit())
        layout.addRow("Address", QLineEdit())
        # self.setTabText(0,"Contact Details")
        self.stack1.setLayout(layout)


    def personal_ui(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton("Male"))
        sex.addWidget(QRadioButton("Female"))
        layout.addRow(QLabel("Gender"), sex)
        layout.addRow("Date of Birth", QLineEdit())

        self.stack2.setLayout(layout)


    def educational_ui(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("subjects"))
        layout.addWidget(QCheckBox("Physics"))
        layout.addWidget(QCheckBox("Maths"))
        self.stack3.setLayout(layout)


    def display(self, i):
        self.Stack.setCurrentIndex(i)


def main():
    app = QApplication(sys.argv)
    stacked_ex = StackedExample()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
