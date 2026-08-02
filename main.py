from tkinter import *

class Pomodoro:
    def __init__(self, window):
        self.window = window
        self.window.title("Pomodoro Timer")
        self.window.geometry("300x180")
        self.window.resizable(False, False)

        self.hour = StringVar(value="00")
        self.minute = StringVar(value="50")
        self.second = StringVar(value="00")
        self.break_time = StringVar(value="10")

        self.remaining = 0
        self.is_break = False

        Label(window, text="Work Time").place(x=20, y=5)

        Entry(window, width=3, font=("Roboto", 18),
              textvariable=self.hour).place(x=20, y=30)
        Entry(window, width=3, font=("Roboto", 18),
              textvariable=self.minute).place(x=75, y=30)
        Entry(window, width=3, font=("Roboto", 18),
              textvariable=self.second).place(x=130, y=30)

        Label(window, text="Break (minutes)").place(x=20, y=70)
        Entry(window, width=5, font=("Roboto", 18),
              textvariable=self.break_time).place(x=20, y=95)

        self.status = Label(window, text="Ready", font=("Roboto", 12))
        self.status.place(x=150, y=95)

        Button(window, text="START", command=self.start).place(x=20, y=140)

    def start(self):
        """Starts the work timer."""
        try:
            self.remaining = (int(self.hour.get()) * 3600 + int(self.minute.get()) * 60 +
                int(self.second.get()))
            self.is_break = False
            self.status.config(text="Work")
            self.countdown()

        except ValueError:
            self.status.config(text="Invalid input")

    def countdown(self):
        """Updates the timer every second."""
        if self.remaining >= 0:
            mins, secs = divmod(self.remaining, 60)
            hrs, mins = divmod(mins, 60)

            self.hour.set(f"{hrs:02}")
            self.minute.set(f"{mins:02}")
            self.second.set(f"{secs:02}")

            self.remaining -= 1
            self.window.after(1000, self.countdown)

        else:
            if not self.is_break:
                self.start_break()
            else:
                self.start()

    def start_break(self):
        """Starts the break timer."""
        self.is_break = True
        self.status.config(text="Break")

        self.remaining = int(self.break_time.get()) * 60
        self.countdown()


def main():
    window = Tk()
    Pomodoro(window)
    window.mainloop()

if __name__ == "__main__":
    main()

