#

import tkinter as tk
from tkinter import ttk
import sv_ttk

import json
import pyglet
import os

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math as mt

from latex import mathObject

from io import BytesIO
import win32clipboard
from PIL import Image

#import latex as lt

pyglet.font.add_file("Lato-Regular.ttf")
data_path = os.path.expanduser('~')+"\AppData\Local\mathclav"

class graphScreen(tk.Frame):
    def __init__(self, mathObj):
        self.mathObj = mathObj
        master = tk.Toplevel()
        master.title("MathClav - Graph")
        master.iconbitmap('favicon.ico')

        master.tk.call(sv_ttk.set_theme("dark"))

        settings = json.load(open(data_path+'\settings\settings.json'))
        if settings['settings']['theme'] == "light" :
            master.tk.call(sv_ttk.toggle_theme())
        tk.Frame.__init__(self, master)

        tk.Label(self, text="Titre du Graphique :", font=('Calibri 10')).grid(row=0, column=0, padx = 10)
        self.titre=ttk.Entry(self, width=35)
        self.titre.insert(0, ("f(x) = $" + self.mathObj.str()+"$"))
        self.titre.grid(row=0, column=1, padx = 10, pady=(0, 10))
        
        tk.Label(self, text="x minimum :", font=('Calibri 10')).grid(row=1, column=0, padx = 10)
        self.xmin=ttk.Entry(self, width=35)
        self.xmin.insert(0, "0")
        self.xmin.grid(row=2, column=0, padx = 10, pady=(0, 10))

        tk.Label(self, text="x maximum :", font=('Calibri 10')).grid(row=1, column=1, padx = 10)
        self.xmax=ttk.Entry(self, width=35)
        self.xmax.insert(0, "10")
        self.xmax.grid(row=2, column=1, padx = 10, pady=(0, 10))
        
        tk.Label(self, text="y minimum :", font=('Calibri 10')).grid(row=3, column=0, padx = 10)
        self.ymin=ttk.Entry(self, width=35)
        self.ymin.insert(0, "0")
        self.ymin.grid(row=4, column=0, padx = 10, pady=(0, 10))
        
        tk.Label(self, text="y maximum :", font=('Calibri 10')).grid(row=3, column=1, padx = 10)
        self.ymax=ttk.Entry(self, width=35)
        self.ymax.insert(0, "10")
        self.ymax.grid(row=4, column=1, padx = 10, pady=(0, 10))
        
        tk.Label(self, text="Label sur l'axe x :", font=('Calibri 10')).grid(row=5, column=0, padx = 10)
        self.xlabel=ttk.Entry(self, width=35)
        self.xlabel.grid(row=6, column=0, padx = 10, pady=(0, 10))
        
        tk.Label(self, text="Label sur l'axe y:", font=('Calibri 10')).grid(row=5, column=1, padx = 10)
        self.ylabel=ttk.Entry(self, width=35)
        self.ylabel.grid(row=6, column=1, padx = 10, pady=(0, 10))
        
        tk.Label(self, text="Asymptote horizontal :", font=('Calibri 10')).grid(row=7, column=0, padx = 10)
        self.xasym=ttk.Entry(self, width=35)
        self.xasym.grid(row=8, column=0, padx = 10, pady=(0, 10))
        
        tk.Label(self, text="Asymptote Vertical :", font=('Calibri 10')).grid(row=7, column=1, padx = 10)
        self.yasym=ttk.Entry(self, width=35)
        self.yasym.grid(row=8, column=1, padx = 10, pady=(0, 10))
        
        tk.Label(self, text="Pas de la trace :", font=('Calibri 10')).grid(row=9, column=0, padx = 10)
        self.pas=ttk.Entry(self, width=35)
        self.pas.insert(0, "0.01")
        self.pas.grid(row=10, column=0, padx = 10, pady=(0, 10))
        
        self.grilleActive = tk.IntVar()
        self.grille = ttk.Checkbutton(self, text="Grille", variable=self.grilleActive)
        self.grille.grid(row=10, column=1, padx = 10, pady=(0, 10))
        
        tk.Label(self, text="Variable de tracer :", font=('Calibri 10')).grid(row=11, column=0, padx = 10)
        self.var=ttk.Entry(self, width=35)
        self.var.insert(0, "x")
        self.var.grid(row=12, column=0, padx = 10, pady=(0, 10))
        
        self.graphButton = ttk.Button(self, text='Graph', width="15", command=self.graph)
        self.graphButton.grid(row=12, column=1, padx=10)
        
        self.pack()

        self.mainloop()
    
    def graph(self):
        if not(graph(self.mathObj, float(self.xmin.get()), float(self.xmax.get()), float(self.ymin.get()), float(self.ymax.get()), float(self.pas.get()), self.grilleActive.get(), self.titre.get(), self.xlabel.get(), self.ylabel.get(), self.var.get(), self.xasym.get(), self.yasym.get())):
            tk.messagebox.showinfo("Graph", "La Formule n'est pas une fonction")


