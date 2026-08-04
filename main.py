from PySide6.QtWidgets import * 
from PySide6.QtCore import Qt 

# fgc = #D4BE98
# bgc = #32302F
# bdgc = #252424

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        container = QWidget()
        self.setCentralWidget(container)

        layout = QVBoxLayout(container)

        page_container = QWidget()
        page_layout = QHBoxLayout(page_container)

        pomo_btn = QPushButton("Pomodoro")
        timer_btn = QPushButton("Timer")
        watch_btn = QPushButton("Stopwatch")
        
        page_layout.addWidget(pomo_btn)
        page_layout.addWidget(timer_btn)
        page_layout.addWidget(watch_btn)

        lbl = QLabel("T I M E")
        lbl.setAlignment(Qt.AlignCenter)

        btn = QPushButton("START")
        
        layout.addWidget(page_container)
        layout.addWidget(lbl)
        layout.addWidget(btn)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.setWindowTitle("Hello World")
    window.resize(640, 360)
    window.show()

    app.exec()

