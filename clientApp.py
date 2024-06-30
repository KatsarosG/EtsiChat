from PySide6 import QtCore, QtWidgets, QtGui
import clientGui
import sys

app = QtWidgets.QApplication([])

if __name__ == "__main__":
    widget = clientGui.ClientWindow()
    widget.show()
    sys.exit(app.exec())
