from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class CheckDemo(QWidget):
   def __init__(self, parent = None):
      super(CheckDemo, self).__init__(parent)

      layout = QHBoxLayout()
      self.b1 = QCheckBox("Button1")
      self.b1.setChecked(True)
      self.b1.stateChanged.connect(lambda:self.chk_state(self.b1))
      layout.addWidget(self.b1)

      self.b2 = QCheckBox("Button2")
      self.b2.toggled.connect(lambda:self.chk_state(self.b2))
      layout.addWidget(self.b2)

      self.setLayout(layout)
      self.setWindowTitle("checkbox demo")

   def chk_state(self,b):
         if b.isChecked() == True:
            print(b.text()+" is selected")
         else:
            print(b.text()+" is deselected")

def main():

   app = QApplication(sys.argv)
   ex = CheckDemo()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()
