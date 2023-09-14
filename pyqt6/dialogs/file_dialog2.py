from PyQt6.QtWidgets import (QMainWindow, QTextEdit,
        QFileDialog, QApplication)
from PyQt6.QtGui import QIcon, QAction
from pathlib import Path
from functools import partial
import sys
import os


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        path = os.path.dirname(__file__)
        os.chdir(path)
        openFile = QAction(QIcon('images/file-open.svg'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open File')
        # open file dialog with the home directory
        openFile.triggered.connect(partial(self.showOpenDialog, str(Path.home())))
        saveFile = QAction(QIcon('images/file-save.png'), 'Save', self)
        saveFile.setShortcut('Ctrl+S')
        saveFile.setStatusTip('Save File')
        # save file dialog with the directory of the current file
        saveFile.triggered.connect(partial(self.showSaveDialog, path))
        

        self.menubar = self.menuBar()
        self.menubar.setNativeMenuBar(False)
        fileMenu = self.menubar.addMenu('&File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)

        self.setGeometry(300, 300, 550, 450)
        self.setWindowTitle('File dialog')
        self.show()

    def showOpenDialog(self, dir):
        fname = QFileDialog.getOpenFileName(self, 'Open file', dir)
        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)
                
    def showSaveDialog(self, dir):
        fname = QFileDialog.getSaveFileName(self, 'Save file', dir)
        if fname[0]:
            with open(fname[0], "w") as file:
                file.write(self.textEdit.toPlainText())
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
    