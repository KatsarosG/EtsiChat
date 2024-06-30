from PySide6 import QtCore, QtWidgets, QtGui
import server

width = 800
height = 600

class ScrollLabel(QtWidgets.QScrollArea):
    # constructor
    def __init__(self, *args, **kwargs):
        QtWidgets.QScrollArea.__init__(self, *args, **kwargs)
 
        # making widget resizable
        self.setWidgetResizable(True)
 
        # making qwidget object
        content = QtWidgets.QWidget(self)
        self.setWidget(content)
 
        # vertical box layout
        lay = QtWidgets.QVBoxLayout(content)
 
        # creating label
        self.label = QtWidgets.QLabel(content)
 
        # setting alignment to the text
        #self.label.setAlignment(QtGui.Qt.AlignLeft | Qt.AlignTop)
 
        # making label multi-line
        self.label.setWordWrap(True)
 
        # adding label to the layout
        lay.addWidget(self.label)
 
    # the setText method
    def setText(self, text):
        # setting text to the label
        self.label.setText(text)

class ServerWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EtsiChat Server")
        self.resize(QtCore.QSize(width,height))

        #Declaration of buttons
        StartServerButton = QtWidgets.QPushButton("Start Server")
        StopServerButton = QtWidgets.QPushButton("Stop Server")

        #Cofigure Buttons
        StartServerButton.setFixedSize(200,20)
        StopServerButton.setFixedSize(200,20)
        
        #Declaration of chatbox Label
        global Console 
        Console = ScrollLabel(self)
        Console.setText("Console")
        '''
        Console = QtWidgets.QScrollArea
        Console.label =QtWidgets.QLabel("CONSOLE")
        Console.label.setStyleSheet("QLabel {color: black; background-color: silver; border: 1px solid gray; border-radius: 2px;}")
        Console.label.setWordWrap(True)
        '''
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

