from PySide6 import QtGui, QtCore
from PySide6.QtWidgets import * 
from PySide6.QtCore import Qt, Signal 
from PySide6.QtGui import QFont, QCursor
from helpers.stopwatch import StopWatch

class StopWatchPage(QWidget):
    def __init__(self):
        super().__init__()

        self.stopwatch = StopWatch()

        self.lbl = QLabel("00:00:00")
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
        self.reset.setStyleSheet("background: #EA6962;")
        self.reset.hide()

        btn_area = QWidget()
        btn_area.setFixedWidth(300)
        
        btn_layout = QGridLayout(btn_area)
        btn_layout.setContentsMargins(0, 0, 0, 0)
        btn_layout.addWidget(self.btn, 0, 1, Qt.AlignCenter)
        btn_layout.addWidget(self.reset, 0, 2, Qt.AlignRight)
        btn_layout.setColumnStretch(0, 1)
        btn_layout.setColumnStretch(2, 1)

        layout = QVBoxLayout(self)
        layout.addWidget(self.lbl, 0, Qt.AlignCenter)
        layout.addWidget(btn_area, 0, Qt.AlignCenter)

        self.stopwatch.time_changed.connect(self.update_display)
        self.btn.clicked.connect(self.toggle_watch)
        self.reset.clicked.connect(self.reset_watch)
        self.setStyleSheet("""
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

    def toggle_watch(self):
        if self.stopwatch.stopwatch.isActive():
            self.stopwatch.stop()
            self.btn.setText("START")
            self.reset.show()
        else: 
            self.stopwatch.start()
            self.btn.setText("PAUSE")
            self.reset.show()
    
    def reset_watch(self):
        if self.stopwatch.stopwatch.isActive():
            self.stopwatch.stop()
            self.btn.setText("START")
            self.reset.hide()
            self.stopwatch.reset()

        else: 
            self.stopwatch.reset()
            self.btn.setText("START")
            self.reset.hide()


    def update_display(self, ms):
        total_seconds = ms // 1000
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        
        self.lbl.setText(f"{hours:02}:{minutes:02}:{seconds:02}")


