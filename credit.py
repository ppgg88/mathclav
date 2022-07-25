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
from matplotlib.pyplot import margins
import pyglet
import sv_ttk
import webbrowser as wb
import os
import json

#constantes couleurs:
bg = '#121212'
bgMath = '#3A3A3A'
bg_buton = '#2e2e2e'
blue = '#b3d0ff'
red = '#ffa1c3'
green = '#c9ffc9'
whith = '#f0f0f0'

pyglet.font.add_file("Lato-Regular.ttf")
data_path = os.path.expanduser('~')+"\AppData\Local\mathclav"

if not(os.path.exists(data_path)):
    os.makedirs(data_path)
    os.makedirs(data_path+"\historique")
    os.makedirs(data_path+"\log")
    os.makedirs(data_path+"\settings")

# for user they alredy have download verssion 0.1 of MathClav
if not(os.path.exists(data_path+"\settings")):
    os.makedirs(data_path+"\settings")
    
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

        l = tk.Label(master, text="MathClav V0.2 \nBy : Team SchnakyX & apparentés (TS&a) \n\nLicence (CC BY-NC-SA 4.0) 2022 - MathClav \nThis work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0\n\n Lien : https://sourceforge.net/p/mathclav/ \n\n Contact us : paul.giroux87@gmail.com ", font=("Helvetica", 10), bg=bgMath, fg=whith)
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

if __name__ == '__main__':
    c = credit()

