from PySide6.QtWidgets import * 
from PySide6.QtCore import Qt, Signal 

class StartButton(QWidget):
    def __init__(self):
        super().__init__()

        btn_layout = QHBoxLayout(self)
        btn_layout.setContentsMargins(0, 0, 0, 0)
        btn_layout.setSpacing(0)

        self.btn = QPushButton("START")
        btn_layout.addWidget(self.btn)

