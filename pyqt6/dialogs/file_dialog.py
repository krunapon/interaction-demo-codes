from PyQt6.QtWidgets import (QMainWindow, QTextEdit,
                             QFileDialog, QApplication)
from PyQt6.QtGui import QIcon, QAction
from pathlib import Path
import sys, os

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        path = os.path.dirname(__file__)
        os.chdir(path)
        openFile = QAction(QIcon('images/file-open.svg'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        self.menubar = self.menuBar()
        self.menubar.setNativeMenuBar(False)
        fileMenu = self.menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 550, 450)
        self.setWindowTitle('File dialog')
        self.show()

    def showDialog(self):
        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)
    

        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
    