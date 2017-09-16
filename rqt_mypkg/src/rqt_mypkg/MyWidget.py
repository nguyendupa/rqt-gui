from python_qt_binding.QtWidgets import QWidget, QToolTip,QPushButton
from python_qt_binding.QtGui import QFont,QPalette, QColor

class MyWidget(QWidget):
    
    def __init__(self):
        super(MyWidget, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        QToolTip.setFont(QFont('SansSerif', 10))
        
        self.setToolTip('This is a <b>QWidget</b> widget')
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(100,100,255))
        self.setPalette(p)

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)  

        btn2 = QPushButton('Button', self)
        btn2.setToolTip('This is a <b>QPushButton 2</b> widget')
        btn2.resize(btn.sizeHint())
        btn2.move(50, 150)      
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Tooltips Test Noob')
        self.show()