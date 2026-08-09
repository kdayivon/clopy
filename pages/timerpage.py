from PySide6 import QtGui, QtCore
from PySide6.QtWidgets import * 
from PySide6.QtCore import Qt, Signal, QTime
from PySide6.QtGui import QFont, QCursor
from helpers.pomotimer import PomoTimer

class TimerPage(QWidget):
    def __init__(self):
        super().__init__()

        self.timer = PomoTimer()
        self.timer.set_time(30*60)

        self.dur = QLabel("00:30:00")
        self.dur.setFont(QFont('Arial Rounded MT Bold', 12))

        self.lbl = QLineEdit("00:30:00")
        self.lbl.setFont(QFont('Arial Rounded MT Bold', 100))
        self.lbl.setAlignment(Qt.AlignCenter)
        self.lbl.setFixedWidth(600)
        self.btn = QPushButton("START") 
        self.btn.setFixedSize(180, 60)
        self.btn.setFont(QFont('Arial Rounded MT Bold', 18))
        self.btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.reset = QPushButton("RESET")
        self.reset.setFixedSize(50, 40)
        self.reset.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.reset.setFont(QFont('Arial Rounded MT Bold'))
        self.reset.hide()

        self.end = QLabel("HH:MM")
        self.end.setFont(QFont('Arial Rounded MT Bold', 12))
        self.end.setStyleSheet("margin-top: 20px;")
        curr = QTime.currentTime()
        new_time = curr.addSecs(30*60)
        self.end.setText(f"{new_time.hour():02}:{new_time.minute():02}")

        btn_area = QWidget()
        btn_area.setFixedWidth(300)
        
        btn_layout = QGridLayout(btn_area)
        btn_layout.setContentsMargins(0, 0, 0, 0)
        btn_layout.addWidget(self.btn, 0, 1, Qt.AlignCenter)
        btn_layout.addWidget(self.reset, 0, 2, Qt.AlignRight)
        btn_layout.setColumnStretch(0, 1)
        btn_layout.setColumnStretch(2, 1)

        layout = QVBoxLayout(self)
        layout.addWidget(self.dur, 0, Qt.AlignCenter)
        layout.addWidget(self.lbl, 0, Qt.AlignCenter)
        layout.addWidget(btn_area, 0, Qt.AlignCenter)
        layout.addWidget(self.end, 0, Qt.AlignCenter)

        self.btn.clicked.connect(self.toggle_timer)
        self.reset.clicked.connect(self.reset_timer)
        self.lbl.returnPressed.connect(self.set_time)

        self.timer.time_changed.connect(self.update_display)
        self.timer.finished.connect(self.timer_finished)

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
                hours, minutes, seconds = map(int, text.split(":"))
                total_seconds = (hours*3600) + (minutes * 60) + seconds
                self.dur.setText(f"{hours:02}:{minutes:02}:{seconds:02}")
                curr = QTime.currentTime()
                new_time = curr.addSecs(total_seconds)
                self.end.setText(f"{new_time.hour():02}:{new_time.minute():02}")
            else:
                total_seconds = int(text) * 60
                self.dur.setText(f"00:{text:02}:00")
                curr = QTime.currentTime()
                new_time = curr.addSecs(total_seconds)
                self.end.setText(f"{new_time.hour():02}:{new_time.minute():02}")
            if total_seconds <= 0:
                total_seconds = 0
                self.dur.setText("00:00:00")
                curr = QTime.currentTime()
                self.end.setText(f"{curr.hour():02}:{curr.minute():02}")
        except ValueError:
            self.update_display(self.timer.remaining)
            self.dur.setText("00:00:00")
            curr = QTime.currentTime()
            self.end.setText(f"{curr.hour():02}:{curr.minute():02}")
            return 
        self.timer.set_time(total_seconds)
        self.update_display(self.timer.remaining)

    def toggle_timer(self):
        if self.timer.timer.isActive():
            self.timer.stop()
            self.btn.setText("START")
            self.reset.hide()
        else: 
            self.timer.start()
            self.btn.setText("PAUSE")
            self.reset.show()

    def reset_timer(self):
        if self.timer.timer.isActive():
            self.timer.stop()
            self.btn.setText("START")
            self.reset.hide()
            self.timer.reset()

        else: 
            self.timer.reset()
            self.btn.setText("START")
            self.reset.hide()

    def update_display(self, remaining):
        hours = remaining // 3600
        minutes = (remaining % 3600) // 60
        seconds = remaining % 60

        self.lbl.setText(f"{hours:02}:{minutes:02}:{seconds:02}")

    def timer_finished(self):
        pass

