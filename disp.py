import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
import tkinter as tk

master = tk.Tk()

mpl.rcParams['font.size'] = 20
mpl.rcParams['text.usetex'] = False
mpl.rcParams['text.latex.preamble'] = r'\usepackage{{amsmath}}'

fig = plt.figure()
a = fig.add_subplot(111)
a.get_xaxis().set_visible(False)
a.get_yaxis().set_visible(False)
a.patch.set_visible(False)
a.axis('off')

canvas =  FigureCanvasTkAgg(fig, master)

a.clear()
a.text(0.6, 0.6, r'$\genfrac{a}{b}{c}{d}{e}{f}$', fontsize = 11)

canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

tk.mainloop()