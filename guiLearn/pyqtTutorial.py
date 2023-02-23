from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

#this laptop resolution is 1366x768 

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.intiUI()

    def intiUI(self):


        self.setGeometry(200, 200, 300, 300)
    #               xpos,yos,width,height  0,0 is just the top right corner
        self.setWindowTitle("This is the title")

        self.label = QtWidgets.QLabel(self)#this is where the lable will be
        self.label.setText("my first lable")
        self.label.move(50,50)#where the lable will show

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("click me")
        self.b1.clicked.connect(self.clicked)


        #self.b2 = QtWidgets.QPushButton(self)
        #self.b2.setText("this is another button")
        #self.b2.clicked.connect(self.clicked)
        #self.b2.move(150,150)
    def clicked(self):
        self.label.setText("You pressed the button")
        self.update()

    def update(self):
        self.label.adjustSize()

#def clicked():
 #   print("clicked")

#def click():
#    print("click me again")


def window():
    app = QApplication(sys.argv)
    
    win = MyWindow()
    
    #win = QMainWindow()
    #win.setGeometry(200, 200, 300, 300)
    #               xpos,yos,width,height  0,0 is just the top right corner
    #win.setWindowTitle("This is the title")


    

    win.show() #this will actually show the window
    #makes sure windows will exit, and leave when we click x button
    sys.exit(app.exec_())

window()#basically just calls the function to show the window