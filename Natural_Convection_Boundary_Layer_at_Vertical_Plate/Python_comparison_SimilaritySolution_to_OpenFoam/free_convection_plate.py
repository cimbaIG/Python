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

#####################################################################################################################################
############################################## Initial values for the problem #######################################################
#####################################################################################################################################

Lplate = 0.3
Pr = 0.7
g = 9.81
Tinf = 300
Tplate = 307
beta = 0.003
nu = math.pow(10,-5)
rho = 1.2
cp = 1005
k = 0.0257

#####################################################################################################################################
################################################# Laminar or turbulent flow? ########################################################
################## If Ra < 10^9, flow is laminar! Otherwise is turbulent and following procedure is not valid! ######################
#####################################################################################################################################

Gr = (g*beta*(Tplate-Tinf)*math.pow(Lplate,3)) / math.pow(nu,2) 
Ra = Gr * Pr 
print "Gr = ", Gr 
print "Ra = ", Ra

#####################################################################################################################################
################################################### Similarity solution #############################################################
#####################################################################################################################################

n = 100
eta = np.linspace(0, 10, n)

def free_convection(y, eta):
    return [y[1], y[2], -3*y[0]*y[2] + 2*y[1]*y[1] - y[3],
            y[4], -3*Pr*y[0]*y[4]]

def derivation(a):
    x0 = [0, 0 , a[0], 1, a[1]]
    f = scipy.integrate.odeint(free_convection, x0, eta)
    return f[np.size(eta)-1,1], f[np.size(eta)-1,3]

a = scipy.optimize.fsolve(derivation,[0.676, -0.5046],xtol=1e-06);

initial_condition = [0, 0, a[0], 1, a[1]]
y = scipy.integrate.odeint(free_convection, initial_condition, eta)

#####################################################################################################################################
###################################### Transform similarity data to dimensional values ##############################################
#####################################################################################################################################

# Get arrays that contain similarity values of Ux, T and gradT

velSimilarity = y[:,1]
tempSimilarity = y[:,3]
gradTempSimilarity = y[:,4]

# Arrays initialization

samplingPositions = np.array([0.07, 0.14, 0.21, 0.28])
Grx = np.zeros(samplingPositions.size)
Rax = np.zeros(samplingPositions.size)
etaDimensional07 = np.zeros(eta.size)
etaDimensional14 = np.zeros(eta.size)
etaDimensional21 = np.zeros(eta.size)
etaDimensional28 = np.zeros(eta.size)
velDimensional07 = np.zeros(velSimilarity.size)
velDimensional14 = np.zeros(velSimilarity.size)
velDimensional21 = np.zeros(velSimilarity.size)
velDimensional28 = np.zeros(velSimilarity.size)
tempDimensional07 = np.zeros(tempSimilarity.size)
tempDimensional14 = np.zeros(tempSimilarity.size)
tempDimensional21 = np.zeros(tempSimilarity.size)
tempDimensional28 = np.zeros(tempSimilarity.size)

# Get Gr and Ra values for the different x positions of the boundary layer

for i in range(0,samplingPositions.size):
    Grx[i] = (g*beta*(Tplate-Tinf))*(math.pow(samplingPositions[i],3)) / (nu**2)
    Rax[i] = Grx[i] * Pr

print "Grx = ", Grx, " Rax = ", Rax

# Get dimensional eta values from similarity eta values

for i in range(0, eta.size):
    etaDimensional07[i] = eta[i] / ( (1/samplingPositions[0]) * (math.pow(0.25 * Grx[0], 0.25)) )

for i in range(0, eta.size):
    etaDimensional14[i] = eta[i] / ( (1/samplingPositions[1]) * (math.pow(0.25 * Grx[1], 0.25)) )

for i in range(0, eta.size):
    etaDimensional21[i] = eta[i] / ( (1/samplingPositions[2]) * (math.pow(0.25 * Grx[2], 0.25)) )

