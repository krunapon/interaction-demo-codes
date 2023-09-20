from PyQt6.QtCore import pyqtProperty, QObject

class CustomObject(QObject):
    def __init__(self):
        super().__init__()
        self._value = 0        # the default value

    def getValue(self):
        return self._value

    def setValue(self, value):
        self._value = value

    value = pyqtProperty(int, getValue, setValue)
    
obj = CustomObject()
obj.value = 7
print(obj.value)