from PySide6 import QtGui, QtCore
from PySide6.QtWidgets import * 
from PySide6.QtCore import Qt, Signal 
from PySide6.QtGui import QFont, QCursor
from helpers.timedisplay import TimeDisplay
from helpers.startbutton import StartButton
from helpers.pomotimer import PomoTimer

class PomodoroPage(QWidget):
    def __init__(self):
        super().__init__()

        self.pomo = PomoTimer()
        self.mode = "pomodoro"

        self.lbl = QLineEdit("50:00")
        self.lbl.setFont(QFont('Arial Rounded MT Bold', 100))
        self.lbl.setAlignment(Qt.AlignCenter)
        self.lbl.setFixedWidth(500)
        self.btn = QPushButton("START") 
        self.btn.setFixedSize(180, 60)
        self.btn.setFont(QFont('Arial Rounded MT Bold', 18))
        self.btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.iter = QLabel("#1")
        self.iter.setFont(QFont('Arial Rounded MT Bold', 12))
        self.iter.setStyleSheet("margin-top: 20px;")
        self.counter = 1

        layout = QVBoxLayout(self)

        layout.addWidget(self.lbl)
        layout.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.btn, 0, Qt.AlignCenter)
        layout.addWidget(self.iter, 0, Qt.AlignCenter)

        self.btn.clicked.connect(self.toggle_timer)
        self.lbl.returnPressed.connect(self.set_time)

        self.pomo.time_changed.connect(self.update_display)
        self.pomo.finished.connect(self.timer_finished)

        self.setStyleSheet("""
                    QLineEdit {
                        border: none;
                        color: #D4BE98;
                        background: transparent;
                    }
                    QPushButton {
                        border: none;
                        color: #32302F;
                        background: #D4BE98; 
                        border-radius: 5px;
                    }
                    QLabel {
                        border: none;
                        color: #D4BE98;
                        background: transparent;
                    }
                """)
    def set_time(self):
        text = self.lbl.text().strip()
        try:
            if ":" in text:
                minutes, seconds = map(int, text.split(":"))
                total_seconds = minutes * 60 + seconds
            else:
                total_seconds = int(text) * 60
            if total_seconds <= 0:
                total_seconds = 0
        except ValueError:
            self.update_display(self.pomo.remaining)
            return 
        self.pomo.set_time(total_seconds)
        self.update_display(self.pomo.remaining)

    def toggle_timer(self):
        if self.pomo.timer.isActive():
            self.pomo.stop()
            self.btn.setText("START")
            self.btn.setFixedHeight(60)
            self.btn.setStyleSheet("margin-top: 0px;")
        else: 
            self.pomo.start()
            self.btn.setText("PAUSE")
            self.btn.setStyleSheet("margin-top: 10px;")

    def update_display(self, remaining):
        minutes = remaining // 60
        seconds = remaining % 60

        self.lbl.setText(f"{minutes:02}:{seconds:02}")

    def timer_finished(self):
        if self.mode == "pomodoro":
            self.mode = "break"
            self.pomo.remaining = self.pomo.break_dur
        else:
            self.mode = "pomodoro"
            self.pomo.remaining = self.pomo.pomo_dur
            self.counter += 1
            self.iter.setText(f"#{self.counter}")

        self.pomo.time_changed.emit(self.pomo.remaining)
        self.update_display(self.pomo.remaining)
        self.btn.setText("START")

