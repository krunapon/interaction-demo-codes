import sys
from PyQt5.QtWidgets import *


class Exercise3(QWidget):

    def __init__(self, name):
        super().__init__()
        self.init_ui(name)

    def init_ui(self, name):
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 3, 1)

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        grid.addLayout(hbox, 6, 1)

        self.setLayout(grid)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review by ' + name)
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Exercise3(sys.argv[1])
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
