import scipy
import scipy.integrate
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#Change font type and font size in axis labels
matplotlib.rcParams.update({'legend.markerscale': 1.5, 'legend.handlelength': 1, 'legend.frameon': 1, 'legend.handletextpad': 1 , 'font.size': 18,'font.family':'Times New Roman'})

#Change font type and font size in axis labels
matplotlib.rcParams.update({'legend.markerscale': 1.5, 'legend.handlelength': 1, 'legend.frameon': 1, 'legend.handletextpad': 1 , 'font.size': 18,'font.family':'Times New Roman'})

#matplotlib.rcParams['text.usetex'] = True
#matplotlib.rcParams['text.latex.unicode'] = True
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

def blasius(y, eta):
    return [y[1], y[2], -0.5*y[0]*y[2]]

n = 201
initial_condition = [0,0,0.33206]
eta = np.linspace(0, 10, n)
y = scipy.integrate.odeint(blasius, initial_condition, eta)

print np.size(eta)
print np.size(y)

fig = plt.figure(1)
ax = plt.axes()
plt.plot(y[:,0], eta, color='k', linewidth=2, linestyle='-' , label=r'$f(\eta)$')
plt.plot(y[:,1], eta,color='k',linewidth=2, linestyle='--' , label=r'$\frac{df(\eta)}{d\eta}$')
plt.plot(y[:,2], eta, color='k',linewidth=2, linestyle='-.', label=r'$\frac{d^2 f(\eta)}{d\eta^2}$')
plt.xlabel(r'$f(\eta),\frac{df(\eta)}{d\eta},\frac{d^2 f(\eta)}{d\eta^2}$', fontname="Times New Roman", fontsize=24)
plt.ylabel(r'$\eta$', fontname="Times New Roman", fontsize=24)
startY, endY = (0, 10.01)
startX, endX = (0, 1.201)
plt.xlim(startX, endX)
plt.ylim(startY, endY)
ax.yaxis.set_ticks(np.arange(startY,endY,1))
ax.xaxis.set_ticks(np.arange(startX,endX,0.1))
legend = plt.legend(numpoints=1, loc=2)
frame = legend.get_frame()
plt.grid(True)
ax.grid(color='k', linestyle=':', linewidth=0.2)

#Get current figure
figure = plt.gcf()
#Set figure size
figure.set_size_inches(7, 5)
#When saving, specify the DPI
plt.savefig('blasiusSolution.png', dpi = 300, bbox_inches='tight')

plt.show()