for i in range(0, eta.size):
    etaDimensional28[i] = eta[i] / ( (1/samplingPositions[3]) * (math.pow(0.25 * Grx[3], 0.25)) )

# Get dimensional Ux values from similarity Ux values

for i in range(0, velSimilarity.size):
    velDimensional07[i] = velSimilarity[i] / ( (samplingPositions[0] * math.pow(Grx[0], -0.5)) / (2 * nu) )

for i in range(0, velSimilarity.size):
    velDimensional14[i] = velSimilarity[i] / ( (samplingPositions[1] * math.pow(Grx[1], -0.5)) / (2 * nu) )

for i in range(0, velSimilarity.size):
    velDimensional21[i] = velSimilarity[i] / ( (samplingPositions[2] * math.pow(Grx[2], -0.5)) / (2 * nu) )

for i in range(0, velSimilarity.size):
    velDimensional28[i] = velSimilarity[i] / ( (samplingPositions[3] * math.pow(Grx[3], -0.5)) / (2 * nu) )

# Get dimensional T values from similarity T values

for i in range(0, tempSimilarity.size):
    tempDimensional07[i] = tempSimilarity[i] * ( Tplate - Tinf ) + Tinf

for i in range(0, tempSimilarity.size):
    tempDimensional14[i] = tempSimilarity[i] * ( Tplate - Tinf ) + Tinf

for i in range(0, tempSimilarity.size):
    tempDimensional21[i] = tempSimilarity[i] * ( Tplate - Tinf ) + Tinf

for i in range(0, tempSimilarity.size):
    tempDimensional28[i] = tempSimilarity[i] * ( Tplate - Tinf ) + Tinf

#####################################################################################################################################
################################################## Load numerical results ###########################################################
#####################################################################################################################################

Ux1stOD_07= np.loadtxt('Ux1stOD_x=0.07.dat')
UxMean1stOD_07 = np.loadtxt('x=0.07_UMeanx1stOD.dat')

T1stOD_07 = np.loadtxt('T1stOD_x=0.07.dat')
TMean1stOD_07 = np.loadtxt('x=0.07_TMean1stOD.dat')

Ux1stOD_14= np.loadtxt('Ux1stOD_x=0.14.dat')
UxMean1stOD_14 = np.loadtxt('x=0.14_UMeanx1stOD.dat')

T1stOD_14 = np.loadtxt('T1stOD_x=0.14.dat')
TMean1stOD_14 = np.loadtxt('x=0.14_TMean1stOD.dat')

Ux1stOD_21= np.loadtxt('Ux1stOD_x=0.21.dat')
UxMean1stOD_21 = np.loadtxt('x=0.21_UMeanx1stOD.dat')

T1stOD_21 = np.loadtxt('T1stOD_x=0.21.dat')
TMean1stOD_21 = np.loadtxt('x=0.21_TMean1stOD.dat')

Ux1stOD_28= np.loadtxt('Ux1stOD_x=0.28.dat')
UxMean1stOD_28 = np.loadtxt('x=0.28_UMeanx1stOD.dat')

T1stOD_28 = np.loadtxt('T1stOD_x=0.28.dat')
TMean1stOD_28 = np.loadtxt('x=0.28_TMean1stOD.dat')

#####################################################################################################################################
####################################### Compare similarity values with numerical results ############################################
#####################################################################################################################################

###################### Comparison between similarity Ux and numerical 1stOD SIMPLE Ux - COARSE MESH #################################

fig = plt.figure(1)
ax = plt.axes()

plt.plot(etaDimensional07, velDimensional07, 'o', markeredgecolor='none', markerfacecolor='k', markersize=6, label='Similarity solution')
plt.plot(etaDimensional14, velDimensional14, 'o', markeredgecolor='none', markerfacecolor='k', markersize=6)
plt.plot(etaDimensional21, velDimensional21, 'o', markeredgecolor='none', markerfacecolor='k', markersize=6)
plt.plot(etaDimensional28, velDimensional28, 'o', markeredgecolor='none', markerfacecolor='k', markersize=6)
         
