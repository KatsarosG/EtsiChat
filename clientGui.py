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
        SendMessageButton = QtWidgets.QPushButton("Send")

        #Cofigure Buttons
        ConnectButton.setFixedSize(200,30)
        StartServerButton.setFixedSize(200,30)
        SendMessageButton.setFixedSize(50,30)
        
        #Declaration of chatbox Label
        global ChatBox
        ChatBox = QtWidgets.QTextEdit()
        ChatBox.setReadOnly(True)
        #ChatBox.setStyleSheet("QLabel {color: black; background-color: silver; border: 1px solid gray; border-radius: 2px;}")
        global MessageBox
        MessageBox = QtWidgets.QTextEdit()
        MessageBox.setFixedHeight(60)

        #Declaration of application Layouts
        outerLayout = QtWidgets.QHBoxLayout(self)
        menuLayout = QtWidgets.QVBoxLayout()
        chatLayout = QtWidgets.QVBoxLayout()
        messageBoxLayout = QtWidgets.QHBoxLayout()

        #Placement of widgets to the coresponding layouts
        chatLayout.addWidget(ChatBox)
        messageBoxLayout.addWidget(MessageBox)
        messageBoxLayout.addWidget(SendMessageButton)
        menuLayout.addWidget(ConnectButton)
        menuLayout.addWidget(StartServerButton)
        chatLayout.addLayout(messageBoxLayout)
        outerLayout.addLayout(menuLayout)
        outerLayout.addLayout(chatLayout)

        menuLayout.insertSpacing(-1,height*0.9)

        #Declaration of the functions that get called by the buttons
        def startServerApp() :
            self.serverWidget = serverGui.ServerWidget()
            self.serverWidget.show()

        def connectToServer():
            try:
                host, ok = QtWidgets.QInputDialog.getText(self, 'Server Address', 'Server Address:', text='127.0.0.1')
                if ok and host:
                    port, ok = QtWidgets.QInputDialog.getText(self, 'Server port', 'Server port\n(Default: 13121)', text='13121')
                    if ok and host: 
                        while True:
                            inputUsername, ok = QtWidgets.QInputDialog.getText(self, 'Username', 'Enter your username\n(Must be at least 4 characters)')
                            if ok and len(inputUsername)>=4:
                                client.username = inputUsername 
                                client.connectToServer(host, port)
                                break
            except:
                errMsg = QtWidgets.QMessageBox()
                errMsg.setText('Error: Connection Refused\nCheck server address and port. If error persist contact server administrator.')
                errMsg.exec_()

        #Calling of above functions at the event of a clicked button
        ConnectButton.clicked.connect(connectToServer)
        StartServerButton.clicked.connect(startServerApp)
        SendMessageButton.clicked.connect(client.sendMessage)

    def closeEvent(self, event):
        client.recieveFlag = False
