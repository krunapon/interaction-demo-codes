import sys
from PyQt6.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QRadioButton')
        self.setMinimumWidth(300)

        # create a grid layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel('Please select a platform:', self)

        androidRb = QRadioButton('Android', self)
        androidRb.toggled.connect(self.update)

        iosRb = QRadioButton('iOS', self)
        iosRb.toggled.connect(self.update)

        self.resultLabel = QLabel('', self)

        layout.addWidget(label)
        layout.addWidget(androidRb)
        layout.addWidget(iosRb)
        layout.addWidget(self.resultLabel)

        # show the window
        self.show()

    def update(self):
        # get the radio button that sends the signal
        rb = self.sender()

        # check if the radio button is checked
        if rb.isChecked():
            self.resultLabel.setText(f'You selected {rb.text()}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())