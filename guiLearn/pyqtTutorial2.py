from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys


#sub QMainWindow into out own class called MainWindow
#MainWindow is QMainWindow's parent class
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs): #takes the arguments and keyword arguments and pass into __init__ to the parent class
        super(MainWindow, self).__init__(*args, **kwargs)#you must always call the super init function when you subclass a qt class

        self.setWindowTitle("My awesome app")

        label = QLabel("This is awesome")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)#allows you to set the widget that goes in the middle of the windoe

#create QApplication instance
app = QApplication(sys.argv)#sys.argv allows us to pass command line arguments into out application


window = MainWindow()#this creates the window instance
window.show()#this is important as this shows the actual window

app.exec_() #this calls the event loop