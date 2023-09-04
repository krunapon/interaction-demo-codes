import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QHBoxLayout')

        # create a buttons layout
        buttons_layout = QHBoxLayout()
        titles = ['Yes', 'No', 'Cancel']

        buttons_layout.addStretch()

        buttons = [QPushButton(title) for title in titles]
        for button in buttons:
            buttons_layout.addWidget(button)

        buttons_layout.addStretch()
        
        overall_layout = QVBoxLayout()
        lineedit = QLineEdit("Hello World")
        lineedit.setMinimumWidth(300)
        overall_layout.addWidget(lineedit)
        overall_layout.addLayout(buttons_layout)

        self.setLayout(overall_layout)

        # show the window
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())