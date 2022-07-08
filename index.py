import tkinter as tk
from tkinter import ttk
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from latex import *
import pyperclip

matplotlib.use('TkAgg')
#matplotlib.rcParams['font.size'] = 20
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.preamble'] = r'\usepackage{{amsmath}}'


class mainWindow(tk.Frame):
    def __init__(self, master=None):
        master.bind("<KeyPress>", self.action)
        master.bind("<Button-1>",self.copy_to_clipboard)
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
        self.result = [mathObject()]
        self.precedent = [mathSymbol('')]
        self.elements = []
        self.grec = False
        self.math = False
        self.createWidgets()

    def createWidgets(self):
        self.label = tk.Label(self)
        self.label.bind("<Button-1>",self.copy_to_clipboard)

        self.label.pack()

        self.indication = tk.Label(self, text="Lettre Usuelle", font=("Arial", 12), fg='#000066')
        self.indication.pack()
        self.indication.bind("<Button-1>",self.copy_to_clipboard)

        label = tk.Frame(self)
        label.pack()

        # Define the figure size and plot the figure
        fig = plt.Figure(figsize=(200, 2), dpi=self.dpi)
        self.wx = fig.add_subplot(111)
        self.wx.get_xaxis().set_visible(False)
        self.wx.get_yaxis().set_visible(False)
        self.wx.patch.set_visible(False)
        self.wx.axis('off')
        self.canvas = FigureCanvasTkAgg(fig, master=label)
        self.canvas.get_tk_widget().pack(expand=1, fill=tk.BOTH, side=tk.TOP)
        #self.graph()
        self.latex_display()


        self.btn = tk.Frame(self)

        liste = []
        for i in range(1, 30):
            liste.append(i)

        s1 = tk.Label(self.btn, text="Moteur LaTex :", font=("Arial", 10))
        s1.grid(row=0, column=0)

        self.cobobox1 = ttk.Combobox(self.btn, values=["Intern Engine (MatPlot)", "Extern Engine"], state="readonly")
        self.cobobox1.bind("<<ComboboxSelected>>", self.engine)
        self.cobobox1.current(0)
        self.cobobox1.grid(row=1, column=0)


        s = tk.Label(self.btn, text="Taille :", font=("Arial", 10))
        s.grid(row=0, column=1)

        self.cobobox = ttk.Combobox(self.btn, values=liste, state="readonly")
        self.cobobox.bind("<<ComboboxSelected>>", self.change_size)
        self.cobobox.current(self.size-1)
        self.cobobox.grid(row=1, column=1)
        
        self.clearButton = tk.Button(self.btn, text='Effacer',width="20", command=self.clear,  font=("Arial", 11))
        #self.clearButton.pack()
        self.clearButton.grid(row=1, column=2)

        self.quitButton = tk.Button(self.btn, text='Quit', width="20", command=self.quit,  font=("Arial", 11))
        self.quitButton.grid(row=1, column=3)
        #self.quitButton.pack()
        self.btn.pack()

    def clear(self):
        self.result = [mathObject()]
        self.elements = []
        self.precedent = [mathSymbol('')]
        self.cursor = 0
        self.rg = 0
        self.rg_prev = 0
        self.cursor_prev = 0
        self.i = [0]
        self.pos = 0.9

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
        if self.cobobox1.get() == "Intern Engine":
            self.engine_use = 0
        else:
            self.engine_use = 1
        self.result[self.rg].add(mathSymbol(chr(166)), self.cursor)
        self.graph()
        self.result[self.rg].destroy(self.cursor+1)

    def latex_display(self):
        # Get the Entry Input
        tmptext = self.result[0].str().replace('\\newline', chr(10))
        self.label.configure(text=tmptext, font=("Arial", 11))

    def change_size(self, temp):
        self.size = int(self.cobobox.get())
        self.result[self.rg].add(mathSymbol(chr(166)), self.cursor)
        self.graph()
        self.result[self.rg].destroy(self.cursor+1)
        print(self.size)

    def action(self, touche):
        print(touche)

        corespondance = [
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
            [mathSymbol('A'), mathSymbol('B'), mathSymbol('\\Gamma '), mathSymbol('\\Delta '), mathSymbol('E'), mathSymbol('Z'), mathSymbol('H'), mathSymbol('\\Theta '), mathSymbol('I'), mathSymbol('K'), mathSymbol('\\Lambda '), mathSymbol('M'), mathSymbol('N'), mathSymbol('\\Xi '), mathSymbol('O'), mathSymbol('\\Pi '), mathSymbol('P'), mathSymbol('\\Sigma '), mathSymbol('T'), mathSymbol('Y'), mathSymbol('\\Phi '), mathSymbol('X'), mathSymbol('\\Psi '), mathSymbol('\\Omega ')],
            [mathSymbol('\\alpha '), mathSymbol('\\beta '), mathSymbol('\\gamma '), mathSymbol('\\delta '), mathSymbol('\\epsilon '), mathSymbol('\\zeta '), mathSymbol('\\eta '), mathSymbol('\\theta '), mathSymbol('\\iota '), mathSymbol('\\kappa '), mathSymbol('\\lambda '), mathSymbol('\\mu '), mathSymbol('\\nu '), mathSymbol('\\xi '), mathSymbol('\\omicron '), mathSymbol('\\pi '), mathSymbol('\\rho '), mathSymbol('\\sigma '), mathSymbol('\\tau '), mathSymbol('\\upsilon '), mathSymbol('\\phi '), mathSymbol('\\chi '), mathSymbol('\\psi '), mathSymbol('\\omega ')],
            [   [mathSymbol('\Rightarrow '), mathSymbol('\Leftarrow ')],
                [binom()],
                [mathSymbol('\in '),mathSymbol('\supset '),mathSymbol('\subset '),mathSymbol('\supseteq '),mathSymbol('\subseteq ')],
                ['d'],
                [mathSymbol('\Longleftrightarrow '),mathSymbol('\Leftrightarrow ')],
                [mathSymbol('\\rightarrow '),mathSymbol('\leftarrow '),mathSymbol('\leftrightarrow ')],
                [system(3, 2)],
                ['h'],
                [integral(), integral2(),integral2f(), integral_double(), integral_doublef(),  integral_triple(),  integral_triplef()],
                [mathSymbol('\imath '), mathSymbol('\jmath '), mathSymbol('\Re '),mathSymbol('\Im ')],
                ['k'],
                [ln(), log(), e(), exp()],
                [lim1(), lim()],
                ['n'],
                [sum(), sum1(), mathSymbol('\sum ')],
                [prod(), prod1(), mathSymbol('\prod ')],
                [frac()],
                [mathSymbol('\mathbb{R} '),mathSymbol('\mathbb{C} '),mathSymbol('\\mathbb{N} '),mathSymbol('\mathbb{Z} '),mathSymbol('\mathbb{Q} ')],
                [sqrt(), sqrt_n()],
                [cos(), sin(), tan()],
                [mathSymbol('\cup '), mathSymbol('\cap '), union(), intersection()],
                [vect()],
                [mathSymbol('\\forall '), mathSymbol('\\exists ')],
                [e(), exp(), ln(), log()],
                [arccos(), arcsin(), arctan()],
                [mathSymbol('\infty '), mathSymbol('+\infty '), mathSymbol('-\infty '), mathSymbol('\pm\infty ')],
            ]
        ]

        key = touche.keycode
        # Si on appuie sur une touche de controle : ctrl : grec ou alt : math
        if touche.keysym=='Control_L': #ctrl
            self.mode_prev = int(self.grec)+10*int(self.math)
            self.ctrl_l = True
            self.grec = not(self.grec)
            self.math = False
            if self.grec:
                self.indication.configure(text="Lettre Grec", fg='#339933')
            else:
                self.indication.configure(text="Lettre Usuelle",fg='#000066')

        elif touche.keysym=='Alt_R': 
            if self.ctrl_l:

                if self.mode_prev == 10: self.math = True
                else : self.math = False
                if self.mode_prev == 1: self.grec = True
                else : self.grec = False

                if self.math:
                    self.indication.configure(text="Mode Math", fg='#990033')
                elif self.grec:
                    self.indication.configure(text="Lettre Grec", fg='#339933')
                else:
                    self.indication.configure(text="Lettre Usuelle",fg='#000066')
                self.ctrl_l = True
        
        else :
            self.ctrl_l = False

        if touche.keysym=='Control_L' or touche.keysym=='Alt_L':
            pass
        elif key == 222: #²nde
            self.grec = False
            self.math = not(self.math)
            if self.math:
                self.indication.configure(text="Mode Math", fg='#990033')
            else:
                self.indication.configure(text="Lettre Usuelle",fg='#000066')

        elif key == 39: # ->
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
                    print(self.elements)
                    print(self.rg)
                    self.elements.pop(self.rg-1)
                    self.result.pop(self.rg)
                    self.rg = self.rg-1
                    if self.rg < 0:
                        self.rg = 0

        elif key == 37: # <-
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
            if self.cursor != 0:
                self.precedent.append(mathSymbol(''))
                self.result[self.rg].destroy(self.cursor)
                self.cursor -= 1
            elif self.rg>0 and self.i[len(self.i)-1]==0:
                self.precedent.append(mathSymbol(''))
                self.cursor = self.cursor_prev
                self.result.pop(self.rg)
                self.elements.pop(self.rg-1)
                self.rg -= 1
                self.result[self.rg].destroy(self.cursor)
                self.cursor -= 1
            elif self.rg>0 :
                self.precedent.append(mathSymbol(''))
                self.result.pop(self.rg)
                self.i[len(self.i)-1] -= 1
                self.result.append(self.elements[self.rg-1].content[self.i[len(self.i)-1]])

                self.cursor = len(self.result[self.rg].content)

        ## touche sans actions
        elif key in [16, 20] or (self.math and touche.char=='^'):
            pass
        
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

        ## letre grec
        elif self.grec:
            if key >= 65 and key <88: 
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
        
        ## symbole math
        elif self.math:
            valid = True
            if key >= 65 and key <=90: #fonction associer à une letre
                t = corespondance.copy()
                temp = t[3][key-65]
                if type(temp[0]) != str: 
                    a = True
                    for i in range(0, len(temp)):
                        if temp[i].__str__() == self.precedent[len(self.precedent)-1].__str__():
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
                else : 
                    print("fonction non enregistrer")
                    valid = False
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
                valid = False
                self.result[self.rg] = self.elements[len(self.elements)-1].content[self.i[len(self.i)-1]+1]
                self.i[len(self.i)-1] += 1
                self.cursor = 0
            elif key == 221: #puissance touche '^'
                temp = [power(), indice()]
                a = True
                for i in range(0, len(temp)):
                    if temp[i].__str__() == self.precedent[len(self.precedent)-1].__str__():
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
            elif touche.char == '(':
                self.precedent.append(parenthese())
            elif touche.char == ')':
                self.precedent.append(parenthese_carre())
            elif touche.char == '|':
                self.precedent.append(norme())
            elif touche.char != None: #sinon caractere normaux
                self.precedent.append(mathSymbol(str(touche.char)))

            else : valid = False
            if valid: #si le caractere est valide -> ajout dans la liste
                self.result[self.rg].add(self.precedent[len(self.precedent)-1], self.cursor)
                self.cursor+=1

        elif key == 32: #space
            self.precedent.append(mathSymbol("\: "))
            self.result[self.rg].add(self.precedent[len(self.precedent)-1], self.cursor)
            self.cursor+=1
        ## lettre normale
        else:
            if touche.char != None:
                tmp = mathSymbol(str(touche.char))
                self.result[self.rg].add(tmp, self.cursor)
                self.precedent.append(tmp)
                self.cursor+=1


        self.rg_prev = self.rg
        self.cursor_prev =self.cursor
        print(self.result[self.rg].str())
        if not(key in [17, 222,39,37,8]) or not(self.math and key==191):
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
        print(self.elements)
        print(self.result)
        print(self.result[self.rg].content)
        print(self.cursor)

    def multiple_choice(self, temp):
        a = True
        for i in range(0, len(temp)):
            if temp[i].__str__() == self.precedent[len(self.precedent)-1].__str__():
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
        self.result[self.rg].add(self.precedent[len(self.precedent)-1], self.cursor)
        self.cursor+=1

    def graph(self):
        # Get the Entry Input
        tmptext = self.result[0].str()
        tmptext = tmptext.replace(r"\newline", "$ \n $")
        tmptext = tmptext.replace(r"æ", "a")
        # Clear any previous Syntax from the figure
        if self.engine_use == 0:
            try : 
                matplotlib.rcParams['text.usetex'] = False
                self.wx.clear()
                self.wx.text(-0.1, self.pos, r"$"+tmptext.replace(r"\text",r"\mathrm")+"$", fontsize = self.size)
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

    def copy_to_clipboard(self, temp):
        tmptext = self.result[0].str().replace(r"\newline", chr(10))
        pyperclip.copy(tmptext)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("MathClav")
    app = mainWindow(root)
    app.mainloop()

