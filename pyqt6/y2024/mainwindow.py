import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)

window = QMainWindow()
window.show()

# start the event loop
app.exec()
