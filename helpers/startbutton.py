from PySide6.QtWidgets import * 
from PySide6.QtCore import Qt, Signal 
from PySide6.QtGui import QFont

class StartButton(QWidget):
    def __init__(self):
        super().__init__()

        self.btn = QPushButton("START")
        self.btn.resize(200, 55)
        self.btn.setFont(QFont('Arial Rounded MT Bold', 30))


