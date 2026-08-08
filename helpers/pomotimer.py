from PySide6.QtCore import QObject, QTimer, Signal
from PySide6.QtCore import QDateTime

class PomoTimer(QObject):
    time_changed = Signal(int)
    finished = Signal()
    
    def __init__(self, pomo_min=50, break_min=10):
        super().__init__()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.pomo_dur = pomo_min * 60
        self.break_dur = break_min * 60
        self.remaining = self.pomo_dur

        self.end_time = None
        self.running = False

    def set_time(self, seconds):
        self.pomo_dur = seconds 
        self.remaining = seconds
        self.time_changed.emit(self.remaining)

    def start(self):
        self.running = True

        self.timer.start(1000)

    def stop(self):
        self.timer.stop()
        self.running = False

    def update(self):
        if self.remaining > 0:
            self.remaining -= 1
            self.time_changed.emit(self.remaining)

        if self.remaining == 0:
            self.timer.stop()
            self.finished.emit()




