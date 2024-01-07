import os
from gui import CartoonifyingApp
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1080x600+200+200")
    root.configure(bg="#2d2d2d")
    app = CartoonifyingApp(root)
    root.mainloop()
