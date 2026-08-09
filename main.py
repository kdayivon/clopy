from PySide6.QtWidgets import * 
from PySide6.QtCore import Qt, Signal 
from helpers.topbar import TopBar 
from pages.pomopage import PomodoroPage 
from pages.timerpage import TimerPage 
from pages.watchpage import StopWatchPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        container = QWidget()
        self.setCentralWidget(container)
        container.setStyleSheet("background-color: #3C3836;")

        layout = QVBoxLayout(container)

        self.nav = TopBar()
        self.stack = QStackedWidget()
        layout.addWidget(self.nav)
        layout.addWidget(self.stack)

        self.pomo_page = PomodoroPage()
        self.timer_page = TimerPage()
        self.watch_page = StopWatchPage()

        self.stack.addWidget(self.pomo_page)
        self.stack.addWidget(self.timer_page)
        self.stack.addWidget(self.watch_page)
        layout.addWidget(self.stack)
        
        self.stack.setCurrentIndex(0)
        self.nav.page_i.connect(self.stack.setCurrentIndex)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.setWindowTitle("Clopy")
    window.resize(640, 360)
    window.show()

    app.exec()

