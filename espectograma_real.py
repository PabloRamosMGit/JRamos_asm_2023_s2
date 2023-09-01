import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
#Codigo de ejemplo del espectograma real, sacado de la documentacion de scipy,
#Se encuentra disponible en https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.spectrogram.html

#Esto es un generador aleatorio que se utilizará para agregar ruido aleatorio a la señal.
rng = np.random.default_rng()
fs = 10e3 #Sampling frequency, 10kHz
N = 1e5 #Number of samples in the signal
amp = 2 * np.sqrt(2) #Amplitud de la onda portadora

noise_power = 0.01 * fs / 2 #Potencia del ruido

time = np.arange(N) / float(fs) #Es el tiempo de muestreo

mod = 500*np.cos(2*np.pi*0.25*time) #Es una forma de onda coseno con una frecuencia de 0,25 Hz que modulará la señal portadora.

carrier = amp * np.sin(2*np.pi*3e3*time + mod) #Es la señal portadora

noise = rng.normal(scale=np.sqrt(noise_power), size=time.shape)
noise *= np.exp(-time/5)  #El ruido va decreciendo exponecialmente

x = carrier + noise  #La señal final que es el ruido más la señal portadora
f, t, Sxx = signal.spectrogram(x, fs)  #Se saca el array de valores del espectograma

#Por ultimo se grafica
plt.pcolormesh(t, f, Sxx, shading='gouraud')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [s]')
plt.show()
