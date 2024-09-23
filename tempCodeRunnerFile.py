import tkinter as tk
from tkinter import Canvas, messagebox
from tkinter import *

class Main:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("投射シミュレーション設定")
        self.window.config(bg="#87cefa")
        self.window.geometry("800x600+0+0")
        self.window.protocol("WM_DELETE_WINDOW", self.close_windows)
        self.setup_ui()

        self.simulator = tk.Toplevel(self.window)
        self.window.title("投射シミュレーション")
        self.simulator.geometry("640x480+800+0")
        self.simulator.protocol("WM_DELETE_WINDOW", self.close_windows)

        self.cv = Canvas(self.simulator)
        self.cv.pack()
        
    def setup_ui(self):
        TITLE_FONT = ("Helvetica", 28, "bold")
        LABEL_FONT = ("Helvetica", 14)
        BUTTON_FONT = ("Helvetica", 14, "bold")
        MAIN_COLOR = "#4169e1"
        SECONDARY_COLOR = "#7fffd4"
        ACCENT_COLOR = "#ff7f50"

        self.title_label = tk.Label(text="投射シミュレーション", fg=MAIN_COLOR, bg="#87cefa", font=TITLE_FONT)
        self.title_label.pack()

        # Form frame to hold the input fields
        self.form_frame = tk.Frame(self.window, bg="#87cefa")
        self.form_frame.pack(pady=10, padx=30)

        # Initial velocity (v_0)
        self.v0_label = tk.Label(self.form_frame, text="初速度 (v_0):", font=LABEL_FONT, bg="#87cefa")
        self.v0_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.v0_entry = tk.Entry(self.form_frame,font=LABEL_FONT)
        self.v0_entry.grid(row=0, column=1, padx=10, pady=5)

        # Projection angle (θ)
        self.angle_label = tk.Label(self.form_frame, text="投射角度 (0=<θ<360):", font=LABEL_FONT, bg="#87cefa")
        self.angle_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.angle_entry = tk.Entry(self.form_frame, font=LABEL_FONT)
        self.angle_entry.grid(row=1, column=1, padx=10, pady=5)

        # Restitution coefficient (e)
        self.e_label = tk.Label(self.form_frame, text="反発係数 (0=<e<1):", font=LABEL_FONT, bg="#87cefa")
        self.e_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.e_entry = tk.Entry(self.form_frame,font=LABEL_FONT)
        self.e_entry.grid(row=2, column=1, padx=10, pady=5)

        # Initial x-coordinate (x_0)
        self.x0_label = tk.Label(self.form_frame, text="初期 x 座標 (x_0):", font=LABEL_FONT, bg="#87cefa")
        self.x0_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.x0_entry = tk.Entry(self.form_frame,font=LABEL_FONT)
        self.x0_entry.grid(row=3, column=1, padx=10, pady=5)

        # Initial y-coordinate (y_0)
        self.y0_label = tk.Label(self.form_frame, text="初期 y 座標 (y_0):", font=LABEL_FONT, bg="#87cefa")
        self.y0_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.y0_entry = tk.Entry(self.form_frame,font=LABEL_FONT)
        self.y0_entry.grid(row=4, column=1, padx=10, pady=5)

        # Width of the simulator window
        self.width_label = tk.Label(self.form_frame, text="シミュレータ幅:", font=LABEL_FONT, bg="#87cefa")
        self.width_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.width_entry = tk.Entry(self.form_frame,font=LABEL_FONT)
        self.width_entry.grid(row=5, column=1, padx=10, pady=5)

        # Height of the simulator window
        self.height_label = tk.Label(self.form_frame, text="シミュレータ高さ:", font=LABEL_FONT, bg="#87cefa")
        self.height_label.grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.height_entry = tk.Entry(self.form_frame,font=LABEL_FONT)
        self.height_entry.grid(row=6, column=1, padx=10, pady=5)

        self.button_frame = tk.Frame(self.window, bg="#87cefa")
        self.button_frame.pack()

        self.apply_button = tk.Button(self.button_frame, text="決定",padx=50, pady=10, font=BUTTON_FONT, bg=SECONDARY_COLOR, width=10)
        self.apply_button.pack(side=tk.TOP, padx=5,pady=30)

        # Buttons
        self.start_button = tk.Button(self.button_frame, text="シミュレーション開始", padx=50, pady=10, font=BUTTON_FONT, bg=SECONDARY_COLOR, width=10)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = tk.Button(self.button_frame, text="戻す", padx=50, pady=10, font=BUTTON_FONT, bg=ACCENT_COLOR, width=10)
        self.stop_button.pack(side=tk.LEFT, padx=5)


    def close_windows(self):
        self.window.destroy()
        self.simulator.destroy()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    simulator = Main()
    simulator.run()