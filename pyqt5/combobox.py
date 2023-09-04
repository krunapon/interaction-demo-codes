#!/usr/bin/python

"""
ZetCode PyQt5 tutorial

This example shows how to use
a QComboBox widget.

Author: Jan Bodnar
Website: zetcode.com
"""

import sys

from PyQt5.QtWidgets import (QWidget, QLabel,
                             QComboBox, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel('Khon Kaen University', self)
        combo = QComboBox(self)
        combo.addItem('Khon Kaen University')
        combo.addItem('Chulalongkorn University')
        combo.addItem('Chiang Mai University')
        combo.move(20, 30)
        self.lbl.move(30, 80)
        combo.activated[str].connect(self.onActivated)
        self.setMinimumSize(250, 100)
        self.setWindowTitle('QComboBox')
        self.show()

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
