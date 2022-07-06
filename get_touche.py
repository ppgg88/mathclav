from logging import root
import tkinter as tk

def action(x):
    print(x)

root = tk.Tk()
root.bind("<KeyPress>", action)
root.mainloop()