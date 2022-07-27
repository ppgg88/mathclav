#

import tkinter as tk
from tkinter import ttk

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math as mt
#import latex as lt

def graph(Mathobj, xmin=0, xmax=10, xstep=0.1, ymin=0, ymax=15, ystep=0.1):
    func = Mathobj.graphStr().replace('x', 'x_')
    x = []
    y = []
    for i in range(xmin, int(xmax/xstep)):
        x.append(i*xstep)
        x_ = i*xstep
        for t in range(0, len(func)-2):
            if func[t].isdigit() and func[t+1].isalpha():
                func = func[:t+1]+ "*" + func[t+1:]
            
        try:
            y.append(eval(func))
        except:
            print("Ereur dans la fonction : ", func)
            return(False)
    plt.plot(x, y)
    plt.axis([xmin, xmax, ymin, ymax])
    plt.show()