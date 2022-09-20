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
import tkinter.font as font
import os
import json
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import globals as g

matplotlib.use('TkAgg')

#constantes couleurs:

g.initialize()

pyglet.font.add_file("Lato-Regular.ttf")
data_path = g.data_path

class help(tk.Frame):
    def __init__(self, corespondance):
        self.corespondance = corespondance
        master = tk.Toplevel()
        master.title("MathClav - Aide")
        master.iconbitmap('favicon.ico')

        master.tk.call(sv_ttk.set_theme("dark"))
        settings = json.load(open(data_path+'\settings\settings.json'))
        if settings['settings']['theme'] == "light" :
            master.tk.call(sv_ttk.toggle_theme())
        tk.Frame.__init__(self, master)
        if settings['settings']['theme'] == "light" :
            img = ImageTk.PhotoImage(Image.open('clavier.png').resize((1000,400), Image.ANTIALIAS))
        else :
            img = ImageTk.PhotoImage(Image.open('clavier_dark.png').resize((1000,400), Image.ANTIALIAS))
        panel = tk.Label(self, image = img)
        panel.pack(side = "bottom", fill = "both", expand = "yes")
        
        self.btn = tk.Frame(self)
        
        s = ttk.Style()
        s.configure('my.TButton', font=('Helvetica', 14, 'bold'))
        self.quitButton = ttk.Button(self.btn, text='Quitter', width="40", command=master.destroy, style='my.TButton')
        self.quitButton.grid(row=0, column=1, padx=10, pady=10)
        self.helpButton = ttk.Button(self.btn, text='Vue Liste', width="40", command=self.vuelist, style='my.TButton')
        self.helpButton.grid(row=0, column=0, padx=10, pady=10)
        
        self.btn.pack()
        self.pack()

        self.mainloop()
    
    def vuelist(self):
        with open (data_path+'\settings\settings.json',"r+") as f :
            settings = json.load(f)
            settings['settings']['help_mode']="list"

            f.seek(0)
            f.write(json.dumps(settings))
            f.truncate()       

        self.master.destroy()
        help_2(self.corespondance)

