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
        self.rg_prev = 0
        self.cursor = 0
        self.cursor_prev = 0
        self.engine_use = 0
        self.i = [0]
        self.n = 0
        self.ctrl_l = False
        self.mode_prev = 0
        self.size = 11
        self.dpi = 100
        self.pos = 0.9
        try :
            self.result = [pickle.load(open(data_path+r"\historique\last.pkl", "rb"))]
        except:
            self.result = [mathObject()]
        self.cursor=len(self.result[0].content)
        self.precedent = [mathSymbol('')]
        self.elements = []
        self.grec = False
        self.prev_time = 0
        self.math = False
        self.createWidgets()
        self.result[self.rg].add(mathSymbol(chr(166)), self.cursor)
        self.graph()
        self.result[self.rg].destroy(self.cursor+1)
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
        fig = plt.Figure(figsize=(200, 2), dpi=self.dpi)
        self.wx = fig.add_subplot(111)
        self.wx.get_xaxis().set_visible(False)
        self.wx.get_yaxis().set_visible(False)
        self.wx.patch.set_visible(False)
        self.wx.axis('off')
        fig.patch.set_facecolor(bgMath)
        
        self.canvas = FigureCanvasTkAgg(fig, master=label)
        self.canvas.get_tk_widget().pack(expand=1, fill=tk.BOTH, side=tk.TOP)
        #self.graph()
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

        self.copyButton = ttk.Button(self.btn, text="Copier le LaTex", width="20", command=self.copy_to_clipboard)
        self.copyButton.grid(row=0, column=2, padx=10,pady=8)

        self.themeButton = ttk.Button(self.btn, text="Thème clair", width="20", command=self.changeTheme)
        self.themeButton.grid(row=0, column=3, padx=10,pady=8)

        self.clearButton = ttk.Button(self.btn, text='Effacer',width="20", command=self.clear)
        self.clearButton.grid(row=1, column=2, padx=10)

        self.quitButton = ttk.Button(self.btn, text='Aide ?', width="20", command=self.openHelp)
        self.quitButton.grid(row=1, column=3, padx=10)
        self.btn.pack(padx=10, pady=20)
        
    def clear(self):
        '''efface le texte precedement ecris'''
        self.result = [mathObject()]
        self.elements = []
        self.precedent = [mathSymbol('')]
        self.cursor = 0
        self.rg = 0
        self.rg_prev = 0
        self.cursor_prev = 0
        self.i = [0]
        self.pos = 0.9
        self.latex_display()
        self.wx.clear()
        try : 
            self.result[self.rg].add(mathSymbol("|"), self.cursor)
            self.graph()
            self.result[self.rg].destroy(self.cursor+1)
        except :
            self.result[self.rg].add(mathSymbol("|"), self.cursor)
            self.graph()
            self.result[self.rg].destroy(self.cursor+1)

    def engine(self, temp = None):
        '''change le moteur de rendue latex'''
        if self.cobobox1.get() == "Intern Engine":
            self.engine_use = 0
        else:
            self.engine_use = 1
        self.result[self.rg].add(mathSymbol(chr(166)), self.cursor)
        self.graph()
        self.result[self.rg].destroy(self.cursor+1)

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
        self.result[self.rg].add(mathSymbol(chr(166)), self.cursor)
        self.graph()
        self.result[self.rg].destroy(self.cursor+1)
        logging.info("set text sizes : " + str(self.size))

    def action(self, touche):
        '''action sur les touches'''
        logging.info("press :" +  str(touche))

        # tableau de corespondance entre lettres normal, grec et signe mathématique
        corespondance = [
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
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
                mathSymbol('\\omicron '), #o 
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
            ],
            [   [mathSymbol('\Rightarrow '), mathSymbol('\Leftarrow ')],
                [binom()],
                [mathSymbol('\in '),mathSymbol('\supset '),mathSymbol('\subset '),mathSymbol('\supseteq '),mathSymbol('\subseteq ')],
                [e(), exp(), ln(), log()],
                [mathSymbol('\Longleftrightarrow '),mathSymbol('\Leftrightarrow ')],
                [mathSymbol('f'),mathSymbol('g'),mathSymbol('h'),mathSymbol('u')],
                [mathSymbol('\\rightarrow '),mathSymbol('\leftarrow '),mathSymbol('\leftrightarrow ')],
                [mathSymbol('h')],
                [integral(), integral2(),integral2f(), integral_double(), integral_doublef(),  integral_triple(),  integral_triplef()],
                [mathSymbol('\imath '), mathSymbol('\jmath '), mathSymbol('\Re '),mathSymbol('\Im ')],
                [system(2, 2),system(3, 2),system(4, 2),system(5, 2)],
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
            ]
        ]

        key = touche.keycode
        # Si on appuie sur une touche de controle : ctrl : grec
        if touche.keysym=='Control_L': #ctrl
            self.mode_prev = int(self.grec)+10*int(self.math)
            self.ctrl_l = True
            self.grec = not(self.grec)
            self.math = False
            if self.grec:
                self.indication.configure(text="Lettre Grecque", foreground=green)
            else:
                self.indication.configure(text="Lettre Usuelle",foreground=blue)

        # gestion du bug de la touche 'alt gr'
        elif touche.keysym=='Alt_R': 
            if self.ctrl_l:

                if self.mode_prev == 10: self.math = True
                else : self.math = False
                if self.mode_prev == 1: self.grec = True
                else : self.grec = False

                if self.math:
                    self.indication.configure(text="Mode Math", foreground=red)
                elif self.grec:
                    self.indication.configure(text="Lettre Grecque", foreground=green)
                else:
                    self.indication.configure(text="Lettre Usuelle",foreground=blue)

                self.ctrl_l = True

        
        else :
            self.ctrl_l = False
        
        ## touche sans actions
        if touche.keysym=='Control_L' or touche.keysym=='Alt_L'  or touche.keysym=='Alt_R' or key in [16, 20, 38, 40, 17, 19, 145, 35, 36, 91, 179, 175,174,173] or (self.math and touche.char=='^') or touche.char== "\\" or touche.char== "\t" or touche.char=="#" or touche.char=="`" :
            pass

        elif key == 222: #²nde (mode math)
            self.grec = False
            self.math = not(self.math)
            if self.math:
                self.indication.configure(text="Mode Math", foreground=red)
            else:
                self.indication.configure(text="Lettre Usuelle",foreground=blue)

        elif key == 39: # fleche droite ->
            self.precedent.append(mathSymbol(''))
            if len(self.result[self.rg].content) > self.cursor:
                self.cursor += 1
            else :
                try :
                    self.result[self.rg] = self.elements[len(self.elements)-1].content[self.i[len(self.i)-1]+1]
                    self.i[len(self.i)-1] += 1
                    self.cursor = 0
                except :
                    self.cursor = self.result[self.rg-1].content.index(self.elements[self.rg-1])+1
                    self.elements.pop(self.rg-1)
                    self.result.pop(self.rg)
                    self.rg = self.rg-1
                    if self.rg < 0:
                        self.rg = 0

        elif key == 37: # fleche gauche <-
            self.precedent.append(mathSymbol(''))
            if(self.cursor >= 1 and type(self.result[self.rg].content[self.cursor-1]).__name__ != "mathSymbol"):
                self.i.append(self.result[self.rg].content[self.cursor-1].imax)
                self.result.append(self.result[self.rg].content[self.cursor-1].content[self.i[len(self.i)-1]])
                self.elements.append(self.result[self.rg].content[self.cursor-1])
                self.rg = len(self.result)-1
                self.cursor = len(self.result[self.rg].content)
            elif self.cursor > 0:
                self.cursor -= 1
            elif self.cursor == 0 and self.rg == 0:
                pass
            elif self.i[len(self.i)-1] > 0:
                self.i[len(self.i)-1] -= 1
                self.result.pop(self.rg)
                self.result.append(self.elements[len(self.elements)-1].content[self.i[len(self.i)-1]])
                self.cursor = len(self.result[self.rg].content)
            elif self.i[len(self.i)-1] == 0:
                self.cursor = self.result[self.rg-1].content.index(self.elements[self.rg-1])
                self.i.pop(len(self.i)-1)
                self.result.pop(self.rg)
                self.elements.pop(self.rg-1)
                self.rg = self.rg-1

        elif key == 8: #suppr <--
            print(self.i[len(self.i)-1])
            if self.cursor != 0:
                self.precedent.append(mathSymbol(''))
                self.result[self.rg].destroy(self.cursor)
                self.cursor -= 1
            elif self.rg>0 and self.i[len(self.i)-1]==0:
                #self.precedent.append(mathSymbol(''))
                self.cursor = self.result[self.rg-1].content.index(self.elements[self.rg-1])
                self.result.pop(self.rg)
                self.elements.pop(self.rg-1)
                self.rg -= 1
                self.result[self.rg].destroy(self.cursor+1)
            elif self.rg>0 :
                self.precedent.append(mathSymbol(''))
                self.result.pop(self.rg)
                self.i[len(self.i)-1] -= 1
                self.result.append(self.elements[self.rg-1].content[self.i[len(self.i)-1]])

                self.cursor = len(self.result[self.rg].content)

        elif key == 27: #escape
            self.quiter()
        
        elif key == 46: #suppr -->
            if self.cursor != len(self.result[self.rg].content):
                self.result[self.rg].destroy(self.cursor+1)

        elif touche.char == "\x03": #ctrl-c
            self.copy_to_clipboard()
        
        elif key == 120: #F9
            c = credit()
        
        elif touche.char == "=" and self.result[0].str() == "raptor":
            v = raptor()
        ## touche qui ne depend pas du mode selectioner
        elif key==13:
            self.multiple_choice([mathSymbol('\\newline')])
            self.pos-=0.11
        elif touche.char=='=':
            self.multiple_choice([mathSymbol("="), mathSymbol("\\approx "),mathSymbol("\\neq ") ,mathSymbol("\\equiv "), mathSymbol("\\sim "),mathSymbol("\\simeq "), mathSymbol("\\propto ")])
        elif touche.char=='*':
            self.multiple_choice([mathSymbol("\\times "), mathSymbol("\\cdot "), mathSymbol("\\wedge "),mathSymbol("\\ast "), mathSymbol("\\odot "), mathSymbol("\\otimes ")])
        elif touche.char=='+':
            self.multiple_choice([mathSymbol("+ "), mathSymbol("\\pm "),mathSymbol("\\mp "),mathSymbol("\\oplus ")])
        elif touche.char=='-':
            self.multiple_choice([mathSymbol("- "), mathSymbol("\\mp "),mathSymbol("\\pm "),mathSymbol("\\ominus ")])
        elif touche.char=='!':
            self.multiple_choice([mathSymbol("! "), mathSymbol("\\neg "),mathSymbol("\\not ")])
        elif touche.char=='{':
            self.multiple_choice([ crochet()])
        elif touche.char=='}':
            self.multiple_choice([crochet()])
        elif touche.char=='&':
            self.multiple_choice([ mathSymbol("\\wedge "),mathSymbol("\\vee "),mathSymbol("& ")])
        elif key == 226: #inf</sup> '</>'
            self.multiple_choice([mathSymbol("<"), mathSymbol(">"), mathSymbol("\leq "), mathSymbol("\geq "), mathSymbol("\ll "), mathSymbol("\gg ")])
        elif touche.char=='"':
            self.multiple_choice([texte()])
        elif key == 32: #space
            self.multiple_choice([mathSymbol("\: ")])
        elif touche.char == '$':
            self.multiple_choice([mathSymbol("\$")])

        ## lettre grec (utiliser si le mode grec est activé)
        elif self.grec:
            if key >= 65 and key <91: 
                if touche.char.isupper():
                    self.precedent.append(corespondance[1][key-65])
                else:
                    self.precedent.append(corespondance[2][key-65])
                self.result[self.rg].add(self.precedent[len(self.precedent)-1], self.cursor)
                self.cursor+=1
            elif touche.char != None: #sinon caractere normaux
                self.precedent.append(mathSymbol(str(touche.char)))
                self.result[self.rg].add(self.precedent[len(self.precedent)-1], self.cursor)
                self.cursor+=1
        
        ## symbole math (utiliser si le mode math est activé)
        elif self.math:
            if touche.char == 'h':
                h = historique(self.result[0], self)
            elif key >= 65 and key <= 90: #fonction associer à une letre
                t = corespondance.copy()
                temp = t[3][key-65]
                if type(temp[0]) != str: 
                    self.multiple_choice(temp)
                else : 
                    logging.info("Fonction Math non enregistrée sur la touche : " + str(key))
            elif key == 191: #fraction touche '/'
                temp = self.result[self.rg].content[self.cursor-1]
                self.result[self.rg].destroy(self.cursor)
                fr = frac()
                self.result[self.rg].add(fr, self.cursor-1)
                self.elements.append(fr)
                self.result.append(self.result[self.rg].content[self.cursor-1].content[0])
                self.i[len(self.i)-1] = 0
                self.rg+=1
                self.cursor=1
                self.result[self.rg].add(temp, self.cursor-1)
                self.precedent.append(mathSymbol(''))
                self.result[self.rg] = self.elements[len(self.elements)-1].content[self.i[len(self.i)-1]+1]
                self.i[len(self.i)-1] += 1
                self.cursor = 0
            elif key == 221: #puissance touche '^'
                temp = [power(), indice()]
                self.multiple_choice(temp)
            elif touche.char == '(':
                self.multiple_choice([parenthese()])
            elif touche.char == ')':
                self.multiple_choice([parenthese_carre()])
            elif touche.char == '|':
                self.multiple_choice([norme(), norme2()])
            elif touche.char == '_':
                self.multiple_choice([indice()])
            elif touche.char != None: #sinon caractere normal
                self.multiple_choice([mathSymbol(touche.char.replace('^',''))])

        
        ## lettre normale (utiliser si aucun mode n'est activé)
        else:
            if touche.char != None and touche.char != '^':
                tmp = mathSymbol(str(touche.char).replace('^', ''))
                self.result[self.rg].add(tmp, self.cursor)
                self.precedent.append(tmp)
                self.cursor+=1


        self.rg_prev = self.rg
        self.cursor_prev = self.cursor
        if not(key in [17, 222,39,37,8]) and not(self.math and key==191):
            if type(self.precedent[len(self.precedent)-1]).__name__ != "mathSymbol":
                try :
                    self.result.append(self.result[self.rg].content[len(self.result[self.rg].content)-1].content[0])
                    self.i[len(self.i)-1] = 0
                except :
                    self.result.append(self.result[self.rg].content[len(self.result[self.rg].content)-1].content)
                self.elements.append(self.result[self.rg].content[len(self.result[self.rg].content)-1])
                self.rg = len(self.result)-1
                self.cursor = 0
        
        self.result[self.rg].add(mathSymbol(chr(166)), self.cursor)
        self.graph()
        self.result[self.rg].destroy(self.cursor+1)
        self.latex_display()

        #Save log
        logging.info("elements dans la piles :" + str(self.elements))
        logging.info("elements dans le niveau :" + str(self.result[self.rg].content))
        logging.info("position du cursseur :" + str(self.cursor))
        logging.info("code Latex :" + self.result[0].str())


    def multiple_choice(self, temp):
        '''permet de gerer le cas ou la fonction change lorsque l'on apuis plusieur fois sur le meme bouton'''
        
        a = True
        for i in range(0, len(temp)):
            if temp[i].__str__() == self.precedent[len(self.precedent)-1].__str__() and self.prev_time > (millis()-900):
                if self.rg != self.rg_prev:
                    self.result.pop(self.rg)
                    self.elements.pop(self.rg-1)
                    self.rg=self.rg_prev
                    self.cursor = self.cursor_prev
                self.result[self.rg].destroy(self.cursor)
                self.cursor -= 1
                l = i+1
                if l>=len(temp): l = 0
                self.precedent[len(self.precedent)-1] = temp[l]
                a = False
                break
        if a:
            self.precedent.append(temp[0])
            l=0
            try:
                self.multi.master.destroy()
            except:
                pass
            self.multi = multi(self, root, temp, l)
        else:
            self.multi.modifie(l, temp)
        self.result[self.rg].add(self.precedent[len(self.precedent)-1], self.cursor)
        self.cursor+=1
        self.prev_time = millis()

    def graph(self):
        '''permet de gerer le graphique et l'affichage des Math'''
        # Get the Entry Input
        tmptext = self.result[0].str()
        tmptext = tmptext.replace(r"\newline", "$ \n $")
        tmptext = tmptext.replace(r"æ", "a")
        # Clear any previous Syntax from the figure
        if self.engine_use == 0:
            try : 
                matplotlib.rcParams['text.usetex'] = False
                self.wx.clear()
                self.wx.text(-0.1, self.pos, r"$"+tmptext.replace(r"\text",r"\mathrm")+"$", fontsize = self.size, color = whith)
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
                
            else :
                self.btn['bg'] = bg_white
                self.label['bg'] = bg_white
                app['bg'] = bg_white
                self.latex_display()
                self.themeButton['text']="Thème sombre"
                settings['settings']['theme']="light"
            
            f.seek(0)
            f.write(json.dumps(settings))
            f.truncate()         
        
    def openHelp(self) :
        '''ouvre la fenêtre d'aide'''
        self.help = help()




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
            f.write('{"settings": {"theme": "dark"}}')
    app.mainloop()

