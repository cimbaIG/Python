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

n = 250
eta = np.linspace(0, 10, n)

def free_convection(y, eta):
    return [y[1], y[2], -3*y[0]*y[2] + 2*y[1]*y[1] - y[3],
            y[4], -3*Pr*y[0]*y[4]]

def derivation(a):
    x0 = [0, 0 , a[0], 1, a[1]]
    f = scipy.integrate.odeint(free_convection, x0, eta)
    return f[np.size(eta)-1,1], f[np.size(eta)-1,3]*f[np.size(eta)-1,3] + f[np.size(eta)-1,4]*f[np.size(eta)-1,4]

######################################################################
Pr = 0.01

a = scipy.optimize.fsolve(derivation,[0.9862, -0.0812],xtol=1e-06);

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

######################################################################
Pr = 0.1

a = scipy.optimize.fsolve(derivation,[0.856, -0.234],xtol=1e-06);

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

######################################################################
Pr = 0.5

a = scipy.optimize.fsolve(derivation,[0.713, -0.442],xtol=1e-06);

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
Pr = 0.733

a = scipy.optimize.fsolve(derivation,[0.6741, -0.5080],xtol=1e-06);

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

######################################################################
Pr = 1.0

a = scipy.optimize.fsolve(derivation,[0.6421, -0.5671],xtol=1e-06);

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

######################################################################
Pr = 2.0

a = scipy.optimize.fsolve(derivation,[0.5713, -0.7165],xtol=1e-06);

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

######################################################################
Pr = 10.0

a = scipy.optimize.fsolve(derivation,[0.4192, -1.1694],xtol=1e-06);

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

######################################################################
Pr = 100.0

a = scipy.optimize.fsolve(derivation,[0.2517, -2.191],xtol=1e-06);

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

######################################################################
Pr = 1000.0

a = scipy.optimize.fsolve(derivation,[0.1450, -3.966],xtol=1e-06);

print "a = ", a

initial_condition = [0, 0, a[0], 1, a[1]]
y = scipy.integrate.odeint(free_convection, initial_condition, eta)

print "y = ", y

fig1 = plt.figure(1)
ax = plt.axes()
plt.plot(eta, y[:,1], color='k', linewidth=2, linestyle='-' , label=r'$f(\eta)$')
#plt.xlabel(r'$\eta$')
#plt.ylabel(r'$\frac{dF)}{deta}$')
startY, endY = (0, 0.601)
startX, endX = (0, 10.01)
plt.xlim(0, 10)
plt.ylim(0, 0.6)
ax.yaxis.set_ticks(np.arange(startY,endY,0.1))
ax.xaxis.set_ticks(np.arange(startX,endX,1))
#legend = plt.legend(numpoints=1, loc=2)
#frame = legend.get_frame()
plt.grid(False)
#ax.grid(color='k', linestyle=':', linewidth=0.2)
#Get current figure
fig1 = plt.gcf()

# Hide the right and top spines
gca().spines['right'].set_visible(False)
gca().spines['top'].set_visible(False)
 
# Only show ticks on the left and bottom spines
gca().yaxis.set_ticks_position('left')
gca().xaxis.set_ticks_position('bottom')

# Set tick marks outside
gca().get_yaxis().set_tick_params(direction='out')
gca().get_xaxis().set_tick_params(direction='out')

#Set figure size
fig1.set_size_inches(10, 8)
#When saving, specify the DPI
plt.savefig('free_convection_velocity.png', dpi = 300, bbox_inches='tight')
plt.savefig('free_convection_velocity.pdf', dpi = 300, bbox_inches='tight')

fig2 = plt.figure(2)
ax = plt.axes()
plt.plot(eta, y[:,3], color='k',linewidth=2, linestyle='-' , label=r'$\frac{df(\eta)}{d\eta}$')
#plt.xlabel(r'$u"x3b7"$')
#plt.ylabel(r'$G(\eta)$')
startY, endY = (0, 1.01)
startX, endX = (0, 10.01)
plt.xlim(0, 10)
plt.ylim(0, 1)
ax.yaxis.set_ticks(np.arange(startY,endY,0.1))
ax.xaxis.set_ticks(np.arange(startX,endX,1))
#legend = plt.legend(numpoints=1, loc=2)
#frame = legend.get_frame()
plt.grid(False)
#ax.grid(color='k', linestyle=':', linewidth=0.2)
#Get current figure
fig2 = plt.gcf()

# Hide the right and top spines
gca().spines['right'].set_visible(False)
gca().spines['top'].set_visible(False)
 
# Only show ticks on the left and bottom spines
gca().yaxis.set_ticks_position('left')
gca().xaxis.set_ticks_position('bottom')

# Set tick marks outside
gca().get_yaxis().set_tick_params(direction='out')
gca().get_xaxis().set_tick_params(direction='out')

#Set figure size
fig2.set_size_inches(10, 8)
#When saving, specify the DPI
plt.savefig('free_convection_temperature.png', dpi = 300, bbox_inches='tight')
plt.savefig('free_convection_temperature.pdf', dpi = 300, bbox_inches='tight')

plt.show()
