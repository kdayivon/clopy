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
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update)

        self.end_time = None
        self.running = False

    def start(self, seconds):
        self.end_time = QDateTime.currentDateTime().addSecs(seconds)
        self.running = True

        self.started.emit()
        self.timer.start()

    def stop(self):
        self.timer.stop()
        self.running = False
        slelf.stopped.emit()

    def update(self):
        remaining = QDateTime.currentDateTime().secsTo(self.end_time)

        if remaining <= 0:
            remaining = 0
            self.time_changed.emit(remaining)

            self.stop()
            self.finished.emit()
            return
        self.time_changed.emit(remaining)


