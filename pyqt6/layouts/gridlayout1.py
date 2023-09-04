import sys
from PyQt6.QtWidgets import QWidget, QGridLayout, QLineEdit, QApplication
from PyQt6.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        textEdit1 = QLineEdit("Line1")
        textEdit2 = QLineEdit("Line2")          
        textEdit3 = QLineEdit("Line3") 
        textEdit4 = QLineEdit("The whole line")    
        self.gridLayout = QGridLayout()
        self.gridLayout.addWidget(textEdit1, 0, 0) 
        self.gridLayout.addWidget(textEdit2, 0, 1)
        self.gridLayout.addWidget(textEdit3, 0, 2)  
        self.gridLayout.addWidget(textEdit4, 1, 0, 1, 3) 
        self.setLayout(self.gridLayout)
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()