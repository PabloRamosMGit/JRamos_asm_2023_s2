import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram
#Código de espectrograma complejo

fs = 4000  #Sampling frequency, 4kHz
t = np.arange(0, 5, 1/fs) #Number of samples in the signal
x2 = np.exp(2j * np.pi * 100 * np.cos(2 * np.pi * 2 * t)) #Señal compleja


# Array de espectrograma complejo
frequencies, times, Sxx = spectrogram(x2, fs=fs, nperseg=256, noverlap=128,return_onesided=False)

#Graficar el espectograma, se utliza decibeles para que se grafique mejor el espectograma de X
plt.pcolormesh(times, frequencies, 10 * np.log10(np.abs(Sxx)),shading='gouraud')
plt.title('Complex Spectrogram')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.colorbar(label='Power/Frequency (dB/Hz)')
plt.show()
