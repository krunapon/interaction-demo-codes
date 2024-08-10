from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from random import choice

window_titles = ["Manee Jaidee", "653040123-4", "Something went wrong"]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.n_times_clicked = 0
        self.setWindowTitle("My App")
        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)
        self.windowTitleChanged.connect(self.the_window_title_changed)
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.n_times_clicked += 1
        print(f"The number of clicks is {self.n_times_clicked}")
        new_window_title = choice(window_titles)
        print(f"Setting title:  {new_window_title}")
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self, window_title):
        print(f"Window title changed: {window_title}")
        if window_title == "Something went wrong":
            self.button.setDisabled(True)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
