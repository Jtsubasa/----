import tkinter as tk
from tkinter import Canvas, messagebox
from tkinter import *

class Main:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("投射シミュレーション設定")
        self.window.config(bg="#87cefa")
        self.window.geometry("640x480+0+0")
        self.setup_ui()

        self.simulator = tk.Tk()
        self.cv = Canvas(self.simulator)
        self.cv.pack()
        self.simulator.geometry("640x480+660+0")
        self.ball_movement()

    def setup_ui(self):
        TITLE_FONT = ("Helvetica", 28, "bold")
        TIMER_FONT = ("Helvetica", 64, "bold")
        BUTTON_FONT = ("Helvetica", 14, "bold")
        MAIN_COLOR = "#4169e1"
        SECONDARY_COLOR = "#7fffd4"
        ACCENT_COLOR = "#ff7f50"
        
        self.title_label = tk.Label(text="投射シミュレーション", fg=MAIN_COLOR, bg="#87cefa", font=TITLE_FONT)
        self.title_label.pack()

        self.button_frame = tk.Frame(self.window, bg="#87cefa")
        self.button_frame.pack(pady=20)

        # ボタンたち
        self.start_button = tk.Button(self.button_frame, text="シミュレーション開始", padx=50, pady=10, font=BUTTON_FONT, bg=SECONDARY_COLOR, width=10)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = tk.Button(self.button_frame, text="戻す", padx=30, pady=10, font=BUTTON_FONT, bg=ACCENT_COLOR, width=10)
        self.stop_button.pack(side=tk.LEFT, padx=5)

    def ball_movement(self):
        Initial_Velocity = 0

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    simulator = Main()
    simulator.run()