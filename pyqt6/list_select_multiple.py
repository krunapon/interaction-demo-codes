from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QAbstractItemView, QDialog

class ListSelectMultiple(QDialog):
    def __init__(self, parent=None):
        super(ListSelectMultiple, self).__init__(parent)
        self.layout = QtWidgets.QVBoxLayout()
        self.listWidget = QtWidgets.QListWidget()
        self.listWidget.setSelectionMode(
            QAbstractItemView.SelectionMode.MultiSelection
        )
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 211, 291))
        for i in range(10):
            item = QtWidgets.QListWidgetItem(f"Item {i+1}")
            self.listWidget.addItem(item)
        self.listWidget.itemClicked.connect(self.printItemText)
        self.layout.addWidget(self.listWidget)
        self.setLayout(self.layout)

    def printItemText(self):
        items = self.listWidget.selectedItems()
        x = []
        for i in range(len(items)):
            x.append(str(self.listWidget.selectedItems()[i].text()))
        print (x)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form = ListSelectMultiple()
    form.show()
    app.exec()