def graph(Mathobj, xmin, xmax, ymin, ymax, xstep,  grille, titre, xlabel, ylabel, variable,  yasym, xaxym):
    func = Mathobj.graphStr().replace(variable, 'æ')
    erreur = False
    x = []
    y = []
    ax = []
    ay = []
    sng=1
    a = 0
    virgule = 0
    for i in range(0, len(xaxym)):
        if  i==0 :
            ax.append(0)
        if xaxym[i] == ';':
            ax[a] = sng*ax[a]
            sng=1
            ax.append(0)
            a +=1
            virgule = 0
        elif xaxym[i] == ' ':
            pass
        elif xaxym[i] == '-':
            sng = -1
        elif xaxym[i] == ',' or xaxym[i] == '.':
            virgule+=1
        else :
            try :
                if virgule>0 :
                    ax[a] = 1/(10**virgule)*int(xaxym[i])+ax[a]
                    virgule+=1
                else:
                    ax[a] = int(xaxym[i])+10*ax[a]
            except :
                ax[a]=sng*ax[a]
                ax.append(0)
                virgule = 0
                a +=1
                sng=1
    if ax != []:
        ax[len(ax)-1] = sng*ax[len(ax)-1]
    
    a=0
    virgule = 0
    sng=1
    for i in range(0, len(yasym)):
        if  i==0 :
            ay.append(0)
        if yasym[i] == ';':
            ay[a] = sng*ay[a]
            ay.append(0)
            virgule = 0
            sng = 1
            a +=1
        elif yasym[i] == '-':
            sng = -1
        elif yasym[i] == ' ':
            pass
        elif yasym[i] == ',' or yasym[i] == '.':
            virgule+=1
        else :
            try :
                if virgule>0 :
                    ay[a] = 1/(10**virgule)*int(yasym[i])+ay[a]
                    virgule+=1
                else:
                    ay[a] = int(yasym[i])+10*ay[a]
            except :
                ay[a] = sng*ay[a]
                ay.append(0)
                a +=1
                sng = 1
    
    if ay != []:
        ay[len(ay)-1] = sng*ay[len(ay)-1]
    a = int((xmax-xmin)/xstep)
    for i in range(0,a):
        x.append(i*xstep+xmin)
        æ = i*xstep+xmin
        for t in range(0, len(func)-1):
            if func[t].isdigit() and (func[t+1].isalpha() or func[t+1] == 'æ' or func[t+1] == '\\' or func[t+1] == '('):
                func = func[:t+1]+ "*" + func[t+1:]
            elif func[t]=='æ' and (func[t+1].isalpha() or func[t+1]=='\\' or func[t+1]=='('):
                func = func[:t+1]+ "*" + func[t+1:]
            elif func[t]==')' and (func[t+1]=='æ' or func[t+1]=='\\' or func[t+1].isalpha() or func[t+1]=='('):
                func = func[:t+1]+ "*" + func[t+1:]
        try:
            y.append(eval(func))
            erreur = False
        except:
            if erreur:
                print("Ereur dans la fonction : ", func)
                return(False)
            else:
                erreur = True
                x.pop(len(x)-1)
    plt.plot(x, y, color='blue', linewidth=1.5)
    
    for t in ax:
        plt.plot([t, t], [ymin, ymax], color='red', linewidth=0.5) 
    for t in ay:
        plt.plot([xmin, xmax], [t, t], color='red', linewidth=0.5) 
        
    plt.axis([xmin, xmax, ymin, ymax])
    if grille == 1:
        plt.grid()
        print(grille)
    plt.title(titre)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    xaxisticks = []
    for i in range(0, 6):
        xaxisticks.append(xmin +i*(xmax-xmin)/5)
        for t in ax:
            if t>(xmin +i*(xmax-xmin)/5) and t<(xmin +(i+1)*(xmax-xmin)/5):
                xaxisticks.append(t)
    plt.gca().axes.xaxis.set_ticks(xaxisticks)
    
    yaxisticks = []
    for i in range(0, 6):
        yaxisticks.append(ymin +i*(ymax-ymin)/5)
        for t in ay:
            if t>(ymin +i*(ymax-ymin)/5) and t<(ymin +(i+1)*(ymax-ymin)/5):
                yaxisticks.append(t)
    plt.gca().axes.yaxis.set_ticks(yaxisticks)
    
    filepath = data_path+'\Plot.png'
    plt.savefig(filepath, dpi=300, bbox_inches='tight')
    image = Image.open(filepath)

    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()

    send_to_clipboard(win32clipboard.CF_DIB, data)
    plt.show()
    return(True)

def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()
