from PyQt6.QtWidgets import *
import sys

class Window(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Labels Demo")
		self.setGeometry(700, 100, 300, 200)
		self.green_label = QLabel('Light green', self)
		self.green_label.move(100, 50)
		self.green_label.setStyleSheet("color: blue; background-color: lightgreen")

		self.yellow_label = QLabel('Yellow', self)
		self.yellow_label.move(100, 100)
		self.yellow_label.setStyleSheet("background-color: yellow; border: 1px solid black;")

		self.show()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
