import sympy
import math
from sympy.abc import x, y
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#Change font type and font size in axis labels
matplotlib.rcParams.update({'legend.markerscale': 1.5, 'legend.handlelength': 1, 'legend.frameon': 1, 'legend.handletextpad': 1 , 'font.size': 18,'font.family':'Times New Roman'})

matplotlib.rcParams['text.usetex'] = True
#matplotlib.rcParams['text.latex.unicode'] = True
#matplotlib.rcParams['mathtext.fontset'] = 'stix'
#matplotlib.rcParams['font.family'] = 'STIXGeneral'

def plot_streamlines(ax, u, v, xlim=(-2, 6), ylim=(-2, 6)):
    x0, x1 = xlim
    y0, y1 = ylim
    x = np.arange(0, 10)
    y = np.arange(0, 10)
    X, Y = np.meshgrid(x, y)
    u = np.ones((10, 10))
    v = np.ones((10, 10))
    ax.streamplot(X, Y, u, v, color='black', density=2 , arrowsize=1, arrowstyle='->', broken_streamlines=False)

def format_axes(ax):
    ax.set_aspect('equal')
    ax.figure.subplots_adjust(bottom=0, top=1, left=0, right=1)
    ax.xaxis.set_ticks([])
    ax.yaxis.set_ticks([])
    for spine in ax.spines.itervalues():
        spine.set_visible(False)

xlim = ylim = (-2, 2)
fig, ax = plt.subplots(figsize=(10, 10))
plt.grid(True)
plt.xlabel(r'$x_1$', fontname="Times New Roman", fontsize=24)
plt.ylabel(r'$x_2$', fontname="Times New Roman", fontsize=24)
plt.title(r'Paralelno strujanje pod kutem $\alpha = 45^{\circ}$')
plot_streamlines(ax, (-4.99, 4.99), (-4.99, 4.97))

tz1 = plt.Circle((0,0), radius=0.03, facecolor='black', edgecolor='black')
ax.add_patch(tz1)

#Get current figure
figure = plt.gcf()
#Set figure size
#figure.set_size_inches(5, 5)
#When saving, specify the DPI
plt.savefig('zad_2_1_streamlines.pdf', bbox_inches='tight')
#Show figure
plt.show()

format_axes(ax)    
