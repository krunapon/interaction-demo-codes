from PyQt6 import QtWidgets 
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QSlider, QMainWindow, QLabel, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.slider = QSlider(Qt.Orientation.Horizontal)

        self.slider.setMinimum(0)
        self.slider.setMaximum(10)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(2)
        self.slider.setValue(5)
        self.slider.valueChanged.connect(self.display)
        
        self.value_label = QLabel("Value: "+str(self.slider.value()))
        self.value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.slider)
        layout.addWidget(self.value_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def display(self):
        print(self.sender().value())
        self.value_label.setText("Value: "+str(self.sender().value()))
        self.value_label.adjustSize() 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window =  MainWindow()
    window.show()
    app.exec()
