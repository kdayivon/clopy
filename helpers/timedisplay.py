from PySide6.QtWidgets import * 
from PySide6.QtCore import Qt, Signal 

class TimeDisplay(QWidget):
    def __init__(self):
        super().__init__()

        time_layout = QHBoxLayout(self)
        time_layout.setContentsMargins(0, 0, 0, 0)
        time_layout.setSpacing(0)

        self.lbl = QLabel("T I M E")
        self.lbl.setAlignment(Qt.AlignCenter)
        time_layout.addWidget(self.lbl)

