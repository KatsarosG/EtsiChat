from PySide6 import QtCore, QtWidgets, QtGui
import client
import server
import serverGui
#import serverApp

width = 800
height = 600

class ClientWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EtsiChat")
        self.resize(QtCore.QSize(width,height))

        #Declaration of buttons
        ConnectButton = QtWidgets.QPushButton("Connect To Existing Server")
        StartServerButton = QtWidgets.QPushButton("Start New Server")

        #Cofigure Buttons
        ConnectButton.setFixedSize(200,20)
        StartServerButton.setFixedSize(200,20)
        
        #Declaration of chatbox Label
        global ChatBox
        ChatBox = QtWidgets.QTextEdit("ChatBox")
        ChatBox.setReadOnly(True)
        #ChatBox.setStyleSheet("QLabel {color: black; background-color: silver; border: 1px solid gray; border-radius: 2px;}")

        #Declaration of application Layouts
        outerLayout = QtWidgets.QHBoxLayout(self)
        menuLayout = QtWidgets.QVBoxLayout()
        chatLayout = QtWidgets.QVBoxLayout()

        #Placement of widgets to the coresponding layouts
        chatLayout.addWidget(ChatBox)
        menuLayout.addWidget(ConnectButton)
        menuLayout.addWidget(StartServerButton)
        outerLayout.addLayout(menuLayout)
        outerLayout.addLayout(chatLayout)

        menuLayout.insertSpacing(-1,height*0.9)

        #Declaration of the functions that get called by the buttons
        def startServerApp() :
            self.serverWidget = serverGui.ServerWidget()
            self.serverWidget.show()

        #Calling of above functions at the event of a clicked button
        ConnectButton.clicked.connect(client.connectToServer)
        StartServerButton.clicked.connect(startServerApp)
