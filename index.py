# MathClav v0.2  
# by : Team SchnakyX & apparentés (TS&a)
#
# Licence (CC BY-NC-SA 4.0) 2022 - MathClav
# This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0
# International License. To view a copy of this license, visit 
# http://creativecommons.org/licenses/by-nc-sa/4.0/ 
# or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
#
# This program is distributed in the hope that it will be useful,
# for any question, please contact us at paul.giroux87@gmail.com

import tkinter as tk
from tkinter import ttk
#import pyi_splash
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from numpy import insert
from latex import *
import logging
import sys
import pyperclip
import pickle
from historique import *
from credit import *
import os
import time
import pyglet
import sv_ttk
import json
from help import *
from multitouche import *
from graph import *
import copy

#constantes couleurs :

whith = '#f0f0f0'
bg = '#1e1e1e'
bgMath = '#3A3A3A'
bg_buton = '#2e2e2e'
bg_white = '#FFFFFF'
blue = '#4188fd'
red = '#ea4646'
green = '#5cc25c'

#imports a new font
pyglet.font.add_file("Lato-Regular.ttf")

millis = lambda: int(round(time.time() * 1000))

data_path = os.path.expanduser('~')+"\AppData\Local\mathclav"

if not(os.path.exists(data_path)):
    os.makedirs(data_path)
    os.makedirs(data_path+"\settings")
    os.makedirs(data_path+"\historique")
    os.makedirs(data_path+"\log")

# for user they alredy have download verssion 0.1 of MathClav
if not(os.path.exists(data_path+"\settings")):
    os.makedirs(data_path+"\settings")

