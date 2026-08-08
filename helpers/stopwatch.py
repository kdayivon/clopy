from PySide6.QtCore import QObject, QTimer, Signal, QElapsedTimer 

class StopWatch(QObject):
    time_changed = Signal(int)

    def __init__(self):
        super().__init__()

        self.time = 0
        self.clock = QElapsedTimer()
        self.stopwatch = QTimer()
        self.stopwatch.timeout.connect(self.update)

    def start(self):
        self.clock.start()
        self.stopwatch.start(50)

    def stop(self):
        if self.stopwatch.isActive():
            self.time += self.clock.elapsed()
        self.stopwatch.stop()

    def reset(self):
        self.stopwatch.stop()
        self.time = 0
        self.time_changed.emit(0)

    def update(self):
        current = self.time + self.clock.elapsed()
        self.time_changed.emit(current)
