import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ku.ziku import *
from ku.ziku_z import *
from ku.ci_2 import *
from ku.ci_3 import *
from ku.ci_4x import *


class LinuxInput_gui(QWidget):
		
    def __init__(self):
		
        super(LinuxInput_gui, self).__init__()
        font = QFont()
        font.setPointSize(14)
        self.setStyleSheet('font-size: 14pt; font-family: Courier;')
        self.initUI()
        self.zi = [zi, c2, c3, c4x]
        self.fzi = fzi 
        
    def initUI(self):
        
        self.sinput = QPushButton('Input')
        self.soutput= QPushButton('Output')   
        self.schoose = QPushButton('Choose')
        self.sabout = QPushButton('About')          
        self.lE1 = QLineEdit()
        self.lE2 = QLineEdit()
        self.lE3 = QLineEdit()
        self.tEx = QTextEdit()
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.sinput, 1, 0)   
        grid.addWidget(self.soutput, 2, 0)
        grid.addWidget(self.schoose, 3, 0)
        grid.addWidget(self.sabout, 4, 0)
        grid.addWidget(self.lE1, 1, 1, 1, 1)
        grid.addWidget(self.lE2, 2, 1, 1, 1)  
        grid.addWidget(self.lE3, 3, 1, 1, 1) 
        grid.addWidget(self.tEx, 4, 1, 2, 1) 

        self.lE3.installEventFilter(self)
        #self.lE3.textEdited.connect(self.showCurrentText)
        self.setLayout(grid) 
        self.setWindowTitle('LinuxInput_gui')
        self.sinput.clicked.connect(self.inputButton)
        self.soutput.clicked.connect(self.outputButton)
        self.sabout.clicked.connect(self.aboutButton)
        self.lE1.returnPressed.connect(self.search_slot)
        self.lE2.returnPressed.connect(self.search_slot1)

    def eventFilter(self, source, event):
        if (event.type() == QEvent.KeyPress and source is self.lE3):
            if event.text() == '\r':
                if self.lE3.text() == "":
                    #self.tEx.setPlainText(self.first_entry[0])
                    #self.tEx.append(self.first_entry[0])
                    self.tEx.insertPlainText(self.l[0])
                    self.lE3.setFocus() 
                else:
                    t1 = int(self.lE3.text())
                    #self.tEx.setPlainText(t1)
                    #self.tEx.append(t1)
                    self.tEx.insertPlainText(self.l[t1 - 1])
             
                self.lE3.setText("")
                self.lE1.setText("")
                self.lE1.setFocus()
                 
        #print('key press:', (event.key(), event.text()))
        return super(LinuxInput_gui, self).eventFilter(source, event)
    
    def showCurrentText(self, text):
        print('current-text:', text)

        
    def search_slot(self):
        
        pin = self.lE1.text().strip()
        o = pin .count(' ')
        if o > 3:
            o = 3
        if pin[-1] == '.':
            pin = pin[:-1]
            self.l = self.fzi.get(pin)    
            
        else:
            self.l = self.zi[o].get(pin)
        
        if self.l is not None and len(self.l):
            first_entry1 = "".join(list(map(lambda x: str(self.l.index(x) + 1) + "." + x, self.l)))
            self.lE2.setText(' '.join(first_entry1))
            self.lE3.setFocus()

    def search_slot1(self):
                
        pass

    def inputButton(self):
                
        pass
     
    def outputButton(self):
                
        pass
        
    def chooseButton(self):		
        
        pass

    def aboutButton(self):
		
        QMessageBox.about(self, "Thanks for use Linux-input",
                "<p>Contact mt.kongtong@gmail.com</p>")        
        
        
def main():    

    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("gtk"))
    widget = LinuxInput_gui()
    widget.resize(520, 640) 
    qr = widget.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    widget.move(qr.topLeft())		
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
