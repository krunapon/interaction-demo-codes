from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget, QAbstractItemView
import sys

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        self.listWidget = QListWidget()
        self.listWidget.addItems(["One", "Two", "Three"])

        self.listWidget.currentItemChanged.connect(self.index_changed)
        self.listWidget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(self.listWidget)


    def index_changed(self, i): # Not an index, i is a QListWidgetItem
        print(i.text())

    def text_changed(self, s): # s is a str
        print(s)

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()