from PySide6 import QtCore, QtWidgets, QtGui
import server
from datetime import datetime

width = 800
height = 600

class ServerWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EtsiChat Server")
        self.resize(QtCore.QSize(width,height))

        #Declaration of buttons
        StartServerButton = QtWidgets.QPushButton("Start Server")
        StopServerButton = QtWidgets.QPushButton("Stop Server")

        #Cofigure Buttons
        StartServerButton.setFixedSize(200,30)
        StopServerButton.setFixedSize(200,30)
        
        #Declaration of chatbox Label
        global Console
        Console = QtWidgets.QTextEdit("Console")
        #Console.setText("Console")
        Console.setReadOnly(True)
        #console = Console

        #Declaration of application Layouts
        outerLayout = QtWidgets.QHBoxLayout(self)
        menuLayout = QtWidgets.QVBoxLayout()
        outputLayout = QtWidgets.QVBoxLayout()

        #Placement of widgets to the coresponding layouts
        outputLayout.addWidget(Console)
        menuLayout.addWidget(StartServerButton)
        menuLayout.addWidget(StopServerButton)
        outerLayout.addLayout(menuLayout)
        outerLayout.addLayout(outputLayout)

        menuLayout.insertSpacing(-1,height*0.9)

        #Declaration of the functions that get called by the buttons
        #...

        #Calling of above functions at the event of a clicked button
        StartServerButton.clicked.connect(server.startServer)
        StopServerButton.clicked.connect(server.stopServer)

    def closeEvent(self, event):
        server.stopServer()
'''
    global consoleWrite
    def consoleWrite(text):
        print(text)
        newConsoleText = str(Console.toPlainText() + '\n' + str(datetime.now()) + " >> " + text)
        ServerWidget.Console.setPlainText(newConsoleText)
'''
