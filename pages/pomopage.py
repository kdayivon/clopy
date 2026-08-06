from PySide6.QtWidgets import * 
from PySide6.QtCore import Qt, Signal 
from PySide6.QtGui import QFont
from helpers.timedisplay import TimeDisplay
from helpers.startbutton import StartButton
from helpers.pomotimer import PomoTimer

class PomodoroPage(QWidget):
    def __init__(self):
        super().__init__()

        self.pomo = PomoTimer()

        self.lbl = QLabel("50:00")
        self.lbl.setFont(QFont('Arial Rounded MT Bold', 100))
        self.btn = QPushButton("START") 
        self.btn.setFixedSize(180, 60)
        self.btn.setFont(QFont('Arial Rounded MT Bold', 18))

        layout = QVBoxLayout(self)

        layout.addWidget(self.lbl)
        layout.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.btn, 0, Qt.AlignCenter)

        self.btn.clicked.connect(self.start_timer)

        self.pomo.time_changed.connect(self.update_display)
        self.pomo.finished.connect(self.timer_finished)

        self.setStyleSheet("""
                    QLabel {
                        border: none;
                        color: #D4BE98;
                    }
                    QPushButton {
                        border: none;
                        color: #32302F;
                        background: #D4BE98; 
                        border-radius: 5px;
                    }
                """)

    def start_timer(self):
        self.pomo.start(50*60)

    def update_display(self, remaining):
        minutes = remaining // 60
        seconds = remaining % 60

        self.lbl.setText(f"{minutes:02}:{seconds:02}")

    def timer_finished(self):
        self.btn.setText("Done !")

