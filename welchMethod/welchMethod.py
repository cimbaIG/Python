from time import time
from more_itertools import sample
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

#Read moment signal data and create moment and sample vectors
moment_data = np.loadtxt("moment_signal.txt")
moment = moment_data[:,0]
samples = moment_data[:,1]

#Data sampling frequency
fs = 2000

#Create time vector from sample number and frequency
time_ = samples / fs
nsecs = time_[len(time_) - 1]
lx = int(fs * nsecs) #Get window length

#Compute and plot the power spectral density
f, Pxx_den = signal.welch(moment, fs)

fig, (ax0, ax1) = plt.subplots(2, 1)
ax0.plot(time_,moment,color='black')
ax0.set_title("Moment signal")
ax0.set_xlabel('Time t [s]')
ax0.set_ylabel('Moment M [Nm]')

ax1.semilogy(f, Pxx_den,color='black')
ax1.set_title("PSD of moment signal using Welch method")
ax1.set_xlabel('Frequency f [Hz]')
ax1.set_ylabel('PSD [(Nm)^2/Hz]')

plt.show()