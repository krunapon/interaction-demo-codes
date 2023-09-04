import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        menubar = self.menuBar()
        # need to have this statement if you use Mac OS
        menubar.setNativeMenuBar(False)


        imp_menu = QMenu('Import', self)
        imp_act = QAction('Import mail', self)

        imp_menu.addAction(imp_act)

        file_menu = menubar.addMenu('File')
        new_act = QAction('New', self)

        file_menu.addAction(new_act)
        file_menu.addMenu(imp_menu)

        exit_act = QAction(QIcon('app-icon.png'), 'Exit', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.setStatusTip('Exit application')
        exit_act.triggered.connect(QApplication.instance().quit)

        file_menu.addAction(exit_act)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Simple menu')

        # self.statusBar().showMessage('Ready')
        self.statusBar().addPermanentWidget(QLabel('Ready'), 1)

        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
