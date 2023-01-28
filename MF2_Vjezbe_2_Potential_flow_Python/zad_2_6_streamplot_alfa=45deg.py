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
#matplotlib.rcParams['text.latex.unicode'] = True

def potential_function():
    m = 2*math.pi
    alpha = math.pi/4
    r = sympy.sqrt((x)**2 + (y)**2)
    theta = sympy.atan2(y,x)
    return (-m/2*math.pi)*(sympy.cos(theta - alpha)/r)

def velocity_field(fi):
    u = sympy.lambdify((x, y), fi.diff(x), 'numpy')
    v = sympy.lambdify((x, y), fi.diff(y), 'numpy')
    return u, v

def plot_streamlines(ax, u, v, xlim=(-5, 5), ylim=(-5, 5)):
    x0, x1 = xlim
    y0, y1 = ylim
    Y, X =  np.ogrid[y0:y1:100j, x0:x1:100j]
    ax.streamplot(X, Y, u(X, Y), v(X, Y), color='black', density=2 , arrowsize=1, arrowstyle='->', broken_streamlines=True)

def format_axes(ax):
    ax.set_aspect('equal')
    ax.figure.subplots_adjust(bottom=0, top=1, left=0, right=1)
    ax.xaxis.set_ticks([])
    ax.yaxis.set_ticks([])
    for spine in ax.spines.itervalues():
        spine.set_visible(False)

fi = potential_function()
u, v = velocity_field(fi)

xlim = ylim = (-5, 5)
fig, ax = plt.subplots(figsize=(10, 10))
plt.grid(True)
plt.xlabel(r'$x_1$', fontname="Times New Roman", fontsize=24)
plt.ylabel(r'$x_2$', fontname="Times New Roman", fontsize=24)
plt.title(r'Dipol u (0,0), $\alpha = \pi / 4$ rad')
plot_streamlines(ax, u, v, (-5.97, 5.97), (-5.97, 5.97))

tz1 = plt.Circle((0,0), radius=0.03, facecolor='black', edgecolor='black')
ax.add_patch(tz1)

#Get current figure
figure = plt.gcf()
#Set figure size
#figure.set_size_inches(5, 5)
#When saving, specify the DPI
plt.savefig('zad_2_6_streamlines_alfa=45deg.pdf', bbox_inches='tight')
#Show figure
plt.show()

format_axes(ax)    
