# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import scipy
from scipy import optimize
import scipy.integrate
import pylab
import numpy as np
import matplotlib
import math
import matplotlib.pyplot as plt
from matplotlib.pyplot import gca

#Change font type and font size in axis labels
matplotlib.rcParams.update({'legend.markerscale': 1.5, 'legend.handlelength': 1, 'legend.frameon': 0, 'legend.handletextpad': 1 , 'font.size': 26,'font.family':'Arial', 'font.weight': 'bold', 'font.style': 'italic'})

params = {'axes.labelsize': 26,
         'axes.labelweight': 'bold',
         'axes.titlesize': 26,
         'xtick.labelsize': 26,
         'ytick.labelsize': 26}
matplotlib.pylab.rcParams.update(params)

#matplotlib.rcParams['text.usetex'] = True
#matplotlib.rcParams['text.latex.unicode'] = True
matplotlib.rcParams['mathtext.fontset'] = 'custom'
matplotlib.rcParams['mathtext.it'] = 'stixsans:italic'
matplotlib.rcParams['mathtext.bf'] = 'stixsans:italic:bold'

n = 251
eta = np.linspace(0, 10, n)

def free_convection(y, eta):
    return [y[1], y[2], -3*y[0]*y[2] + 2*y[1]*y[1] - y[3],
            y[4], -3*Pr*y[0]*y[4]]

def derivation(a):
    x0 = [0, 0 , a[0], 1, a[1]]
    f = scipy.integrate.odeint(free_convection, x0, eta)
    return f[np.size(eta)-1,1], f[np.size(eta)-1,3]*f[np.size(eta)-1,3] + f[np.size(eta)-1,4]*f[np.size(eta)-1,4]

######################################################################
Pr = 0.72

a = scipy.optimize.fsolve(derivation,[0.676, -0.5046],xtol=1e-06);

print "a = ", a

initial_condition = [0, 0, a[0], 1, a[1]]
y = scipy.integrate.odeint(free_convection, initial_condition, eta)

print "y = ", y

fig1 = plt.figure(1)
ax = plt.axes()
plt.plot(eta, y[:,1], color='k', linewidth=2, linestyle='-' , label=r'$f(\eta)$')
fig2 = plt.figure(2)
ax = plt.axes()
plt.plot(eta, y[:,3], color='k',linewidth=2, linestyle='-' , label=r'$\frac{df(\eta)}{d\eta}$')

result = np.column_stack((eta,y))

np.savetxt('similarity_solution_Pr=0.72.txt', result, delimiter="	", header="		eta			F(eta)				F'(eta)				F''(eta)			G(eta)				G'(eta)")
######################################################################

