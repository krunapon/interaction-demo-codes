from PyQt6.QtWidgets import QApplication,QWidget,QTextEdit,QVBoxLayout,QPushButton
import sys

class TextEditDemo(QWidget):
        def __init__(self,parent=None):
                super().__init__(parent)

                self.setWindowTitle("QTextEdit")
                self.resize(300,270)

                self.textEdit = QTextEdit()
                self.plainTxtBtn = QPushButton("Edit with plain text")
                self.htmlBtn = QPushButton("Edit with html")

                layout = QVBoxLayout()
                layout.addWidget(self.textEdit)
                layout.addWidget(self.plainTxtBtn)
                layout.addWidget(self.htmlBtn)
                self.setLayout(layout)

                self.plainTxtBtn.clicked.connect(self.plainTxtBtnClicked)
                self.htmlBtn.clicked.connect(self.htmlBtnClicked)

        def plainTxtBtnClicked(self):
                self.textEdit.setPlainText("Hello PyQt6!\nfrom DME KKU students")

        def htmlBtnClicked(self):
                self.textEdit.setHtml("<font color='blue' size='12'>Hello PyQt6!\nfrom <b>DME</b> KKU students</font>")

if __name__ == '__main__':
        app = QApplication(sys.argv)
        win = TextEditDemo()
        win.show()
        sys.exit(app.exec())