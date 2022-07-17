import tkinter as tk
from tkinter import ttk
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from latex import *
import logging
import sys
import pickle

class historique(tk.Frame):
    def __init__(self, str):
        master = tk.Tk()
        master.title("MathClav_Historique")
        tk.Frame.__init__(self, master)
        self.label = tk.Label(self, text=str)
        self.label.pack()
        self.pack()
        self.mainloop()

if __name__ == '__main__':
    h = historique()
    