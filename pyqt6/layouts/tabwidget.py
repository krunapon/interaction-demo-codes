import sys

from PyQt6.QtWidgets import QApplication, QMainWindow , QTabWidget
from PyQt6.QtCore import Qt
from layout_colorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TabWidget Demo")   

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.North)
        tabs.setMovable(True)

        for n, color in enumerate(['Red', 'Green', 'Blue', 'Yellow']):
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()