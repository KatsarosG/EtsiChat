from PySide6 import QtCore, QtWidgets, QtGui
import client

width = 800
height = 600

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EtsiChat")
        self.resize(QtCore.QSize(width,height))

        #Declaration of buttons
        ConnectButton = QtWidgets.QPushButton("Connect to server")

        #Cofigure Buttons
        ConnectButton.setFixedSize(200,20)
        
        #Declaration of chatbox Label
        global ChatBox
        ChatBox = QtWidgets.QLabel("ChatBox")
        ChatBox.setStyleSheet("QLabel {color: black; background-color: silver; border: 1px solid gray; border-radius: 2px;}")

        #Declaration of application Layouts
        outerLayout = QtWidgets.QHBoxLayout(self)
        menuLayout = QtWidgets.QVBoxLayout()
        chatLayout = QtWidgets.QVBoxLayout()

        #Placement of widgets to the coresponding layouts
        chatLayout.addWidget(ChatBox)
        menuLayout.addWidget(ConnectButton)
        outerLayout.addLayout(menuLayout)
        outerLayout.addLayout(chatLayout)

        #Declaration of the functions that get called by the buttons
        #...

        #Calling of above functions at the event of a clicked button
        ConnectButton.clicked.connect(client.connectToServer)