plt.plot(Ux1stOD_07[:,0], Ux1stOD_07[:,1], linewidth='2', color='k', label='OpenFoam')
plt.plot(Ux1stOD_14[:,0], Ux1stOD_14[:,1], linewidth='2', color='k')
plt.plot(Ux1stOD_21[:,0], Ux1stOD_21[:,1], linewidth='2', color='k')
plt.plot(Ux1stOD_28[:,0], Ux1stOD_28[:,1], linewidth='2', color='k')

plt.xlabel(r'$y$, m')
plt.ylabel(r'$u$, m/s')
plt.xlim(0, 0.035)
plt.ylim(0, 0.14)
starty, endy = (0, 0.1401)
startx, endx = (0, 0.03501)
ax.yaxis.set_ticks(np.arange(starty,endy,0.02))
ax.xaxis.set_ticks(np.arange(startx,endx,0.007))
plt.grid(False)
plt.legend(numpoints=1, loc=1)

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
plt.savefig('steadyUx1stOD_comparison_coarseMesh.pdf', dpi = 300, bbox_inches='tight')
plt.show()

################################# Comparison between similarity T and numerical 1stOD SIMPLE T -  COARSE MESH ######################################

fig = plt.figure(2)
ax = plt.axes()

plt.plot(etaDimensional07, tempDimensional07, 'o', markeredgecolor='none', markerfacecolor='k', markersize=6, label='Similarity solution')
plt.plot(etaDimensional14, tempDimensional14, 'o', markeredgecolor='none', markerfacecolor='k', markersize=6)
plt.plot(etaDimensional21, tempDimensional21, 'o', markeredgecolor='none', markerfacecolor='k', markersize=6)
plt.plot(etaDimensional28, tempDimensional28, 'o', markeredgecolor='none', markerfacecolor='k', markersize=6)

plt.plot(T1stOD_07[:,0], T1stOD_07[:,1], linewidth='2', color='k', label='OpenFoam')
plt.plot(T1stOD_14[:,0], T1stOD_14[:,1], linewidth='2', color='k')
plt.plot(T1stOD_21[:,0], T1stOD_21[:,1], linewidth='2', color='k')
plt.plot(T1stOD_28[:,0], T1stOD_28[:,1], linewidth='2', color='k')

plt.xlabel(r'$y$, m')
plt.ylabel(r'$T$, K')
plt.xlim(0, 0.035)
plt.ylim(300, 307)
starty, endy = (300, 307.01)
startx, endx = (0, 0.03501)
ax.yaxis.set_ticks(np.arange(starty,endy,1))
ax.xaxis.set_ticks(np.arange(startx,endx,0.007))
plt.grid(False)
plt.legend(numpoints=1, loc=1)

#Get current figure
figure = plt.gcf()

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
figure.set_size_inches(10, 10)
#When saving, specify the DPI
plt.savefig('steadyT1stOD_comparison_coarseMesh.pdf', dpi = 300, bbox_inches='tight')
plt.show()

plt.show()

#################################### Comparison between similarity Ux and numerical 1stOD PISO Ux - COARSE MESH ########################################

fig = plt.figure(3)
ax = plt.axes()

plt.plot(etaDimensional07, velDimensional07, 'o', markeredgecolor='none', markerfacecolor='k', markersize=6, label='Similarity solution')
plt.plot(etaDimensional14, velDimensional14, 'o', markeredgecolor='none', markerfacecolor='k', markersize=6)
plt.plot(etaDimensional21, velDimensional21, 'o', markeredgecolor='none', markerfacecolor='k', markersize=6)
plt.plot(etaDimensional28, velDimensional28, 'o', markeredgecolor='none', markerfacecolor='k', markersize=6)
         
