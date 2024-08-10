import sys
from PyQt6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu Bar Example")

        # Create menu bar
        menu_bar = self.menuBar()

        # Forces the menu bar to appear within the window on # all platforms, rather than using the native menu # bar on macOS.
        menu_bar.setNativeMenuBar(False)

        # Create file menu and add it to menu bar
        file_menu = menu_bar.addMenu("File")

        # Add actions to file menu
        file_menu.addAction("New")
        file_menu.addAction("Open")
        file_menu.addAction("Save")
        file_menu.addAction("Exit")


# start the event loop
app = QApplication(sys.argv)

window = MainWindow()
print("About to show window")
window.show()
print("Window should be visible now")


app.exec()
