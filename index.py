import tkinter as tk
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import keyboard

matplotlib.use('TkAgg')

corespondance = [
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
    ['\\alpha ', '\\beta ', '\\gamma ', '\\delta ', '\\epsilon ', '\\zeta ', '\\eta ', '\\theta ', '\\iota ', '\\kappa ', '\\lambda ', '\\mu ', '\\nu ', '\\xi ', '\\omicron ', '\\pi ', '\\rho ', '\\sigma ', '\\tau ', '\\upsilon ', '\\phi ', '\\chi ', '\\psi ', '\\omega '],
    [[r'\Rightarrow '],[r'\sqrt{æ} '],['\supset ','\subset ','\supseteq ','\subseteq '],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
]


class mainWindow(tk.Frame):
    def __init__(self, master=None):
        master.bind("<KeyPress>", self.action)
        tk.Frame.__init__(self, master)
        self.pack()
        self.result= ""
        self.precedent = []
        self.trou = -1
        self.Rtrou = ""
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
        #self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        #self.canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)

        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

    def action(self, touche):
        print(touche)
        key = touche.keycode

        # Si on appuie sur une touche de controle : ctrl : grec ou alt : math
        if key == 17: 
            self.grec = not(self.grec)
            self.math = False
        elif key == 16: 
            self.grec = False
            self.math = not(self.math)
        elif key == 39:
            self.remplir()
        elif key == 8:
            self.result = self.result[:-len(self.precedent[len(self.precedent)-1])]
            self.precedent.pop(len(self.precedent)-1)
            self.graph()



        ## letre grec
        elif self.grec:
            if key >= 65 and key <=88: self.precedent.append(corespondance[2][key-65])
            else : self.precedent.append(touche.char)
            if self.trou == -1:
                self.result += self.precedent[len(self.precedent)-1]
                self.remplir()
            else:
                self.Rtrou += self.precedent[len(self.precedent)-1]
                self.result = self.result[:self.trou] +self.Rtrou +self.result[self.trou+1:]
        ## symbole math
        elif self.math:
            if key >= 65 and key <=88: 
                temp = corespondance[3][key-65]
                if self.precedent[len(self.precedent)-1] in temp:
                    self.result = self.result[:-len(self.precedent[len(self.precedent)-1])]
                    l = temp.index(self.precedent[len(self.precedent)-1])+1
                    if l>=len(temp): l = 0
                    self.precedent[len(self.precedent)-1] = temp[l]
                else:
                    self.precedent.append(temp[0])
            else : self.precedent.append(touche.char)
            if self.trou == -1:
                self.result += self.precedent[len(self.precedent)-1]
                self.remplir()
            else:
                self.Rtrou += self.precedent[len(self.precedent)-1]
                self.result = self.result[:self.trou] +self.Rtrou +self.result[self.trou+1:]

        ## lettre normale
        else:
            self.precedent.append(touche.char)
            if self.trou == -1:
                self.result += self.precedent[len(self.precedent)-1]
                self.remplir()
            else:
                t = 1
                if self.Rtrou == "" : t=0
                self.Rtrou += self.precedent[len(self.precedent)-1]
                print(len(self.Rtrou))
                self.result = self.result[:self.trou] +self.Rtrou +self.result[self.trou+len(self.Rtrou)-t:]
 

        print(self.result)
        self.graph()

    def remplir(self):
        self.trou = -1
        self.Rtrou = ""
        for i in range(len(self.result)):
            if self.result[i] == 'æ':
                self.trou = i
                break
        

    def graph(self):
        # Get the Entry Input
        tmptext = self.result
        # Clear any previous Syntax from the figure
        self.wx.clear()
        self.wx.text(0.2, 0.6, (r"$"+tmptext+"$"), fontsize = 11)
        self.canvas.draw()

if __name__ == '__main__':
    root = tk.Tk()
    app = mainWindow(root)
    app.mainloop()
    root.destroy()  # optional; see description below.


