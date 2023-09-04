import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class Exercise2(QMainWindow):
    def __init__(self, name):
        super().__init__()
        self.init_ui(name)

    def init_ui(self, name):
        menubar = self.menuBar()
        # need to have this statement if you use Mac OS
        menubar.setNativeMenuBar(False)

        file_menu = menubar.addMenu('File')
        new_act = QAction('New', self)

        file_menu.addAction(new_act)

        edit_menu = QMenu('Edit', self)
        copy_act = QAction('Copy', self)
        paste_act = QAction('Paste', self)
        edit_menu.addAction(copy_act)
        edit_menu.addAction(paste_act)
        file_menu.addMenu(edit_menu)

        save_act = QAction('Save', self)
        save_act.setShortcut('Ctrl+S')
        file_menu.addAction(save_act)

        exit_act = QAction(QIcon('app-icon.png'), 'Quit', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.setStatusTip('Exit application')
        exit_act.triggered.connect(QApplication.instance().quit)
        file_menu.addAction(exit_act)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Exercise 2')

        self.statusBar().addPermanentWidget(QLabel('By ' + name), 1)

        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Exercise2(sys.argv[1])
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
