from PySide6 import QtCore, QtWidgets, QtGui
import clientGui as gui
import sys

app = QtWidgets.QApplication([])

if __name__ == "__main__":
    widget = gui.MyWidget()
    #widget.setSize(width,height)
    widget.show()
    sys.exit(app.exec())