class help_2(tk.Frame):
    def __init__(self, corespondance):
        self.corespondance = corespondance
        master = tk.Toplevel()

        master.title("MathClav - Aide")
        master.iconbitmap('favicon.ico')

        master.tk.call(sv_ttk.set_theme("dark"))

        settings = json.load(open(data_path+'\settings\settings.json'))
        if settings['settings']['theme'] == "light" :
            master.tk.call(sv_ttk.toggle_theme())
        tk.Frame.__init__(self, master)
        
        self.btn = tk.Frame(self)
        s = ttk.Style()
        s.configure('my.TButton', font=('Helvetica', 14, 'bold'))
        self.quitButton = ttk.Button(self.btn, text='Quitter', width="30", command=master.destroy, style='my.TButton')
        self.quitButton.grid(row=0, column=1, padx=10, pady=10)
        self.helpButton = ttk.Button(self.btn, text='Vue Clavier', width="30", command=self.vueclavier, style='my.TButton')
        self.helpButton.grid(row=0, column=0, padx=10, pady=10)
        self.btn.pack()
        
        container = ttk.Frame(self)
        canvas = tk.Canvas(container)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        
        canvas.configure(yscrollcommand=scrollbar.set, width=700, height=400, selectborderwidth = 0, highlightthickness = 0)
        
        def OnMouseWheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
            return "break" 
        canvas.bind("<MouseWheel>", OnMouseWheel)
        container.bind("<MouseWheel>", OnMouseWheel)
        self.bind("<MouseWheel>", OnMouseWheel)
        
        ttk.Label(scrollable_frame, text=("          "+"²" + " -> "), font=('Helvetica', 14, 'bold')).grid(row=0, column=0, padx=10, pady=10)
        
        self.fig_= plt.Figure(figsize=(4, 0.5), dpi=100)
        self.wx = self.fig_.add_subplot(111)
        if sv_ttk.get_theme()=="dark" :
            self.fig_.patch.set_facecolor(g.bgMath)
        else :
            self.fig_.patch.set_facecolor(g.bgMath_white)
        self.wx.get_xaxis().set_visible(False)
        self.wx.get_yaxis().set_visible(False)
        self.wx.patch.set_visible(False)
        self.wx.axis('off')
        self.canvas_ = FigureCanvasTkAgg( self.fig_, master=scrollable_frame)
        self.canvas_.get_tk_widget()
        tmptext = ' Mode\:\:Math'
        if sv_ttk.get_theme()=="dark" :
            self.wx.text(-0.1, 0.2, r"$"+tmptext.replace(r"\text",r"\mathrm").replace('░', 'x')+"$", fontsize =   14, color=g.red)
        else :
            self.wx.text(-0.1, 0.2, r"$"+tmptext.replace(r"\text",r"\mathrm").replace('░', 'x')+"$", fontsize =   14, color=g.red_dark)
        
        self.canvas_.get_tk_widget().bind("<MouseWheel>", OnMouseWheel)
        self.canvas_.get_tk_widget().grid(row=0, column=1)
        self.canvas_.draw()
        
        self.fig_= plt.Figure(figsize=(2, 0.5), dpi=100)
        self.wx = self.fig_.add_subplot(111)
        if sv_ttk.get_theme()=="dark" :
            self.fig_.patch.set_facecolor(g.bgMath)
        else :
            self.fig_.patch.set_facecolor(g.bgMath_white)
        self.wx.get_xaxis().set_visible(False)
        self.wx.get_yaxis().set_visible(False)
        self.wx.patch.set_visible(False)
        self.wx.axis('off')
        self.canvas_ = FigureCanvasTkAgg( self.fig_, master=scrollable_frame)
        self.canvas_.get_tk_widget()
        tmptext = "\:\:"
        if sv_ttk.get_theme()=="dark" :
            self.wx.text(-0.1, 0.2, r"$"+tmptext.replace(r"\text",r"\mathrm").replace('░', 'x')+"$", fontsize =   14, color=g.whith)
        else :
            self.wx.text(-0.1, 0.2, r"$"+tmptext.replace(r"\text",r"\mathrm").replace('░', 'x')+"$", fontsize =   14, color='black')
        
        self.canvas_.get_tk_widget().bind("<MouseWheel>", OnMouseWheel)
        self.canvas_.get_tk_widget().grid(row=0, column=2)
        self.canvas_.draw()
        
        ttk.Label(scrollable_frame, text=("       "+"CTRL" + " -> "), font=('Helvetica', 14, 'bold')).grid(row=1, column=0, padx=10, pady=10)
    
        self.fig_= plt.Figure(figsize=(4, 0.5), dpi=100)
        self.wx = self.fig_.add_subplot(111)
        if sv_ttk.get_theme()=="dark" :
            self.fig_.patch.set_facecolor(g.bgMath)
        else :
            self.fig_.patch.set_facecolor(g.bgMath_white)
        self.wx.get_xaxis().set_visible(False)
        self.wx.get_yaxis().set_visible(False)
        self.wx.patch.set_visible(False)
        self.wx.axis('off')
        self.canvas_ = FigureCanvasTkAgg( self.fig_, master=scrollable_frame)
        self.canvas_.get_tk_widget()
        tmptext = '\:\:'
        if sv_ttk.get_theme()=="dark" :
            self.wx.text(-0.1, 0.2, r"$"+tmptext.replace(r"\text",r"\mathrm").replace('░', 'x')+"$", fontsize =   14, color=g.whith)
        else :
            self.wx.text(-0.1, 0.2, r"$"+tmptext.replace(r"\text",r"\mathrm").replace('░', 'x')+"$", fontsize =   14, color='black')
        
        self.canvas_.get_tk_widget().bind("<MouseWheel>", OnMouseWheel)
        self.canvas_.get_tk_widget().grid(row=1, column=1)
        self.canvas_.draw()
        
        self.fig_= plt.Figure(figsize=(2, 0.5), dpi=100)
        self.wx = self.fig_.add_subplot(111)
        if sv_ttk.get_theme()=="dark" :
            self.fig_.patch.set_facecolor(g.bgMath)
        else :
            self.fig_.patch.set_facecolor(g.bgMath_white)
        self.wx.get_xaxis().set_visible(False)
        self.wx.get_yaxis().set_visible(False)
        self.wx.patch.set_visible(False)
        self.wx.axis('off')
        self.canvas_ = FigureCanvasTkAgg( self.fig_, master=scrollable_frame)
        self.canvas_.get_tk_widget()
        tmptext = "Mode\:\:Grec"
        if sv_ttk.get_theme()=="dark" :
            self.wx.text(-0.1, 0.2, r"$"+tmptext.replace(r"\text",r"\mathrm").replace('░', 'x')+"$", fontsize =   14, color=g.green)
        else :
            self.wx.text(-0.1, 0.2, r"$"+tmptext.replace(r"\text",r"\mathrm").replace('░', 'x')+"$", fontsize =   14, color=g.green_dark)
        
        self.canvas_.get_tk_widget().bind("<MouseWheel>", OnMouseWheel)
        self.canvas_.get_tk_widget().grid(row=1, column=2)
        self.canvas_.draw()
        
        
        
        for i in range(len(self.corespondance[0])):
            #ttk.Label(scrollable_frame, text="Sample scrolling label").pack()
            ttk.Label(scrollable_frame, text=("          "+corespondance[3][i] + " -> "), font=('Helvetica', 14, 'bold')).grid(row=i+2, column=0, padx=10, pady=10)
            
            self.fig_= plt.Figure(figsize=(4, 0.5), dpi=100)
            self.wx = self.fig_.add_subplot(111)
            if sv_ttk.get_theme()=="dark" :
                self.fig_.patch.set_facecolor(g.bgMath)
            else :
                self.fig_.patch.set_facecolor(g.bgMath_white)
            self.wx.get_xaxis().set_visible(False)
            self.wx.get_yaxis().set_visible(False)
            self.wx.patch.set_visible(False)
            self.wx.axis('off')
            self.canvas_ = FigureCanvasTkAgg( self.fig_, master=scrollable_frame)
            self.canvas_.get_tk_widget()
            tmptext = ''
            for x in corespondance[2][i]:
                tmptext += x.__str__()
                tmptext += '\:\:'
            if sv_ttk.get_theme()=="dark" :
                self.wx.text(-0.1, 0.2, r"$"+tmptext.replace(r"\text",r"\mathrm").replace('░', 'x')+"$", fontsize =   14, color=g.whith)
            else :
                self.wx.text(-0.1, 0.2, r"$"+tmptext.replace(r"\text",r"\mathrm").replace('░', 'x')+"$", fontsize =   14, color='black')
            
            self.canvas_.get_tk_widget().bind("<MouseWheel>", OnMouseWheel)
            self.canvas_.get_tk_widget().grid(row=i+2, column=1)
            self.canvas_.draw()
        
            self.fig_= plt.Figure(figsize=(2, 0.5), dpi=100)
            self.wx = self.fig_.add_subplot(111)
            if sv_ttk.get_theme()=="dark" :
                self.fig_.patch.set_facecolor(g.bgMath)
            else :
                self.fig_.patch.set_facecolor(g.bgMath_white)
            self.wx.get_xaxis().set_visible(False)
            self.wx.get_yaxis().set_visible(False)
            self.wx.patch.set_visible(False)
            self.wx.axis('off')
            self.canvas_ = FigureCanvasTkAgg( self.fig_, master=scrollable_frame)
            self.canvas_.get_tk_widget()
            tmptext = corespondance[1][i].__str__() + "  -  " + corespondance[0][i].__str__()
            if sv_ttk.get_theme()=="dark" :
                self.wx.text(-0.1, 0.2, r"$"+tmptext.replace(r"\text",r"\mathrm").replace('░', 'x')+"$", fontsize =   14, color=g.whith)
            else :
                self.wx.text(-0.1, 0.2, r"$"+tmptext.replace(r"\text",r"\mathrm").replace('░', 'x')+"$", fontsize =   14, color='black')
            
            self.canvas_.get_tk_widget().bind("<MouseWheel>", OnMouseWheel)
            self.canvas_.get_tk_widget().grid(row=i+2, column=2)
            self.canvas_.draw()
            
        container.pack(fill="both", expand=True)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        #for i in range(0, 26):
        #    ttk.Label(self.main, text=corespondance[3][i], font=('Helvetica', 14, 'bold')).grid(row=i, column=0, padx=10, pady=10)
        
        self.pack()

        self.mainloop()
    
    def vueclavier(self):
        with open (data_path+'\settings\settings.json',"r+") as f :
            settings = json.load(f)
            settings['settings']['help_mode']="keyboard"

            f.seek(0)
            f.write(json.dumps(settings))
            f.truncate()       

        self.master.destroy()
        help(self.corespondance)
        
if __name__ == '__main__':
    #c = credit()
    v = help()