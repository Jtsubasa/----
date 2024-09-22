import pygame
import tkinter as tk
from tkinter import *

class main:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("玉シミュレーション設定")
        self.window.config(bg="#87cefa")
        self.window.geometry("600x400+0+0")
        self.setup_ui()

    def setup_ui(self):
        TITLE_FONT = ("Helvetica", 28, "bold")
        LABEL_FONT = ("Helvetica", 18)
        BUTTON_FONT = ("Helvetica", 14, "bold")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    simulator = main()
    simulator.run()