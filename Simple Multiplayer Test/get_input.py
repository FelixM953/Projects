import tkinter as tk
from tkinter import simpledialog

class Get:
    def __init__(self):
        self.ROOT = tk.Tk()

        self.ROOT.withdraw()
        # the input dialog
        self.USER_INP = simpledialog.askstring(title="Test",
                                          prompt="What's your Localhost IP?:")
    
    def Ret(self):
        return self.USER_INP

if __name__ == "__main__":
    run = Get()
    print(run.Ret())