from distutils.log import error
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
    def __init__(self, result):
        self.nb_historique = 0
        try :
            with open(r'historique\nb.pkl', 'rb') as f1:
                self.nb_historique = pickle.load(f1)
        except FileNotFoundError:
            with open(r'historique\nb.pkl', 'wb') as f1:
                pickle.dump(self.nb_historique, f1)
        print(self.nb_historique)
        self.result = result
        self.result_= []
        self.label_historique = []
        master = tk.Tk()
        master.title("MathClav_Historique")
        tk.Frame.__init__(self, master)

        self.label_actuel = tk.Label(self, text=result.str())
        self.label_actuel.grid(row=0, column=0)

        self.button_save = tk.Button(self, text="Save", command=self.save)
        self.button_save.grid(row=0, column=1)

        for i in range(1,self.nb_historique+1):
            with open(r'historique\hist_'+str(i)+'.pkl', 'rb') as f1:
                self.result_.append(pickle.load(f1))
            self.label_historique.append(tk.Label(self, text=self.result_[len(self.result_)-1].str()))
            self.label_historique[len(self.label_historique)-1].grid(row=i, column=0)

        self.pack()
        self.mainloop()
    
    def save(self):
        with open(r'historique\hist_'+str(self.nb_historique+1)+'.pkl', 'wb') as f1:
            pickle.dump(self.result, f1)
        self.nb_historique += 1
        with open(r'historique\nb.pkl', 'wb') as f1:
            pickle.dump(self.nb_historique, f1)

if __name__ == '__main__':
    h = historique(mathObject())
    