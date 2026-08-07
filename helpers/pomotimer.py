from PySide6.QtCore import QObject, QTimer, Signal
from PySide6.QtCore import QDateTime

class PomoTimer(QObject):
    time_changed = Signal(int)
    started = Signal()
    stopped = Signal()
    finished = Signal()
    
    def __init__(self):
        super().__init__()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.remaining = 50*60

        self.end_time = None
        self.running = False

    def set_time(self, seconds):
        self.remaining = seconds 

    def start(self):
        self.running = True

        self.timer.start(1000)
        self.started.emit()

    def stop(self):
        self.timer.stop()
        self.running = False
        self.stopped.emit()

    def update(self):
        if self.remaining > 0:
            self.remaining -= 1
            self.time_changed.emit(self.remaining)

        if self.remaining == 0:
            self.timer.stop()
            self.finished.emit()




