from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class SimpleCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_value = 50
        self.input1 = QSlider(Qt.Horizontal, self)
        self.input2 = QSlider(Qt.Horizontal, self)
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.add = QPushButton("Add")
        self.subtract = QPushButton("Subtract")
        self.mult = QPushButton("Multiply")
        self.divide = QPushButton("Divide")
        self.active_source = self.add
        self.input_value1 = 50
        self.input_value2 = 50
        self.op = "Add"
        self.init_ui()

    def init_slider(self, slider, name):
        slider.setObjectName(name)
        slider.setMinimum(0)
        slider.setMaximum(100)
        slider.setValue(50)
        slider.setTickPosition(QSlider.TicksBelow)
        slider.setTickInterval(5)
        slider.setMinimumSize(300, 50)
        slider.valueChanged[int].connect(lambda:self.change_value(slider))

    def init_label(self, label):
        label.setText(str(self.init_value))
        label.setFont(QFont("Arial", 20))
        label.setStyleSheet("color: blue")
        label.setMinimumSize(80, 30)

    def init_ui(self):
        self.layout = QFormLayout()

        self.hbox1 = QHBoxLayout()
        self.init_label(self.label1)
        self.init_slider(self.input1, "input1")
        self.hbox1.addWidget(self.label1)
        self.hbox1.addWidget(self.input1)

        self.hbox2 = QHBoxLayout()
        self.init_label(self.label2)
        self.init_slider(self.input2, "input2")
        self.hbox2.addWidget(self.label2)
        self.hbox2.addWidget(self.input2)

        self.hbox3 = QHBoxLayout()
        self.hbox3.addWidget(self.add)
        self.hbox3.addWidget(self.subtract)
        self.hbox3.addWidget(self.mult)
        self.hbox3.addWidget(self.divide)
        self.add.clicked[bool].connect(self.update_result)
        self.subtract.clicked[bool].connect(self.update_result)
        self.mult.clicked[bool].connect(self.update_result)
        self.divide.clicked[bool].connect(self.update_result)

        self.hbox4 = QHBoxLayout()
        self.label_result = QLabel("Result", self)
        self.text_result = QLineEdit(self)
        self.text_result.setAlignment(Qt.AlignRight)
        self.text_result.setEnabled(False)
        self.text_result.setFont(QFont("Arial", 25))
        self.text_result.setMinimumSize(100, 25)
        self.text_result.setStyleSheet("QLineEdit {background-color: gray;color:yellow}")
        self.hbox4.addWidget(self.label_result)
        self.hbox4.addWidget(self.text_result)

        self.layout.addRow(self.hbox1)
        self.layout.addRow(self.hbox2)
        self.layout.addRow(self.hbox3)
        self.layout.addRow(self.hbox4)

        self.setLayout(self.layout)
        self.adjustSize()
        self.setWindowTitle('Simple Calculator')
        self.show()

    def change_value(self, slider):
        updated_value = slider.value()
        name = slider.objectName()
        if name == "input1":
            self.label1.setText(str(updated_value))
            self.input_value1 = updated_value
        elif name == "input2":
            self.label2.setText(str(updated_value))
            self.input_value2 = updated_value
        result = self.compute_result(
                self.input_value1, self.input_value2, self.op)
        self.text_result.setText(str(result))

    def update_result(self, pressed):
        source = self.sender()
        temp = self.active_source
        temp.setStyleSheet("QPushButton { background-color: white}")
        self.active_source = source
        self.active_source.setStyleSheet("QPushButton { background-color: rgb(100, 250, 100)}")
        self.input_value1 = self.input1.value()
        self.input_value2 = self.input2.value()
        self.op = source.text()
        self.text_result.setText(str(self.compute_result(
            self.input_value1, self.input_value2, self.op)))


    def compute_result(self, num1, num2, op):
        if op == "Add":
            return num1 + num2
        elif op == "Subtract":
            return num1 - num2
        elif op == "Multiply":
            return num1 * num2
        elif op == "Divide":
            if num2 != 0:
                return num1 / num2
            else:
                return None

def main():
    app = QApplication(sys.argv)
    ex = SimpleCalculator()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
