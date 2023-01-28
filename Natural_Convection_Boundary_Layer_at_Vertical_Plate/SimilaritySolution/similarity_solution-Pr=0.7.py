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
    return f[np.size(eta)-1,1], f[np.size(eta)-1,3]

Pr = 0.7

a = scipy.optimize.fsolve(derivation,[0.676, -0.5046],xtol=1e-06);

print "a = ", a

initial_condition = [0, 0, a[0], 1, a[1]]
y = scipy.integrate.odeint(free_convection, initial_condition, eta)

print "y = ", y

#fig1 = plt.figure(1)
#ax = plt.axes()
#plt.plot(eta, y[:,1], color='k', linewidth=2, linestyle='-' , label=r'$f(\eta)$')
#fig2 = plt.figure(2)
#ax = plt.axes()
#plt.plot(eta, y[:,3], color='k',linewidth=2, linestyle='-' , label=r'$\frac{df(\eta)}{d\eta}$')

result = np.column_stack((eta,y))

np.savetxt('similarity_solution_Pr=0.7.txt', result, delimiter="	", header="		eta			F(eta)				F'(eta)				F''(eta)			G(eta)				G'(eta)")

Tp = 307
Tbesk = 300
g = 9.81
beta = 0.003
nu = pow(10,-5)
L = 0.3
lambd = 0.028

x = np.linspace(0.01, L, 100)
Grx = np.zeros(np.size(x))
Rax = np.zeros(np.size(x))
alphax = np.zeros(np.size(x))
Nux = np.zeros(np.size(x))
NusseltEDE = np.zeros(np.size(x))

print "Grx:"
for i in range(0,np.size(x)):
    Grx[i] = (g * beta * (Tp - Tbesk) * pow(x[i],3)) / pow(nu,2)
    print Grx[i]

print "Rax:"
for i in range(0,np.size(x)):
    Rax[i] = Grx[i] * Pr
    print Rax[i]

print "alphax:"
for i in range(0,np.size(x)):
    alphax[i] = - lambd * result[0,5] * (1/x[i]) * pow((Grx[i]/4),0.25)
    print alphax[i]

print "Nux:"
for i in range(0,np.size(x)):
    Nux[i] = (alphax[i] * x[i]) / lambd
    print Nux[i]

print "NusseltEDE:"
for i in range(0,np.size(x)):
    NusseltEDE[i] = 0.75 * pow(( 2*Pr / ( 5*( 1 + 2 * pow(Pr,0.5) + 2*Pr ) ) ), 0.25) * pow(Rax[i],0.25)
    print NusseltEDE[i]

gradTy_SIMPLE = np.loadtxt('gradTy_SIMPLE.dat')
gradTMeany_PISO = np.loadtxt('gradTMeany_PISO.dat')

gradTy = np.zeros(np.size(gradTy_SIMPLE)/2)
gradTMeany = np.zeros(np.size(gradTMeany_PISO)/2)
x_SIMPLE = np.zeros(np.size(gradTy_SIMPLE)/2)
x_PISO = np.zeros(np.size(gradTMeany_PISO)/2)

for i in range(0,np.size(gradTy)):
    gradTy[i] = gradTy_SIMPLE[i,0]

for i in range(0,np.size(gradTy)):
    x_SIMPLE[i] = gradTy_SIMPLE[i,1]

for i in range(0,np.size(gradTMeany)):
    gradTMeany[i] = gradTMeany_PISO[i,0]

for i in range(0,np.size(gradTMeany)):
    x_PISO[i] = gradTMeany_PISO[i,1]

alphaxSIMPLE = np.zeros(np.size(gradTy_SIMPLE)/2)
alphaxPISO = np.zeros(np.size(gradTMeany_PISO)/2)
NusseltSIMPLE = np.zeros(np.size(gradTy_SIMPLE)/2)
NusseltPISO = np.zeros(np.size(gradTMeany_PISO)/2)
GrxSIMPLE = np.zeros(np.size(gradTy_SIMPLE)/2)
GrxPISO = np.zeros(np.size(gradTMeany_PISO)/2)
RaxSIMPLE = np.zeros(np.size(gradTy_SIMPLE)/2)
RaxPISO = np.zeros(np.size(gradTMeany_PISO)/2)

for i in range(0,np.size(x_SIMPLE)):
    alphaxSIMPLE[i] = - (lambd/(Tp-Tbesk))*gradTy[i]
    print alphaxSIMPLE[i]

for i in range(0,np.size(x_PISO)):
    alphaxPISO[i] = - (lambd/(Tp-Tbesk))*gradTMeany[i]
    print alphaxPISO[i]

for i in range(0,np.size(x_SIMPLE)):
    NusseltSIMPLE[i] = (alphaxSIMPLE[i] * x_SIMPLE[i]) / lambd
    print NusseltSIMPLE[i]

for i in range(0,np.size(x_PISO)):
    NusseltPISO[i] = (alphaxPISO[i] * x_PISO[i]) / lambd
    print NusseltPISO[i]

for i in range(0,np.size(x_SIMPLE)):
    GrxSIMPLE[i] = (g * beta * (Tp - Tbesk) * pow(x_SIMPLE[i],3)) / pow(nu,2)

for i in range(0,np.size(x_PISO)):
    GrxPISO[i] = (g * beta * (Tp - Tbesk) * pow(x_PISO[i],3)) / pow(nu,2)

for i in range(0,np.size(x_SIMPLE)):
    RaxSIMPLE[i] = GrxSIMPLE[i] * Pr 

for i in range(0,np.size(x_PISO)):
    RaxPISO[i] = GrxPISO[i] * Pr

fig = plt.figure(1)
ax = plt.axes()

plt.semilogx(Rax, Nux, 'o', markeredgecolor='k', markerfacecolor='none', markeredgewidth='2', markersize=10, markevery=2, label='Similarity solution')
plt.semilogx(RaxSIMPLE, NusseltSIMPLE, '+', markeredgecolor='k', markerfacecolor='none', markeredgewidth='2', markersize=10, markevery=2, label='Steady state OpenFoam')
plt.semilogx(RaxPISO, NusseltPISO, 'x', markeredgecolor='k', markerfacecolor='none', markeredgewidth='2', markersize=10, markevery=2, label='Transient OpenFoam')
plt.semilogx(Rax, NusseltEDE, linewidth='2', color='k', label='Ede (1964)')

plt.xlabel(r'$Ra_{x}$')
plt.ylabel(r'$Nu_{x}$')
plt.xlim(10**3, 10**8)
plt.ylim(0, 32)
starty, endy = (0, 32.01)
startx, endx = (10**3, 10**8)
ax.yaxis.set_ticks(np.arange(starty,endy,4))
#ax.xaxis.set_ticks(np.arange(startx,endx,20000000))
plt.grid(False)
plt.legend(numpoints=1, loc=2)

# Hide the right and top spines
gca().spines['right'].set_visible(False)
gca().spines['top'].set_visible(False)
 
# Only show ticks on the left and bottom spines
gca().yaxis.set_ticks_position('left')
gca().xaxis.set_ticks_position('bottom')

# Set tick marks outside
gca().get_yaxis().set_tick_params(direction='out')
gca().get_xaxis().set_tick_params(direction='out')

#Get current figure
figure = plt.gcf()
#Set figure size
figure.set_size_inches(10, 10)
#When saving, specify the DPI
plt.savefig('Nusselt_number.pdf', dpi = 300, bbox_inches='tight')
plt.show()