from PySide6.QtWidgets import * 
from PySide6.QtCore import Qt, Signal 

class TopBar(QWidget):
    page_i = Signal(int)

    def __init__(self):
        super().__init__()

        page_layout = QHBoxLayout(self)
        page_layout.setContentsMargins(0, 0, 0, 0)
        page_layout.setSpacing(0)

        self.group = QButtonGroup(self)
        self.group.setExclusive(True)

        self.pomo_btn = QPushButton("Pomodoro")
        self.pomo_btn.setCheckable(True)
        
        self.timer_btn = QPushButton("Timer")
        self.timer_btn.setCheckable(True)

        self.watch_btn = QPushButton("Stopwatch")
        self.watch_btn.setCheckable(True)
        
        self.group.addButton(self.pomo_btn, 0)
        self.group.addButton(self.timer_btn, 1)
        self.group.addButton(self.watch_btn, 2)
        self.group.idClicked.connect(self.page_i.emit)
        
        page_layout.addWidget(self.pomo_btn)
        page_layout.addWidget(self.timer_btn)
        page_layout.addWidget(self.watch_btn)

        self.set_curr_page(0)

    def set_curr_page(self, index):
        self.pomo_btn.setChecked(index == 0)
        self.timer_btn.setChecked(index == 1)
        self.watch_btn.setChecked(index == 2)

