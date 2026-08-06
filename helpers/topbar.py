from PySide6.QtWidgets import * 
from PySide6.QtCore import Qt, Signal 
from PySide6.QtGui import QFont

class TopBar(QWidget):
    page_i = Signal(int)

    def __init__(self):
        super().__init__()

        page_layout = QHBoxLayout(self)
        page_layout.setContentsMargins(0, 0, 0, 0)
        page_layout.setSpacing(0)
        page_layout.setAlignment(Qt.AlignCenter)

        self.group = QButtonGroup(self)
        self.group.setExclusive(True)

        self.pomo_btn = QPushButton("Pomodoro")
        self.pomo_btn.setCheckable(True)
        self.pomo_btn.setFixedSize(115, 35)
        self.pomo_btn.setContentsMargins(0, 0, 0, 0)
        self.pomo_btn.setFont(QFont('Arial Rounded MT Bold', 12))
        
        self.timer_btn = QPushButton("Timer")
        self.timer_btn.setCheckable(True)
        self.timer_btn.setFixedSize(120, 35)
        self.timer_btn.setContentsMargins(0, 0, 0, 0)
        self.timer_btn.setFont(QFont('Arial Rounded MT Bold', 12))

        self.watch_btn = QPushButton("Stopwatch")
        self.watch_btn.setCheckable(True)
        self.watch_btn.setFixedSize(120, 35)
        self.watch_btn.setContentsMargins(0, 0, 0, 0)
        self.watch_btn.setFont(QFont('Arial Rounded MT Bold', 12))
        
        self.group.addButton(self.pomo_btn, 0)
        self.group.addButton(self.timer_btn, 1)
        self.group.addButton(self.watch_btn, 2)
        self.group.idClicked.connect(self.page_i.emit)
        
        page_layout.addWidget(self.pomo_btn)
        page_layout.addWidget(self.timer_btn)
        page_layout.addWidget(self.watch_btn)

        self.set_curr_page(0)
        self.setStyleSheet("""
                    QPushButton {
                        border: none;
                        background: transparent;
                        color: #D4BE98;
                    }
                    QPushButton:hover {
                        background: transparent;
                    }
                    QPushButton:checked {
                        background: rgba(0, 0, 0, 0.15);
                        border-radius: 5px;
                    }
                """)

    def set_curr_page(self, index):
        self.pomo_btn.setChecked(index == 0)
        self.timer_btn.setChecked(index == 1)
        self.watch_btn.setChecked(index == 2)

