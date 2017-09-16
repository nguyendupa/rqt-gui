from python_qt_binding.QtWidgets import QWidget, QToolTip,QPushButton
from python_qt_binding.QtGui import QFont

class MyWidget(QWidget):
    
    def __init__(self):
        super(MyWidget, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setWindowTitle('Not bag')
        self.setToolTip('This is a <b>QWidget</b> widget')
        
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)       
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Tooltips')    
        self.show()