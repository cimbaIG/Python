from time import time
from more_itertools import sample
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

#Read moment signal data and create moment and sample vectors
velocity_data = np.loadtxt("velocity_signal.txt")
velocity = velocity_data[:,0]
samples = velocity_data[:,1]

#Data sampling frequency
fs = 2000

#Create time vector from sample number and frequency
time_ = samples / fs
nsecs = time_[len(time_) - 1]
#lx = int(fs * nsecs) #Get window length
lx = len(time_) ** 2 #Get window length

#Compute and plot the power spectral density
f, Pxx_den = signal.welch(velocity, fs, nperseg = len(time_), scaling = "density")

fig, (ax0, ax1) = plt.subplots(2, 1)
ax0.plot(time_,velocity,color='black')
ax0.set_title("Velocity signal")
ax0.set_xlabel('Time t [s]')
ax0.set_ylabel('Velocity [m/s]')

ax1.plot(f, Pxx_den,color='black')
ax1.set_title("PSD of velocity signal using Welch method")
ax1.set_xlabel('Frequency f [Hz]')
ax1.set_ylabel('PSD [(m/s)^2/Hz]')
plt.yscale("log")
plt.xscale("log")

plt.show()