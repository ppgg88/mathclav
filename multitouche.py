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


from doctest import master
from logging import root
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pyglet
import sv_ttk
import time
import os
import json
import globals as g

#constantes couleurs:

g.initialize()

pyglet.font.add_file("Lato-Regular.ttf")
data_path = g.data_path

millis = lambda: int(round(time.time() * 1000))


class multi(tk.Frame):
    def __init__(self,all, root, latex, l):
        self.root = root
        self.master = tk.Tk()
        self.fig_ =[]
        self.wx_=[]
        self.canvas_ = []
        self.master.tk.call(sv_ttk.set_theme("dark"))
        settings = json.load(open(data_path+'\settings\settings.json'))
        if settings['settings']['theme'] == "light" :
            self.master.tk.call(sv_ttk.toggle_theme())
        tk.Frame.__init__(self, self.master)
        self.master.bind("<KeyPress>", all.action)
        for i in range(0, len(latex)):
            tmptext = latex[i].__str__().replace(r"æ", "a")
            if l == i:
                self.fig_.append(plt.Figure(figsize=(4, 0.5), dpi=100))
                self.wx_.append(self.fig_[len(self.fig_)-1].add_subplot(111))
                if sv_ttk.get_theme()=="dark" :
                    self.fig_[len(self.fig_)-1].patch.set_facecolor(g.bgMath_white)
                else :
                    self.fig_[len(self.fig_)-1].patch.set_facecolor(g.bgMath)
                self.wx_[len(self.wx_)-1].get_xaxis().set_visible(False)
                self.wx_[len(self.wx_)-1].get_yaxis().set_visible(False)
                self.wx_[len(self.wx_)-1].patch.set_visible(False)
                self.wx_[len(self.wx_)-1].axis('off')
                self.canvas_.append(FigureCanvasTkAgg( self.fig_[len(self.fig_)-1], master=self))
                self.canvas_[len(self.canvas_)-1].get_tk_widget()
                if sv_ttk.get_theme()=="dark" :
                    self.wx_[len(self.wx_)-1].text(-0.1, 0.6, r"$"+tmptext.replace(r"\text",r"\mathrm")+"$", fontsize = 10, color='black')
                else :
                    self.wx_[len(self.wx_)-1].text(-0.1, 0.6, r"$"+tmptext.replace(r"\text",r"\mathrm")+"$", fontsize = 10, color=g.whith)
                self.canvas_[len(self.canvas_)-1].get_tk_widget().grid(row=i, column=1)
                self.canvas_[len(self.canvas_)-1].draw()
            else:
                self.fig_.append(plt.Figure(figsize=(4, 0.5), dpi=100))
                self.wx_.append(self.fig_[len(self.fig_)-1].add_subplot(111))
                if sv_ttk.get_theme()=="dark" :
                    self.fig_[len(self.fig_)-1].patch.set_facecolor(g.bgMath)
                else :
                    self.fig_[len(self.fig_)-1].patch.set_facecolor(g.bgMath_white)
                self.wx_[len(self.wx_)-1].get_xaxis().set_visible(False)
                self.wx_[len(self.wx_)-1].get_yaxis().set_visible(False)
                self.wx_[len(self.wx_)-1].patch.set_visible(False)
                self.wx_[len(self.wx_)-1].axis('off')
                self.canvas_.append(FigureCanvasTkAgg( self.fig_[len(self.fig_)-1], master=self))
                self.canvas_[len(self.canvas_)-1].get_tk_widget()
                if sv_ttk.get_theme()=="dark" :
                    self.wx_[len(self.wx_)-1].text(-0.1, 0.6, r"$"+tmptext.replace(r"\text",r"\mathrm")+"$", fontsize = 10, color=g.whith)
                else :
                    self.wx_[len(self.wx_)-1].text(-0.1, 0.6, r"$"+tmptext.replace(r"\text",r"\mathrm")+"$", fontsize = 10, color='black')
                self.canvas_[len(self.canvas_)-1].get_tk_widget().grid(row=i, column=1)
                self.canvas_[len(self.canvas_)-1].draw()
        self.pack()
        #self.master.transient(root)
        self.master.overrideredirect(1)
        self.master.geometry("-0-40")
        self.master.attributes("-toolwindow", 1)
        self.time = millis()
        root.after(1500, lambda: self.supr())
    
    def modifie(self, l, latex):
        tmptext = latex[l].__str__().replace(r"æ", "a")
        #actif
        if sv_ttk.get_theme()=="dark" :
            self.fig_[l].patch.set_facecolor(g.bgMath_white)
            self.wx_[l].text(-0.1, 0.6, r"$"+tmptext.replace(r"\text",r"\mathrm")+"$", fontsize = 10, color='black')
        else :
            self.fig_[l].patch.set_facecolor(g.bgMath)
            self.wx_[l].text(-0.1, 0.6, r"$"+tmptext.replace(r"\text",r"\mathrm")+"$", fontsize = 10, color=g.whith)
        #precedent
        j=l-1
        if j==-1:
            j=len(self.fig_)-1
        tmptext = latex[j].__str__().replace(r"æ", "a")
        if sv_ttk.get_theme()=="dark" :
            self.fig_[j].patch.set_facecolor(g.bgMath)
            self.wx_[j].text(-0.1, 0.6, r"$"+tmptext.replace(r"\text",r"\mathrm")+"$", fontsize = 10, color=g.whith)
        else :
            self.fig_[j].patch.set_facecolor(g.bgMath_white)
            self.wx_[j].text(-0.1, 0.6, r"$"+tmptext.replace(r"\text",r"\mathrm")+"$", fontsize =  10, color='black')
        
        self.canvas_[l].draw()
        self.canvas_[j].draw()
        self.time = millis()
        self.root.after(1500, lambda: self.supr())

    def supr(self):
        if millis()-self.time >= 1500:
            try:
                self.destroy()
                self.master.destroy()
            except:
                pass
        
if __name__=='__main__':
    root = tk.Tk()
    a = multi(root, ["1","2","3","4","5","6","7","8","9","10"], 0)
    root.mainloop()

