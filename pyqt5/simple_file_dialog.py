from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from pathlib import Path


class SimpleFileDialog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.fgColor = "black"
        self.bgColor = "white"

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.showOpenFileDialog)

        saveFile = QAction(QIcon('save.png'), 'Save', self)
        saveFile.setShortcut('Ctrl+S')
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.showSaveFileDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)

        editColor = QMenu('Color', self)
        editBgColor = QAction('Background color', self)
        editBgColor.triggered.connect(self.showColorDialog)
        editFgColor = QAction('Foreground color', self)
        editFgColor.triggered.connect(self.showColorDialog)
        editColor.addAction(editBgColor)
        editColor.addAction(editFgColor)

        editFont = QAction('Font', self)
        editFont.triggered.connect(self.showFontDialog)

        editMenu = menubar.addMenu('Edit')
        editMenu.addMenu(editColor)
        editMenu.addAction(editFont)

        self.setGeometry(300, 300, 550, 450)
        self.setWindowTitle('File dialog')
        self.show()

    def showOpenFileDialog(self):
        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)
        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)

    def showSaveFileDialog(self):
        home_dir = str(Path.home())
        fname = QFileDialog.getSaveFileName(self, 'Save file', home_dir)
        if fname[0]:
            f = open(fname[0], 'w')
            with f:
                data = self.textEdit.toPlainText()
                f.write(data)

    def showColorDialog(self):
        source = self.sender()
        col = QColorDialog().getColor()
        source_type = source.text()
        if col.isValid():
            if source_type == "Background color":
                self.bgColor = col.name()
            elif source_type == "Foreground color":
                self.fgColor = col.name()
            self.textEdit.setStyleSheet('QWidget { color: %s; background-color: %s }'
                                        % (self.fgColor, self.bgColor))

    def showFontDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)


def main():
    app = QApplication(sys.argv)
    ex = SimpleFileDialog()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
