import tkinter as tk
from turtle import color
from unittest import result
from xmlrpc.client import Server
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import keyboard
from latex import *
import pyperclip
matplotlib.use('TkAgg')


class mainWindow(tk.Frame):
    def __init__(self, master=None):
        master.bind("<KeyPress>", self.action)
        tk.Frame.__init__(self, master)
        self.pack()
        self.rg = 0
        self.rg_prev = 0
        self.cursor = 0
        self.cursor_prev = 0
        self.i = [0]
        self.n = 0
        self.result = [mathObject()]
        self.precedent = [mathSymbol('')]
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

        label = tk.Label(self)
        label.pack()

        # Define the figure size and plot the figure
        fig = matplotlib.figure.Figure(figsize=(2000, 1), dpi=100)
        self.wx = fig.add_subplot(111)
        self.wx.get_xaxis().set_visible(False)
        self.wx.get_yaxis().set_visible(False)
        self.wx.patch.set_visible(False)
        self.wx.axis('off')
        self.canvas = FigureCanvasTkAgg(fig, master=label)
        self.canvas.get_tk_widget().pack(expand=1, fill=tk.BOTH, side=tk.TOP)
        self.canvas._tkcanvas.pack(expand=1, fill=tk.BOTH, side=tk.TOP)
        self.elements = []
        #self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        #self.canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)
        self.latex_display()
        self.quitButton = tk.Button(self, text='Quit', command=self.quit,  font=("Arial", 11))
        self.quitButton.pack()

    def latex_display(self):
        # Get the Entry Input
        tmptext = self.result[0].str()
        self.label.configure(text=tmptext, font=("Arial", 11))

    def action(self, touche):
        print(touche)

        corespondance = [
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
            [mathSymbol('\\Alpha '), mathSymbol('\\Beta '), mathSymbol('\\Gamma '), mathSymbol('\\Delta '), mathSymbol('\\Epsilon '), mathSymbol('\\Zeta '), mathSymbol('\\Eta '), mathSymbol('\\Theta '), mathSymbol('\\Iota '), mathSymbol('\\Kappa '), mathSymbol('\\Lambda '), mathSymbol('\\Mu '), mathSymbol('\\Nu '), mathSymbol('\\Xi '), mathSymbol('\\Omicron '), mathSymbol('\\Pi '), mathSymbol('\\Rho '), mathSymbol('\\Sigma '), mathSymbol('\\Tau '), mathSymbol('\\Upsilon '), mathSymbol('\\Phi '), mathSymbol('\\Chi '), mathSymbol('\\Psi '), mathSymbol('\\Omega ')],
            [mathSymbol('\\alpha '), mathSymbol('\\beta '), mathSymbol('\\gamma '), mathSymbol('\\delta '), mathSymbol('\\epsilon '), mathSymbol('\\zeta '), mathSymbol('\\eta '), mathSymbol('\\theta '), mathSymbol('\\iota '), mathSymbol('\\kappa '), mathSymbol('\\lambda '), mathSymbol('\\mu '), mathSymbol('\\nu '), mathSymbol('\\xi '), mathSymbol('\\omicron '), mathSymbol('\\pi '), mathSymbol('\\rho '), mathSymbol('\\sigma '), mathSymbol('\\tau '), mathSymbol('\\upsilon '), mathSymbol('\\phi '), mathSymbol('\\chi '), mathSymbol('\\psi '), mathSymbol('\\omega ')],
            [   [mathSymbol('\Rightarrow '), mathSymbol('\Leftarrow ')],
                ['b'],
                [mathSymbol('\in '),mathSymbol('\supset '),mathSymbol('\subset '),mathSymbol('\supseteq '),mathSymbol('\subseteq ')],
                ['d'],
                [mathSymbol('\Longleftrightarrow '),mathSymbol('\Leftrightarrow ')],
                [mathSymbol('\\rightarrow '),mathSymbol('\leftarrow '),mathSymbol('\leftrightarrow ')],
                ['g'],['h'],
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
            self.grec = not(self.grec)
            self.math = False
            if self.grec:
                self.indication.configure(text="Lettre Grec", fg='#339933')
            else:
                self.indication.configure(text="Lettre Usuelle",fg='#000066')

        elif key == 222: #alt
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
        elif key in [16, 20]:
            pass
        
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
        

        ## letre grec
        elif self.grec:
            if key >= 65 and key <88: 
                if touche.char.isupper():
                    print(corespondance[2][key-65].content[0])
                    corespondance[2][key-65].content[0].upper()
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
        
        self.result[self.rg].add(mathSymbol("|"), self.cursor)
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
        # Clear any previous Syntax from the figure
        self.wx.clear()
        print("$"+tmptext+"$")
        self.wx.text(-0.1, 0.6, ("$"+tmptext+"$"), fontsize = 11)
        self.wx.patch.set_visible(False)
        self.wx.axis('off')
        self.canvas.draw()

    def copy_to_clipboard(self, temp):
        tmptext = self.result[0].str()
        pyperclip.copy(tmptext)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("MathClav")
    app = mainWindow(root)
    app.mainloop()