plt.plot(UxMean1stOD_07[:,0], UxMean1stOD_07[:,1], linewidth='2', color='k', label='OpenFoam')
plt.plot(UxMean1stOD_14[:,0], UxMean1stOD_14[:,1], linewidth='2', color='k')
plt.plot(UxMean1stOD_21[:,0], UxMean1stOD_21[:,1], linewidth='2', color='k')
plt.plot(UxMean1stOD_28[:,0], UxMean1stOD_28[:,1], linewidth='2', color='k')

plt.xlabel(r'$y$, m')
plt.ylabel(r'$u$, m/s')
plt.xlim(0, 0.035)
plt.ylim(0, 0.14)
starty, endy = (0, 0.1401)
startx, endx = (0, 0.03501)
ax.yaxis.set_ticks(np.arange(starty,endy,0.02))
ax.xaxis.set_ticks(np.arange(startx,endx,0.007))
plt.grid(False)
plt.legend(numpoints=1, loc=1)

#Get current figure
figure = plt.gcf()

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
figure.set_size_inches(10, 10)
#When saving, specify the DPI
plt.savefig('transientUx1stOD_comparison_coarseMesh.pdf', dpi = 300, bbox_inches='tight')
plt.show()

################################# Comparison between similarity T and numerical 1stOD PISO T - COARSE MESH ######################################

fig = plt.figure(4)
ax = plt.axes()

plt.plot(etaDimensional07, tempDimensional07, 'o', markeredgecolor='none', markerfacecolor='k', markersize=6, label='Similarity solution')
plt.plot(etaDimensional14, tempDimensional14, 'o', markeredgecolor='none', markerfacecolor='k', markersize=6)
plt.plot(etaDimensional21, tempDimensional21, 'o', markeredgecolor='none', markerfacecolor='k', markersize=6)
plt.plot(etaDimensional28, tempDimensional28, 'o', markeredgecolor='none', markerfacecolor='k', markersize=6)

plt.plot(TMean1stOD_07[:,0], TMean1stOD_07[:,1], linewidth='2', color='k', label='OpenFoam')
plt.plot(TMean1stOD_14[:,0], TMean1stOD_14[:,1], linewidth='2', color='k')
plt.plot(TMean1stOD_21[:,0], TMean1stOD_21[:,1], linewidth='2', color='k')
plt.plot(TMean1stOD_28[:,0], TMean1stOD_28[:,1], linewidth='2', color='k')

plt.xlabel(r'$y$, m')
plt.ylabel(r'$T$, K')
plt.xlim(0, 0.035)
plt.ylim(300, 307)
starty, endy = (300, 307.01)
startx, endx = (0, 0.03501)
ax.yaxis.set_ticks(np.arange(starty,endy,1))
ax.xaxis.set_ticks(np.arange(startx,endx,0.007))
plt.grid(False)
plt.legend(numpoints=1, loc=1)

#Get current figure
figure = plt.gcf()

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
figure.set_size_inches(10, 10)
#When saving, specify the DPI
plt.savefig('transientT1stOD_comparison_coarseMesh.pdf', dpi = 300, bbox_inches='tight')
plt.show()

plt.show()

####################################################### Heat transfer rate ##########################################################

gradT_similarity = np.zeros(samplingPositions.size)
q_similarity = np.zeros(samplingPositions.size)
Q_similarity = np.zeros(samplingPositions.size)
wallArea = 0.3 * 0.005

for i in range(0, samplingPositions.size):
    gradT_similarity[i] = (1/samplingPositions[i]) * (Tplate-Tinf) * math.pow(0.25 * Grx[i],0.25) * y[0,4]

print gradT_similarity

for i in range(0,samplingPositions.size):
    q_similarity[i] = - k * gradT_similarity[i]

print q_similarity

#####################################################################################################################################
############################################################## The end! #############################################################
#####################################################################################################################################
