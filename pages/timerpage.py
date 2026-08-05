from PySide6.QtWidgets import * 
from PySide6.QtCore import Qt, Signal 
from helpers.timedisplay import TimeDisplay

class TimerPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        layout.addWidget(TimeDisplay())