matplotlib.use('TkAgg')
#matplotlib.rcParams['font.size'] = 20
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.preamble'] = r'\usepackage{{amsmath}}'


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(data_path+"\log\mathclav.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

class mainWindow(tk.Frame):

    def __init__(self, master=None):
        '''initialisation de toute les variable et de la fenetre principale'''
        self.master = master
        self.master.bind("<KeyPress>", self.action)
        tk.Frame.__init__(self, master)
        self.pack()
        self.rg = 0
        self.rg_prev = []
        self.rg_prev_ = 0
        self.cursor = [0]
        self.result_prev = []
        self.engine_use = 0
        self.i = [0]
        self.i_prev = []
        self.n = 0
        self.ctrl_l = 0
        self.mode = 0
        self.mode_prev = 0
        try :
            settings = json.load(open(data_path+'\settings\settings.json'))
            self.size = settings['settings']['font_size']
            print(settings['settings']['font_size'])
        except :
            with open (data_path+'\settings\settings.json',"w") as f :
                f.write('{"settings": {"theme" : "%s","font_size" : 11}}'%sv_ttk.get_theme())
                self.size = 11
        self.dpi = 100
        self.pos = (0.8*11/(self.size*0.9))
        
        try :
            self.result = [pickle.load(open(data_path+r"\historique\last.pkl", "rb"))]
        except:
            self.result = [mathObject()]
        self.cursor=[len(self.result[0].content)]
        self.cursor_prev_ =[]
        self.cursor_prev = 0
        self.precedent = [mathSymbol('')]
        self.elements = []
        self.grec = False
        self.prev_time = 0
        self.math = False
        
        self.view_corespondance = [
            [   mathSymbol('A'), 
                mathSymbol('B'), 
                mathSymbol('\\Theta '), 
                mathSymbol('\\Delta '),  
                mathSymbol('E'),
                mathSymbol('\\Phi '),  
                mathSymbol('\\Gamma '),
                mathSymbol('H'), 
                mathSymbol('I'), 
                mathSymbol('\\Omega '),
                mathSymbol('K'), 
                mathSymbol('\\Lambda '), 
                mathSymbol('M'), 
                mathSymbol('N'), 
                mathSymbol('O'), 
                mathSymbol('\\Pi '), 
                mathSymbol('Q'),
                mathSymbol('P'),
                mathSymbol('\\Sigma '), 
                mathSymbol('T'),
                mathSymbol('U'),
                mathSymbol('X'),
                mathSymbol('\\Psi '), 
                mathSymbol('\\Xi '),
                mathSymbol('Y'), 
                mathSymbol('Z'), 
                mathSymbol(''),
                mathSymbol(''), #+
                mathSymbol(''), #-
                mathSymbol(''), #*
                mathSymbol(''), #=
                mathSymbol(''), #<>
                mathSymbol(''), #&
                mathSymbol(''), #!
                mathSymbol(''), #()
                mathSymbol(''), #|
            ],
            [   mathSymbol('\\alpha '), #a
                mathSymbol('\\beta '), #b
                mathSymbol('\\theta '),#c
                mathSymbol('\\delta '), #d
                mathSymbol('\\epsilon '), #e
                mathSymbol('\\varphi '), #f
                mathSymbol('\\gamma '), #g  
                mathSymbol('\\eta '), #h 
                mathSymbol('\\iota '), #i
                mathSymbol('\\omega '), #j 
                mathSymbol('\\kappa '), #k
                mathSymbol('\\lambda '), #l
                mathSymbol('\\mu '), #m
                mathSymbol('\\nu '), #n  
                mathSymbol('o '), #o 
                mathSymbol('\\pi '), #p
                mathSymbol('q'), #q
                mathSymbol('\\rho '), #r 
                mathSymbol('\\sigma '),#s
                mathSymbol('\\tau '), #t 
                mathSymbol('u'), #u
                mathSymbol('\\chi '), #v
                mathSymbol('\\psi '), #w
                mathSymbol('\\xi '), #x
                mathSymbol('\\upsilon '), #y
                mathSymbol('\\zeta '),#z
                mathSymbol(''), #^
                mathSymbol(''), #+
                mathSymbol(''), #-
                mathSymbol(''), #*
                mathSymbol(''), #=
                mathSymbol(''), #<>
                mathSymbol(''), #&
                mathSymbol(''), #!
                mathSymbol(''), #()
                mathSymbol(''), #|
            ],
            [   [mathSymbol('\Rightarrow '), mathSymbol('\Leftarrow ')],
                [binom()],
                [mathSymbol('\in '),mathSymbol('\supset '),mathSymbol('\subset '),mathSymbol('\supseteq '),mathSymbol('\subseteq ')],
                [e(), exp(), ln(), log()],
                [mathSymbol('\Longleftrightarrow '),mathSymbol('\Leftrightarrow ')],
                [mathSymbol('f'),mathSymbol('g'),mathSymbol('h'),mathSymbol('u')],
                [mathSymbol('\\rightarrow '),mathSymbol('\leftarrow '),mathSymbol('\leftrightarrow ')],
                [mathSymbol('Historique')],
                [integral(), integral2(),integral2f(), integral_double(), integral_doublef(),  integral_triple(),  integral_triplef()],
                [mathSymbol('\imath '), mathSymbol('\jmath '), mathSymbol('\Re '),mathSymbol('\Im ')],
                [mathSymbol('\: ')],##
                [ln(), log(), e(), exp()],
                [lim1(), lim()],
                [mathSymbol('n'), mathSymbol('k'), mathSymbol('l')],
                [sum(), sum1(), mathSymbol('\sum ')],
                [prod(), prod1(), mathSymbol('\prod ')],
                [frac()],
                [mathSymbol('\mathbb{R} '),mathSymbol('\mathbb{C} '),mathSymbol('\\mathbb{N} '),mathSymbol('\mathbb{Z} '),mathSymbol('\mathbb{Q} ')],
                [sqrt(), sqrt_n()],
                [cos(), sin(), tan()],
                [mathSymbol('\cup '), mathSymbol('\cap '), union(), intersection()],
                [vect()],
                [mathSymbol('\\forall '), mathSymbol('\\exists ')],
                [mathSymbol('x'), mathSymbol('y'), mathSymbol('z')],
                [arccos(), arcsin(), arctan()],
                [mathSymbol('\infty '), mathSymbol('+\infty '), mathSymbol('-\infty '), mathSymbol('\pm\infty ')],
                [power(view = True), indice(view = True)],
                [mathSymbol("+ "), mathSymbol("\\pm "),mathSymbol("\\mp "),mathSymbol("\\oplus ")],
                [mathSymbol("- "), mathSymbol("\\mp "),mathSymbol("\\pm "),mathSymbol("\\ominus ")],
                [mathSymbol("\\times "), mathSymbol("\\cdot "), mathSymbol("\\wedge "),mathSymbol("\\ast "), mathSymbol("\\odot "), mathSymbol("\\otimes ")],
                [mathSymbol("="), mathSymbol("\\approx "),mathSymbol("\\neq ") ,mathSymbol("\\equiv "), mathSymbol("\\sim "),mathSymbol("\\simeq "), mathSymbol("\\propto ")],
                [mathSymbol("<"), mathSymbol(">"), mathSymbol("\leq "), mathSymbol("\geq "), mathSymbol("\ll "), mathSymbol("\gg ")],
                [ mathSymbol("\\wedge "),mathSymbol("\\vee "),mathSymbol("& ")],
                [mathSymbol("! "), mathSymbol("\\neg "),mathSymbol("a\\not ")],
                [parenthese(), parenthese_carre()],
                [norme(), norme2()]
            ],
            ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "^", "+", "-","*", "=", "</>", "&", "!", "( / )", "|"],
        ]

        
        self.corespondance = [
            [   mathSymbol('A'), 
                mathSymbol('B'), 
                mathSymbol('\\Theta '), 
                mathSymbol('\\Delta '),  
                mathSymbol('E'),
                mathSymbol('\\Phi '),  
                mathSymbol('\\Gamma '),
                mathSymbol('H'), 
                mathSymbol('I'), 
                mathSymbol('\\Omega '),
                mathSymbol('K'), 
                mathSymbol('\\Lambda '), 
                mathSymbol('M'), 
                mathSymbol('N'), 
                mathSymbol('O'), 
                mathSymbol('\\Pi '), 
                mathSymbol('Q'),
                mathSymbol('P'),
                mathSymbol('\\Sigma '), 
                mathSymbol('T'),
                mathSymbol('U'),
                mathSymbol('X'),
                mathSymbol('\\Psi '), 
                mathSymbol('\\Xi '),
                mathSymbol('Y'), 
                mathSymbol('Z'), 
                mathSymbol(''),
                mathSymbol(''), #+
                mathSymbol(''), #-
                mathSymbol(''), #*
                mathSymbol(''), #=
                mathSymbol(''), #<>
                mathSymbol(''), #&
                mathSymbol(''), #!
                mathSymbol(''), #()
                mathSymbol(''), #|
            ],
            [   mathSymbol('\\alpha '), #a
                mathSymbol('\\beta '), #b
                mathSymbol('\\theta '),#c
                mathSymbol('\\delta '), #d
                mathSymbol('\\epsilon '), #e
                mathSymbol('\\varphi '), #f
                mathSymbol('\\gamma '), #g  
                mathSymbol('\\eta '), #h 
                mathSymbol('\\iota '), #i
                mathSymbol('\\omega '), #j 
                mathSymbol('\\kappa '), #k
                mathSymbol('\\lambda '), #l
                mathSymbol('\\mu '), #m
                mathSymbol('\\nu '), #n  
                mathSymbol('o '), #o 
                mathSymbol('\\pi '), #p
                mathSymbol('q'), #q
                mathSymbol('\\rho '), #r 
                mathSymbol('\\sigma '),#s
                mathSymbol('\\tau '), #t 
                mathSymbol('u'), #u
                mathSymbol('\\chi '), #v
                mathSymbol('\\psi '), #w
                mathSymbol('\\xi '), #x
                mathSymbol('\\upsilon '), #y
                mathSymbol('\\zeta '),#z
                mathSymbol(''), #^ 26
                mathSymbol(''), #+ 27
                mathSymbol(''), #- 28
                mathSymbol(''), #* 29
                mathSymbol(''), #= 30
                mathSymbol(''), #<> 31
                mathSymbol(''), #& 32
                mathSymbol(''), #! 33
                mathSymbol(''), #()34
                mathSymbol(''), #| 35
            ],
            [   [mathSymbol('\Rightarrow '), mathSymbol('\Leftarrow ')],
                [binom()],
                [mathSymbol('\in '),mathSymbol('\supset '),mathSymbol('\subset '),mathSymbol('\supseteq '),mathSymbol('\subseteq ')],
                [e(), exp(), ln(), log()],
                [mathSymbol('\Longleftrightarrow '),mathSymbol('\Leftrightarrow ')],
                [mathSymbol('f'),mathSymbol('g'),mathSymbol('h'),mathSymbol('u')],
                [mathSymbol('\\rightarrow '),mathSymbol('\leftarrow '),mathSymbol('\leftrightarrow ')],
                [mathSymbol('Historique')],
                [integral(), integral2(),integral2f(), integral_double(), integral_doublef(),  integral_triple(),  integral_triplef()],
                [mathSymbol('\imath '), mathSymbol('\jmath '), mathSymbol('\Re '),mathSymbol('\Im ')],
                [mathSymbol('\: ')],##
                [ln(), log(), e(), exp()],
                [lim1(), lim()],
                [mathSymbol('n'), mathSymbol('k'), mathSymbol('l')],
                [sum(), sum1(), mathSymbol('\sum ')],
                [prod(), prod1(), mathSymbol('\prod ')],
                [frac()],
                [mathSymbol('\mathbb{R} '),mathSymbol('\mathbb{C} '),mathSymbol('\\mathbb{N} '),mathSymbol('\mathbb{Z} '),mathSymbol('\mathbb{Q} ')],
                [sqrt(), sqrt_n()],
                [cos(), sin(), tan()],
                [mathSymbol('\cup '), mathSymbol('\cap '), union(), intersection()],
                [vect()],
                [mathSymbol('\\forall '), mathSymbol('\\exists ')],
                [mathSymbol('x'), mathSymbol('y'), mathSymbol('z')],
                [arccos(), arcsin(), arctan()],
                [mathSymbol('\infty '), mathSymbol('+\infty '), mathSymbol('-\infty '), mathSymbol('\pm\infty ')],
                [power(view=False), indice(view=False)],
                [mathSymbol("+ "), mathSymbol("\\pm "),mathSymbol("\\mp "),mathSymbol("\\oplus ")],
                [mathSymbol("- "), mathSymbol("\\mp "),mathSymbol("\\pm "),mathSymbol("\\ominus ")],
                [mathSymbol("\\times "), mathSymbol("\\cdot "), mathSymbol("\\wedge "),mathSymbol("\\ast "), mathSymbol("\\odot "), mathSymbol("\\otimes ")],
                [mathSymbol("="), mathSymbol("\\approx "),mathSymbol("\\neq ") ,mathSymbol("\\equiv "), mathSymbol("\\sim "),mathSymbol("\\simeq "), mathSymbol("\\propto ")],
                [mathSymbol("<"), mathSymbol(">"), mathSymbol("\leq "), mathSymbol("\geq "), mathSymbol("\ll "), mathSymbol("\gg ")],
                [ mathSymbol("\\wedge "),mathSymbol("\\vee "),mathSymbol("& ")],
                [mathSymbol("! "), mathSymbol("\\neg "),mathSymbol("a\\not ")],
                [parenthese(), parenthese_carre()],
                [norme(), norme2()]
            ],
            ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "^", "+", "-","*", "=", "</>", "&", "!", "( / )", "|"],
        ]
        
        
        self.createWidgets()
        self.graph()
        #pyi_splash.close()

    def createWidgets(self):
        '''creation de tout les widget sur la page principale'''
        self.label = tk.Label(self)
        self.label.bind("<Button-1>",self.copy_to_clipboard)
        self.label['bg'] = bg
        self.label['fg'] = whith
        self.label.pack()
        
        self.indication = ttk.Label(self, text="Lettre Usuelle", font=("Lato Regular", 12),foreground=blue)
        self.indication.pack()

        label = tk.Frame(self)
        label.pack()

        # Define the figure size and plot the figure
        self.fig = plt.Figure(figsize=(200, 2), dpi=self.dpi)
        self.wx = self.fig.add_subplot(111)
        self.wx.get_xaxis().set_visible(False)
        self.wx.get_yaxis().set_visible(False)
        self.wx.patch.set_visible(False)
        self.wx.axis('off')
        if sv_ttk.get_theme() == 'dark':
            self.fig.patch.set_facecolor(bgMath)
        else:
            self.fig.patch.set_facecolor(bgMath_white)
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=label)
        self.canvas.get_tk_widget().pack(expand=1, fill=tk.BOTH, side=tk.TOP)
        self.latex_display()


        self.btn = tk.Frame(self)
        self.btn['bg'] = bg
        liste = []
        for i in range(1, 30):
            liste.append(i)

        s1 = ttk.Label(self.btn, text="Moteur LaTex :", font=("Lato Regular", 10))
        s1.grid(row=0, column=0)

        self.cobobox1 = ttk.Combobox(self.btn, values=["Intern Engine (MatPlot)", "Extern Engine"], state="readonly")
        self.cobobox1.bind("<<ComboboxSelected>>", self.engine)
        self.cobobox1.current(0)
        self.cobobox1.grid(row=1, column=0, padx=10)


        s = ttk.Label(self.btn, text="Taille :", font=("Lato Regular", 10))
        s.grid(row=0, column=1)

        
        self.cobobox = ttk.Combobox(self.btn, values=liste, state="readonly")
        self.cobobox.bind("<<ComboboxSelected>>", self.change_size)
        self.cobobox.current(self.size-1)
        self.cobobox.grid(row=1, column=1, padx=10)

        self.copyButton = ttk.Button(self.btn, text="Copier le LaTex", width="20", command=self.copy_to_clipboard, takefocus=False)
        self.copyButton.grid(row=0, column=2, padx=10,pady=8)

        self.themeButton = ttk.Button(self.btn, text="Thème clair", width="20", command=self.changeTheme, takefocus=False)
        self.themeButton.grid(row=0, column=3, padx=10,pady=8)

        self.clearButton = ttk.Button(self.btn, text='Effacer Tout',width="20", command=self.clear, takefocus=False)
        self.clearButton.grid(row=1, column=2, padx=10)

        self.quitButton = ttk.Button(self.btn, text='Aide ?', width="20", command=self.openHelp, takefocus=False)
        self.quitButton.grid(row=1, column=3, padx=10)
        self.btn.pack(padx=10, pady=20)
        
    def clear(self):
        '''efface le texte precedement ecris'''
        self.historique()
        self.result = [mathObject()]
        self.elements = []
        self.precedent = [mathSymbol('')]
        self.cursor = [0]
        self.rg = 0
        self.i = [0]
        self.pos = (0.8*11/(self.size*0.9))
        self.latex_display()
        self.wx.clear()
        self.graph()

    def engine(self, temp = None):
        '''change le moteur de rendue latex'''
        if self.cobobox1.get() == "Intern Engine":
            self.engine_use = 0
        else:
            self.engine_use = 1
        self.graph()

    def latex_display(self):
        '''affiche le texte au format latex'''
        # Get the Entry Input
        tmptext = self.result[0].str().replace('\\newline', chr(10))
        if sv_ttk.get_theme()=="dark" :
            self.label.configure(text=tmptext, font=("Lato Regular", 11),fg='white')
        else :
            self.label.configure(text=tmptext, font=("Lato Regular", 11),fg='black')

    def change_size(self, temp):
        '''change la taille du texte'''
        self.size = int(self.cobobox.get())
        self.pos = (0.8*11/(self.size*0.9))
        self.graph()
        logging.info("set text sizes : " + str(self.size))
        with open (data_path+'\settings\settings.json',"r+") as f :
            settings = json.load(f)

            settings['settings']['font_size']=self.size
            
            f.seek(0)
            f.write(json.dumps(settings))
            f.truncate()       

    def historique(self):
        self.result_prev.append(copy.deepcopy(self.result))
        self.i_prev.append(copy.deepcopy(self.i))
        self.cursor_prev_.append(copy.deepcopy(self.cursor))
        self.rg_prev.append(self.rg)

    def action(self, touche):
        '''action sur les touches'''
        logging.info("press :" +  str(touche))
        char = touche.char
        key = touche.keycode
        keyname = touche.keysym
        
        #GREC MAJ
        #GREC min
        #MATH
        corespondance = copy.deepcopy(self.corespondance)
        
        # Si on appuie sur une touche de controle : ctrl : grec
        if keyname == 'Control_L':
            self.mode_prev = self.mode
            if self.mode != 2:
                self.mode = 2
                self.indication.configure(text="Lettre Grecque", foreground=green)
            else :
                self.mode = 0
                self.indication.configure(text="Lettre Usuelle",foreground=blue)
            self.ctrl_l = millis()
            return 1
        elif keyname in ['Alt_R', 'c', 'C', 'z', 'Z'] and millis()-self.ctrl_l < 1000: # corection du bug pour les touche en mode CTRL + ... 
            self.mode = self.mode_prev
            if self.mode == 0 : 
                self.indication.configure(text="Lettre Usuelle",foreground=blue)
            elif self.mode == 1:
                self.indication.configure(text="Mode Math", foreground=red)
            elif self.mode == 2:
                self.indication.configure(text="Lettre Grecque", foreground=green)
            else : #juste en cas de bug ailleur mais aucune reel utilité
                self.mode = 0
                self.indication.configure(text="Lettre Usuelle",foreground=blue)
            
        if keyname == 'twosuperior':
            self.mode_prev = self.mode
            if self.mode != 1:
                self.mode = 1
                self.indication.configure(text="Mode Math", foreground=red)
            else :
                self.mode = 0
                self.indication.configure(text="Lettre Usuelle",foreground=blue)
            return 1
        
        #touche sans action dans le logiciel
        if keyname =='Control_L' or keyname =='Alt_L' or keyname =='Alt_R' or key in [16, 20, 38, 40, 17, 19, 145, 35, 36, 91, 179, 175,174,173] or (self.mode == 1 and touche.char=='^') or touche.char== "\\" or touche.char== "\t" or touche.char=="#" or touche.char=="`" :
            return 1
    
        if keyname == 'F10': # touche F10
            graphScreen(self.result[0])
            return 1
        
        if key == 39: #fleche droite ->
            if len(self.result[self.rg].content)>self.cursor[self.rg]:
                self.cursor[self.rg] += 1
            elif self.rg > 0 and self.i[self.rg] == self.result[self.rg-1].content[self.cursor[self.rg-1]-1].imax:
                self.cursor.pop(self.rg)
                self.result.pop(self.rg)
                self.i.pop(self.rg)
                self.rg -= 1
            elif self.rg > 0 :
                self.i[self.rg] += 1
                self.cursor[self.rg] = 0
                self.result.pop(self.rg)
                self.result.append(self.result[self.rg-1].content[self.cursor[self.rg-1]-1].content[self.i[self.rg]])
            self.graph()
            return(1)
        
        if key == 37: #fleche gauche <-
            if self.cursor[self.rg] > 0:
                if self.result[self.rg].content[self.cursor[self.rg]-1].imax >= 0:
                    self.i.append(self.result[self.rg].content[self.cursor[self.rg]-1].imax)
                    self.result.append(self.result[self.rg].content[self.cursor[self.rg]-1].content[self.i[self.rg]])
                    self.cursor.append(len(self.result[self.rg+1].content))
                    self.rg += 1
                else:
                    self.cursor[self.rg] -= 1
            elif self.rg > 0 and self.i[self.rg] == 0 :
                self.cursor.pop(self.rg)
                self.result.pop(self.rg)
                self.i.pop(self.rg)
                self.rg -= 1
                self.cursor[self.rg] -= 1 
            elif self.rg > 0:
                self.i[self.rg] -= 1
                self.cursor[self.rg] = 0
                self.result.pop(self.rg)
                self.result.append(self.result[self.rg-1].content[self.cursor[self.rg-1]-1].content[self.i[self.rg]])
            self.graph()
            return(1)
        
        if key == 8: #suppr <--
            self.historique()
            if self.cursor[self.rg] == 0 and self.rg > 0:
                self.result.pop(self.rg)
                self.i.pop(self.rg)
                self.cursor.pop(self.rg)
                self.rg -= 1
                self.result[self.rg].content.pop(self.cursor[self.rg]-1)
                self.cursor[self.rg] -= 1
            else:
                self.result[self.rg].content.pop(self.cursor[self.rg]-1)
                self.cursor[self.rg] -= 1
            self.graph()
            return(1)
        
        if key == 46: #suppr -->
            self.historique()
            try:
                self.result[self.rg].content.pop(self.cursor[self.rg])
            except:
                pass
            self.graph()
            return(1)
        
        if key == 27: #escape
            self.quiter()
            return(1)
        
        if touche.char == "\x03": #ctrl-c
            self.copy_to_clipboard()
            return(1)
        
        if touche.char == "\x1a": #ctrl+z
            self.result = copy.deepcopy(self.result_prev[len(self.result_prev)-1])
            self.i = copy.deepcopy(self.i_prev[len(self.i_prev)-1])
            self.cursor = copy.deepcopy(self.cursor_prev_[len(self.cursor_prev_)-1])
            self.rg = self.rg_prev[len(self.rg_prev)-1]
            
            self.result_prev.pop(len(self.result_prev)-1)
            self.i_prev.pop(len(self.i_prev)-1)
            self.cursor_prev_.pop(len(self.cursor_prev_)-1)
            self.rg_prev.pop(len(self.rg_prev)-1)
            
            self.graph()
            return(1)
            
        if key == 120: #F9
            c = credit()
            return(1)
        
        if touche.char == "=" and self.result[0].str() == "raptor":
            v = raptor()
            return(1)
        
        ## touche qui ne depend pas du mode selectioner
        if key==13:
            self.multiple_choice([mathSymbol('\\newline')])
            self.pos-=0.11
            return(1)
        elif touche.char=='=':
            self.multiple_choice([mathSymbol("="), mathSymbol("\\approx "),mathSymbol("\\neq ") ,mathSymbol("\\equiv "), mathSymbol("\\sim "),mathSymbol("\\simeq "), mathSymbol("\\propto ")])
            return(1)
        elif touche.char=='*':
            self.multiple_choice([mathSymbol("\\times "), mathSymbol("\\cdot "), mathSymbol("\\wedge "),mathSymbol("\\ast "), mathSymbol("\\odot "), mathSymbol("\\otimes ")])
            return(1)
        elif touche.char=='+':
            self.multiple_choice([mathSymbol("+ "), mathSymbol("\\pm "),mathSymbol("\\mp "),mathSymbol("\\oplus ")])
            return(1)
        elif touche.char=='-':
            self.multiple_choice([mathSymbol("- "), mathSymbol("\\mp "),mathSymbol("\\pm "),mathSymbol("\\ominus ")])
            return(1)
        elif touche.char=='!':
            self.multiple_choice([mathSymbol("! "), mathSymbol("\\neg "),mathSymbol("\\not ")])
            return(1)
        elif touche.char=='{':
            self.multiple_choice([ crochet()])
            return(1)
        elif touche.char=='}':
            self.multiple_choice([crochet()])
            return(1)
        elif touche.char=='&':
            self.multiple_choice([ mathSymbol("\\wedge "),mathSymbol("\\vee "),mathSymbol("& ")])
            return(1)
        elif keyname == 'less': #inf <
            self.multiple_choice([mathSymbol("<"), mathSymbol(">"), mathSymbol("\leq "), mathSymbol("\geq "), mathSymbol("\ll "), mathSymbol("\gg ")])
            return(1)
        elif keyname == 'greater': #sup >
            self.multiple_choice([ mathSymbol(">"),mathSymbol("<"), mathSymbol("\geq "),mathSymbol("\leq "), mathSymbol("\gg "),  mathSymbol("\ll ")])
            return(1)
        elif touche.char=='"':
            self.multiple_choice([texte()])
            return(1)
        elif key == 32: #space
            self.multiple_choice([mathSymbol("\: ")])
            return(1)
        elif touche.char == '$':
            self.multiple_choice([mathSymbol("\$")])
            return(1)
        
        if self.mode == 0: #mode standard
            try:
                self.multiple_choice([mathSymbol(touche.char)])
            except:
                pass
            return(1)
        
        if self.mode == 1: #mode math
            if char == 'h' or char == 'H':
                historique()
            elif key >= 65 and key <= 90 :
                self.multiple_choice(corespondance[2][key-65])
  
            elif key == 191: #fraction touche '/'
                #####/#/#/#/#/######
                temp = self.result[self.rg].content[self.cursor[self.rg]-1]
                self.result[self.rg].content.pop(self.cursor[self.rg]-1)
                self.cursor[self.rg] -= 1
                self.multiple_choice([frac()])
                self.multiple_choice([temp])
                self.i[self.rg] += 1
                self.cursor[self.rg] = 0
                self.result.pop(self.rg)
                self.result.append(self.result[self.rg-1].content[self.cursor[self.rg-1]-1].content[self.i[self.rg]])
                self.graph()
                
            elif key == 221: #puissance touche '^'
                self.multiple_choice([power(view=False), indice(view=False)])
            elif touche.char == '(':
                self.multiple_choice([parenthese(), parenthese_carre()])
            elif touche.char == ')':
                self.multiple_choice([parenthese(), parenthese_carre()])
            elif touche.char == '|':
                self.multiple_choice([norme(), norme2()])
            elif touche.char == '_':
                self.multiple_choice([indice(view=False)])
            elif touche.char != None: #sinon caractere normal
                self.multiple_choice([mathSymbol(touche.char.replace('^',''))])
            else :
                print('touche inconue en mode math')
            return(1)
        
        if self.mode == 2: #mode Grec
            if key >= 65 and key <= 90: 
                if char.isupper():
                    self.multiple_choice([corespondance[0][key-65]])
                else : 
                    self.multiple_choice([corespondance[1][key-65]])
            else :
                print("lettre inconue en Mode Grec")
            return(1)
    
    def multiple_choice(self, temp):
        self.historique()
        '''permet de gerer le cas ou la fonction change lorsque l'on apuis plusieur fois sur le meme bouton'''
        if len(temp) == 1:

            self.result[self.rg].add(temp[0], self.cursor[self.rg])
            self.precedent.append(temp[0])
            self.cursor[self.rg]+=1
            inser = temp[0]
        else:
            a = True
            for i in range(0, len(temp)):
                if temp[i].__str__() == self.precedent[len(self.precedent)-1].__str__() and self.prev_time > (millis()-1500):
                    inser = temp[i]
                    if self.rg != self.rg_prev_:
                        self.result.pop(self.rg)
                        self.i.pop(self.rg)
                        self.cursor.pop(self.rg)
                        self.rg=self.rg_prev_
                    self.cursor[self.rg] = self.cursor_prev
                    self.result[self.rg].content.pop(self.cursor[self.rg])
                    l = i+1
                    if l>=len(temp): l = 0
                    self.precedent[len(self.precedent)-1] = temp[l]
                    inser = temp[l]
                    a = False
                    break
            if a:
                self.rg_prev_ = self.rg
                self.precedent.append(temp[0])
                inser = temp[0]
                l=0
                try:
                    self.multi.master.destroy()
                except:
                    pass
                self.multi = multi(self, root, temp, l)
            else:
                self.multi.modifie(l, temp)
            self.result[self.rg].add(inser, self.cursor[self.rg])
            self.cursor_prev = self.cursor[self.rg]
            self.cursor[self.rg]+=1
            self.prev_time = millis()

        if inser.imax>=0:
            self.rg_prev_ = self.rg
            self.rg += 1
            self.i.append(0)
            self.cursor.append(0)
            self.result.append(inser.content[0])
        print(self.rg)
        print(self.result[self.rg].content)
        print(self.cursor[self.rg])
            
        self.graph()
       
    def graph(self):
        '''permet de gerer le graphique et l'affichage des Math'''
        self.latex_display()
        self.result[self.rg].add(mathSymbol(chr(166)), self.cursor[self.rg])
        if self.rg != 0:
            self.result[0].add(mathSymbol(r'\:\:░'), len(self.result[0].content))
            tmptext = self.result[0].str()
            self.result[0].content.pop(len(self.result[0].content)-1)
        else:
            tmptext = self.result[0].str()
        self.result[self.rg].content.pop(self.cursor[self.rg])
        # Get the Entry Input
        tmptext = tmptext.replace(r"\newline", "$ \n $")
        tmptext = tmptext.replace(r"æ", "a")
        # Clear any previous Syntax from the figure
        if self.engine_use == 0:
            try : 
                matplotlib.rcParams['text.usetex'] = False
                self.wx.clear()
                if sv_ttk.get_theme() == "dark" :
                    self.wx.text(-0.1, self.pos, r"$"+tmptext.replace(r"\text",r"\mathrm")+"$", fontsize = self.size, color = whith)
                else :
                    self.wx.text(-0.1, self.pos, r"$"+tmptext.replace(r"\text",r"\mathrm")+"$", fontsize = self.size, color = 'black')
                self.wx.patch.set_visible(False)
                self.wx.axis('off')
                self.canvas.draw()
            except:
                matplotlib.rcParams['text.usetex'] = True
                matplotlib.rcParams['text.latex.preamble'] = r'\usepackage{{amsmath}}'
                self.wx.clear()
                self.wx.text(-0.1, self.pos, r"$"+tmptext+"$", fontsize = self.size)
                self.wx.patch.set_visible(False)
                self.wx.axis('off')
                self.canvas.draw()
        else:
            matplotlib.rcParams['text.usetex'] = True
            matplotlib.rcParams['text.latex.preamble'] = r'\usepackage{{amsmath}}'
            self.wx.clear()
            self.wx.text(-0.1, self.pos, r"$"+tmptext+"$", fontsize = self.size)
            self.wx.patch.set_visible(False)
            self.wx.axis('off')
            self.canvas.draw()

    def copy_to_clipboard(self, temp = None):
        '''permet de copier le texte laTex dans le presse-papier'''
        tmptext = self.result[0].str().replace(r"\newline", chr(10))
        pyperclip.copy(tmptext)
        tk.messagebox.showinfo("Copie", "Le code Latex à été copié dans votre presse-papier")

    def quiter(self):
        '''permet de quitter le programme'''
        with open(data_path+r'\historique\last.pkl', 'wb') as f1:
            pickle.dump(self.result[0], f1)
        a=True
        self.quit()
        root.destroy()

    def ajout(self, input):
        '''permet d'ajouter un element dans la pile'''
        for data in input.content:
            self.result[self.rg].content.append(data)
            self.cursor += 1
        self.result[self.rg].add(mathSymbol(chr(166)), self.cursor)
        self.graph()
        self.result[self.rg].destroy(self.cursor+1)
        self.latex_display()
        
    def changeTheme(self) :
        '''change le thème de l'application'''
        sv_ttk.toggle_theme()
        with open (data_path+'\settings\settings.json',"r+") as f :
            settings = json.load(f)

            if sv_ttk.get_theme() == "dark" :
                self.btn['bg'] = bg
                self.label['bg'] = bg
                app['bg'] = bg
                self.latex_display()
                self.themeButton['text']="Thème clair"
                settings['settings']['theme']="dark"
                self.fig.patch.set_facecolor(bgMath)
                self.canvas.draw()
                
            else :
                self.btn['bg'] = bg_white
                self.label['bg'] = bg_white
                app['bg'] = bg_white
                self.latex_display()
                self.themeButton['text']="Thème sombre"
                settings['settings']['theme']="light"
                self.fig.patch.set_facecolor(bgMath_white)
                self.canvas.draw()
            
            f.seek(0)
            f.write(json.dumps(settings))
            f.truncate()
            self.graph()      
        
    def openHelp(self) :
        '''ouvre la fenêtre d'aide'''
        corespondance = self.view_corespondance
        try :
            settings = json.load(open(data_path+'\settings\settings.json'))
            if settings['settings']['help_mode'] == "keyboard" :
                self.help = help(corespondance)
                print(settings['settings']['help_mode'])
            else :
                self.help = help_2(corespondance)
        except :
            with open (data_path+'\settings\settings.json',"w") as f :
                f.write('{"settings": {"theme" : "%s","font_size" : %d,"help_mode" : "keyboard"}}'%(sv_ttk.get_theme(),self.size))
                f.truncate()  
                self.help = help(corespondance)
        #self.help_2 = help_2(corespondance)




if __name__ == '__main__':
    root = tk.Tk()
    root.title("MathClav")
    root.geometry("800x380")
    root.iconbitmap('favicon.ico')
    sv_ttk.set_theme("dark")
    app = mainWindow(root)
    app['bg'] = bg
    try :
        settings = json.load(open(data_path+'\settings\settings.json'))
        if settings['settings']['theme'] == "light" :
            app.changeTheme()
    except :
        with open (data_path+'\settings\settings.json',"w") as f :
            f.write('{"settings": {"theme" : "dark","font_size" : 11,"help_mode" : "keyboard"}}')
    app.mainloop()

