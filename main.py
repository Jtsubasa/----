import pygame as pg
import tkinter as tk
from tkinter import *

class main:
    def __init__(self):
        self.window = tk.Tk()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    simulator = main()
    simulator.run()