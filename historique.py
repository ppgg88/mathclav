from distutils.log import error
import tkinter as tk
from tkinter import ttk
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from latex import *
import logging
import sys
import os
import pickle

class historique(tk.Frame):
    def __init__(self, result, parent):
        self.parent = parent
        self.nb_historique = 0
        self.button_supr = []
        self.label_historique_name = []
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

        self.nom_actuel = tk.Entry(self)
        self.nom_actuel.grid(row=0, column=1)

        self.button_save = tk.Button(self, text="Save", command=self.save)
        self.button_save.grid(row=0, column=2)

        self.afficher()
        self.pack()
        self.mainloop()
    
    def afficher(self):
        for i in self.button_supr:
            i.destroy()
        for i in self.label_historique:
            i.destroy()
        self.result_ = []
        self.label_historique = []
        self.button_supr = []
        for i in range(1,self.nb_historique+1):
            with open(r'historique\hist_'+str(i)+'.pkl', 'rb') as f1:
                self.result_.append(pickle.load(f1))
            self.label_historique_name.append(tk.Label(self, text=self.result_[i-1].name))
            self.label_historique_name[len(self.label_historique_name)-1].grid(row=i, column=0)
            self.label_historique.append(tk.Label(self, text=self.result_[i-1].str()))
            self.label_historique[len(self.label_historique)-1].grid(row=i, column=1)
            self.label_historique[len(self.label_historique)-1].bind("<Button-1>", lambda event, i=i: self.parent.ajout(self.result_[i-1]))
            self.button_supr.append(tk.Button(self, text="Suprimer", command=(lambda i=i:self.supr(i-1))))
            self.button_supr[len(self.button_supr)-1].grid(row=i, column=2)

    def save(self):
        self.result.name = self.nom_actuel.get()
        with open(r'historique\hist_'+str(self.nb_historique+1)+'.pkl', 'wb') as f1:
            pickle.dump(self.result, f1)
        self.nb_historique += 1
        with open(r'historique\nb.pkl', 'wb') as f1:
            pickle.dump(self.nb_historique, f1)
        self.afficher()
    
    def supr(self, i):
        os.remove(r'historique\hist_'+str(self.nb_historique)+'.pkl')
        self.result_.pop(i)
        self.label_historique[i].destroy()
        self.button_supr[i].destroy()
        self.label_historique_name[i].destroy()
        self.button_supr.pop(i)
        self.label_historique.pop(i)
        self.label_historique_name.pop(i)
        self.nb_historique -= 1
        with open(r'historique\nb.pkl', 'wb') as f1:
            pickle.dump(self.nb_historique, f1)
        for i in range(1, len(self.result_)):
            with open(r'historique\hist_'+str(i)+'.pkl', 'wb') as f1:
                pickle.dump(self.result_[i], f1)
        self.afficher()

if __name__ == '__main__':
    h = historique(mathObject())
    