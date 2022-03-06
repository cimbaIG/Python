import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

def time(T, N):
    return np.linspace(0, N * T, N, endpoint = False)

def sine_wave(A, T, N):
    t = time(T, N)
    return A * np.sin((2 * np.pi/(N * T)) * t)

#Fourier transform
A = 1 #Sine wave amplitude
N = len(sine_wave(1,0.25,4)) #Number of sample points
T = 0.25 #Sample spacing (period)
t = time(T,N)
yf = fft(sine_wave(1,0.25,4))
xf = fftfreq(N, T)[:N//2] #only first N//2 results are of interest
print(f"Frequencies = {xf},",f"Amplitudes = {2.0/N * np.abs(yf[0:N//2])}.")

print(fftfreq(N, T))

#Plot signal data
plt.plot(t,sine_wave(A,T,N))
plt.xlim([0, len(t)])
plt.ylim([-1,1])
plt.grid()
plt.title("Signal")
plt.show()

#Plot Fourier transform results
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.xlim([0, len(yf)])
plt.ylim([-1,1])
plt.grid()
plt.title("Fourier transform")
plt.show()