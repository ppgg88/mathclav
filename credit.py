# MathClav v0.3  
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
from matplotlib.pyplot import margins
import pyglet
import sv_ttk
import webbrowser as wb
from PIL import ImageTk, Image
import json
import globals as g

#constantes couleurs:

g.initialize()

pyglet.font.add_file("Lato-Regular.ttf")
data_path = g.data_path
    
class credit(tk.Frame):
    def __init__(self):
        master = tk.Toplevel()
        master.title("MathClav - Credit")
        master.iconbitmap('favicon.ico')

        master.tk.call(sv_ttk.set_theme("dark"))

        settings = json.load(open(data_path+'\settings\settings.json'))
        if settings['settings']['theme'] == "light" :
            master.tk.call(sv_ttk.toggle_theme())
        tk.Frame.__init__(self, master)

        if sv_ttk.get_theme()=="dark" :
            l = tk.Label(master, text="MathClav V0.2 \nPar : Team SchnakyX & apparentés (TS&a) \n\nLicence (CC BY-NC-SA 4.0) 2022 - MathClav \nThis work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0\n\n Lien : https://sourceforge.net/p/mathclav/ \n\n Nous contacter : paul.giroux87@gmail.com ", font=("Helvetica", 10), bg=g.bgMath, fg=g.whith)
        else :
            l = tk.Label(master, text="MathClav V0.2 \nPar : Team SchnakyX & apparentés (TS&a) \n\nLicence (CC BY-NC-SA 4.0) 2022 - MathClav \nThis work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0\n\n Lien : https://sourceforge.net/p/mathclav/ \n\n Nous contacter : paul.giroux87@gmail.com ", font=("Helvetica", 10), bg=g.bgMath_white, fg='black')
        l.pack(ipady=15)
        
        self.btn = tk.Frame(self)

        self.quitButton = ttk.Button(self.btn, text='Quitter', width="15", command=master.destroy)
        self.quitButton.grid(row=0, column=0, padx=10, pady=10)
        
        self.contact = ttk.Button(self.btn, text='Nous contacter', width="15", command=self.contact)
        self.contact.grid(row=0, column=1, padx=10, pady=10)
        
        self.doc = ttk.Button(self.btn, text='Documentation', width="15", command=self.doc)
        self.doc.grid(row=0, column=2, padx=10, pady=10)
        
        self.btn.pack()
        self.pack()

        self.mainloop()

    def contact(self):
        wb.open("mailto:paul.giroux87@gmail.com")

    def doc(self):
        wb.open("https://sourceforge.net/p/mathclav/")



class raptor(tk.Frame):
    def __init__(self):
        master = tk.Toplevel()
        master.title("MathClav - Credit")
        master.iconbitmap('favicon.ico')

        master.tk.call(sv_ttk.set_theme("dark"))

        settings = json.load(open(data_path+'\settings\settings.json'))
        if settings['settings']['theme'] == "light" :
            master.tk.call(sv_ttk.toggle_theme())
        tk.Frame.__init__(self, master)

        img = ImageTk.PhotoImage(Image.open('raptor.jpg').resize((300,300), Image.ANTIALIAS))
        panel = tk.Label(self, image = img)
        panel.pack(side = "bottom", fill = "both", expand = "yes")
        
        self.btn = tk.Frame(self)

        self.quitButton = ttk.Button(self.btn, text='Quitter', width="15", command=master.destroy)
        self.quitButton.grid(row=0, column=0, padx=10, pady=10)
        
        self.btn.pack()
        self.pack()

        self.mainloop()

if __name__ == '__main__':
    #c = credit()
    v = raptor()

