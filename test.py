import tkinter as tk
from unittest import result
from xmlrpc.client import Server
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import keyboard
from latex import *

matplotlib.use('TkAgg')

corespondance = [
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
    [mathSymbol('\\alpha '), mathSymbol('\\beta '), mathSymbol('\\gamma '), mathSymbol('\\delta '), mathSymbol('\\epsilon '), mathSymbol('\\zeta '), mathSymbol('\\eta '), mathSymbol('\\theta '), mathSymbol('\\iota '), mathSymbol('\\kappa '), mathSymbol('\\lambda '), mathSymbol('\\mu '), mathSymbol('\\nu '), mathSymbol('\\xi '), mathSymbol('\\omicron '), mathSymbol('\\pi '), mathSymbol('\\rho '), mathSymbol('\\sigma '), mathSymbol('\\tau '), mathSymbol('\\upsilon '), mathSymbol('\\phi '), mathSymbol('\\chi '), mathSymbol('\\psi '), mathSymbol('\\omega ')],
    [[mathSymbol('\Rightarrow ')],[sqrt()],[mathSymbol('\supset '),mathSymbol('\subset '),mathSymbol('\supseteq '),mathSymbol('\subseteq ')],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
]


class mainWindow(tk.Frame):
    def __init__(self, master=None):
        master.bind("<KeyPress>", self.action)
        tk.Frame.__init__(self, master)
        self.pack()
        self.rg = 0
        self.cursor = 0
        self.result = [mathObject()]
        self.precedent = []
        self.grec = False
        self.math = False
        self.createWidgets()

    def createWidgets(self):
        label = tk.Label(self)
        label.pack()

        # Define the figure size and plot the figure
        fig = matplotlib.figure.Figure(figsize=(7, 4), dpi=100)
        self.wx = fig.add_subplot(111)
        self.wx.get_xaxis().set_visible(False)
        self.wx.get_yaxis().set_visible(False)
        self.canvas = FigureCanvasTkAgg(fig, master=label)
        self.canvas.get_tk_widget().pack(expand=1)
        self.canvas._tkcanvas.pack(expand=1)
        self.elements = []
        #self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        #self.canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)

        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

    def action(self, touche):
        print(touche)

        corespondance = [
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
            [mathSymbol('\\alpha '), mathSymbol('\\beta '), mathSymbol('\\gamma '), mathSymbol('\\delta '), mathSymbol('\\epsilon '), mathSymbol('\\zeta '), mathSymbol('\\eta '), mathSymbol('\\theta '), mathSymbol('\\iota '), mathSymbol('\\kappa '), mathSymbol('\\lambda '), mathSymbol('\\mu '), mathSymbol('\\nu '), mathSymbol('\\xi '), mathSymbol('\\omicron '), mathSymbol('\\pi '), mathSymbol('\\rho '), mathSymbol('\\sigma '), mathSymbol('\\tau '), mathSymbol('\\upsilon '), mathSymbol('\\phi '), mathSymbol('\\chi '), mathSymbol('\\psi '), mathSymbol('\\omega ')],
            [[mathSymbol('\Rightarrow ')],[],[mathSymbol('\supset '),mathSymbol('\subset '),mathSymbol('\supseteq '),mathSymbol('\subseteq ')],['d'],['e'],['f'],['g'],['h'],['i'],['j'],['k'],['l'],['m'],['n'],['o'],['p'],['q'],['r'],[sqrt()],['t'],['u'],['v'],['w'],['x'],['y'],['z']]
        ]

        key = touche.keycode
        # Si on appuie sur une touche de controle : ctrl : grec ou alt : math
        if key == 17: 
            self.grec = not(self.grec)
            self.math = False
        elif key == 222: 
            self.grec = False
            self.math = not(self.math)

        elif key == 39: # ->
            if len(self.result[self.rg].content) > self.cursor:
                self.cursor += 1
            else :
                try :
                    self.result[self.rg] = self.elements[len(self.elements)-1].content[self.i+1]
                    self.i += 1
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
            if(self.cursor > 1 and type(self.result[self.rg].content[self.cursor-1]).__name__ != "mathSymbol"):
                try :
                    if(self.i == 0):
                        self.i = self.result[self.rg].content[self.cursor-1].imax
                    elif(self.rg > 0):
                        self.i -= 1
                        self.result.pop(self.rg)
                        self.elements.pop(self.rg-1)
                        self.rg = self.rg-1

                    self.result.append(self.result[self.rg].content[self.cursor-1].content[self.i])
                    self.elements.append(self.result[self.rg].content[self.cursor-1])
                    self.rg = len(self.result)-1
                except:
                    self.result.append(self.result[self.rg].content.content[self.i])
                    self.elements.append(self.result[self.rg].content)
                    self.rg = len(self.result)-1
            elif self.cursor > 0:
                self.cursor -= 1
            else :
                test = False
                print(self.i)
                print(self.rg)
                print(self.result)
                print(self.elements)
                try:
                    try :
                        if(self.i == 0):
                            self.i = self.result[self.rg].content[self.cursor-1].imax
                        elif(self.rg > 0):
                            self.i -= 1
                            self.cursor = self.result[self.rg-1].content.index(self.elements[self.rg-1])+1
                            self.result.pop(self.rg)
                            self.elements.pop(self.rg-1)
                            self.rg = self.rg-1
                        self.result.append(self.result[self.rg].content[self.cursor-1].content[self.i])
                        self.elements.append(self.result[self.rg].content[self.cursor-1])
                        self.rg = len(self.result)-1
                        self.cursor = len(self.result[self.rg].content)
                    except:
                        self.result.append(self.result[self.rg].content.content[self.i])
                        self.elements.append(self.result[self.rg].content)
                except:
                    self.cursor = self.result[self.rg-1].content.index(self.elements.pop(self.rg-1))
                    self.result.pop(self.rg)
                    self.elements.pop(self.rg-1)
                    self.rg -= 1

        elif key == 8:
            self.result[self.rg].destroy(self.cursor)
            self.cursor -= 1
            self.graph()
        
        elif key == 16:
            pass

        ## letre grec
        elif self.grec:
            if key >= 65 and key <=88: self.precedent.append(corespondance[2][key-65])
            else : self.precedent.append(mathSymbol(touche.char))
        
        ## symbole math
        elif self.math:
            if key >= 65 and key <=88: 
                t = corespondance.copy()
                temp = t[3][key-65]
                if self.precedent[len(self.precedent)-1] in temp:
                    self.result[self.rg].destroy()
                    l = temp.index(self.precedent[len(self.precedent)-1])+1
                    if l>=len(temp): l = 0
                    self.precedent[len(self.precedent)-1] = temp[l]
                else:
                    self.precedent.append(temp[0])
            elif key == 191:
                self.precedent.append(frac())
            else : self.precedent.append(mathSymbol(touche.char))
            self.result[self.rg].add(self.precedent[len(self.precedent)-1], self.cursor)
            self.cursor+=1

        ## lettre normale
        else:
            tmp = mathSymbol(touche.char)
            self.result[self.rg].add(tmp, self.cursor)
            self.precedent.append(tmp)
            self.cursor+=1

        print(self.result[self.rg].str())
        if not(key in [17, 222,39,37,8]):
            if type(self.precedent[len(self.precedent)-1]).__name__ != "mathSymbol":
                try :
                    self.result.append(self.result[self.rg].content[len(self.result[self.rg].content)-1].content[0])
                    self.i = 0
                except :
                    self.result.append(self.result[self.rg].content[len(self.result[self.rg].content)-1].content)
                self.elements.append(self.result[self.rg].content[len(self.result[self.rg].content)-1])
                self.rg = len(self.result)-1
                self.cursor = 0
        
        self.graph()
        print(self.elements)
        print(self.result)
        print(self.result[self.rg].content)
        print(self.cursor)

    def graph(self):
        # Get the Entry Input
        tmptext = self.result[0].str()
        # Clear any previous Syntax from the figure
        self.wx.clear()
        self.wx.text(0.2, 0.6, (r"$"+tmptext+"$"), fontsize = 11)
        self.canvas.draw()

if __name__ == '__main__':
    root = tk.Tk()
    app = mainWindow(root)
    app.mainloop()


