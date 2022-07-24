from distutils.log import error
import tkinter as tk
from tkinter import ttk
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from latex import *
import os
import pickle

#constantes couleurs:
bg = '#121212'
bgMath = '#3A3A3A'
bg_buton = '#2e2e2e'
blue = '#b3d0ff'
red = '#ffa1c3'
green = '#c9ffc9'
whith = '#f0f0f0'

data_path = os.path.expanduser('~')+"\AppData\Local\mathclav"

if not(os.path.exists(data_path)):
    os.makedirs(data_path)
    os.makedirs(data_path+"\historique")
    os.makedirs(data_path+"\log")

matplotlib.use('TkAgg')

class historique(tk.Frame):
    def __init__(self, result, parent):
        self.parent = parent
        self.nb_historique = 0
        self.button_supr = []
        self.label_historique_name = []
        try :
            with open(data_path+r'\historique\nb.pkl', 'rb') as f1:
                self.nb_historique = pickle.load(f1)
        except FileNotFoundError:
            with open(data_path+r'\historique\nb.pkl', 'wb') as f1:
                pickle.dump(self.nb_historique, f1)
        print(self.nb_historique)
        self.result = result
        self.result_= []
        self.label_historique = []
        master = tk.Tk()
        master.title("MathClav - Historique")
        master.iconbitmap('favicon.ico')
        tk.Frame.__init__(self, master)

        tmptext = self.result.str()
        tmptext = tmptext.replace(r"\newline", "$ \n $")
        tmptext = tmptext.replace(r"æ", "a")
        if tmptext == "":
            tmptext = "Vide"
        self.fig_=[]
        self.canvas_=[]
        self.wx_=[]

        self.fig = plt.Figure(figsize=(4, 0.5), dpi=100)
        self.wx = self.fig.add_subplot(111)
        self.wx.get_xaxis().set_visible(False)
        self.wx.get_yaxis().set_visible(False)
        self.wx.patch.set_visible(False)
        self.wx.axis('off')
        self.fig.patch.set_facecolor(bgMath)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget()
        self.wx.text(-0.1, 0.6, r"$"+tmptext.replace(r"\text",r"\mathrm")+"$", fontsize =   8, color = whith)
        self.canvas.get_tk_widget().grid(row=0, column=0)
        self.canvas.draw()


        self.nom_actuel = tk.Entry(self)
        self.nom_actuel.grid(row=0, column=1)

        self.button_save = tk.Button(self, text="Save", command=self.save, bg=bg_buton, fg=whith)
        self.button_save.grid(row=0, column=2)

        self.afficher()
        self.pack()
        self['bg'] = bg
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
            with open(data_path+r'\historique\hist_'+str(i)+'.pkl', 'rb') as f1:
                self.result_.append(pickle.load(f1))
            self.label_historique_name.append(tk.Label(self, text=self.result_[i-1].name, bg=bg, fg=whith))
            self.label_historique_name[len(self.label_historique_name)-1].grid(row=i, column=0)
            self.label_historique_name[len(self.label_historique_name)-1].bind("<Button-1>", lambda event, i=i: self.ajouter(i))

            tmptext = self.result_[len(self.result_)-1].str()
            tmptext = tmptext.replace(r"\newline", "$ \n $")
            tmptext = tmptext.replace(r"æ", "a")
            if tmptext == "":
                tmptext = "Vide"
            self.fig_.append(plt.Figure(figsize=(4, 0.5), dpi=100))
            self.wx = self.fig_[len(self.fig_)-1].add_subplot(111)
            self.fig_[len(self.fig_)-1].patch.set_facecolor(bgMath)
            self.wx.get_xaxis().set_visible(False)
            self.wx.get_yaxis().set_visible(False)
            self.wx.patch.set_visible(False)
            self.wx.axis('off')
            self.canvas_.append(FigureCanvasTkAgg( self.fig_[len(self.fig_)-1], master=self))
            self.canvas_[len(self.canvas_)-1].get_tk_widget()
            self.wx.text(-0.1, 0.6, r"$"+tmptext.replace(r"\text",r"\mathrm")+"$", fontsize =   8, color=whith)
            self.canvas_[len(self.canvas_)-1].get_tk_widget().grid(row=i, column=1)
            self.canvas_[len(self.canvas_)-1].draw()

            self.button_supr.append(tk.Button(self, text="Suprimer", command=(lambda i=i:self.supr(i-1)), bg=bg_buton, fg=whith))
            self.button_supr[len(self.button_supr)-1].grid(row=i, column=2)

    def save(self):
        self.result.name = self.nom_actuel.get()
        with open(data_path+r'\historique\hist_'+str(self.nb_historique+1)+'.pkl', 'wb') as f1:
            pickle.dump(self.result, f1)
        self.nb_historique += 1
        with open(data_path+r'\historique\nb.pkl', 'wb') as f1:
            pickle.dump(self.nb_historique, f1)
        self.afficher()
    
    def supr(self, i):
        os.remove(data_path+r'\historique\hist_'+str(i+1)+'.pkl')
        self.result_.pop(i)
        self.nb_historique -= 1
        for k in range(i+2, self.nb_historique+2):
            os.rename(data_path+r'\historique\hist_'+str(k)+'.pkl', data_path+r'\historique\hist_'+str(k-1)+'.pkl')
        self.master.destroy()
        with open(data_path+r'\historique\nb.pkl', 'wb') as f1:
            pickle.dump(self.nb_historique, f1)
        h = historique(self.result, self.parent)
        
    def ajouter(self, i):
        self.parent.ajout(self.result_[i-1])
        self.master.destroy()

if __name__ == '__main__':
    import index
    index.main()
    