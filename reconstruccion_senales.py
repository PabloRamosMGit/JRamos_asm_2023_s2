import numpy as np
from matplotlib import pyplot as plt
from scipy.io.wavfile import write
from scipy.fft import *

sample_rate = 44100  # Hz
duration = 5
freq=100
def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    y = np.sin((2 * np.pi) * frequencies)
    return x,y
def reconstruc_signal(freq,sample_rate,duration):
    x, tono_orignal = generate_sine_wave(freq, sample_rate, duration)
    ruido = np.random.normal(0, 0.1, len(x))
    senal_ruidosa = tono_orignal + ruido
    N = sample_rate * duration
    yf = rfft(senal_ruidosa)
    xf = rfftfreq(N, 1 / sample_rate)
    cutoff_freq = freq
    yf_filtered = yf
    yf_filtered[xf > cutoff_freq] = 0

    signal_filtered = irfft(yf_filtered)
    return senal_ruidosa,signal_filtered

senal_ruidosa,senal_filtrada= reconstruc_signal(freq,sample_rate,duration)
x,senal_original = generate_sine_wave(freq,sample_rate,duration)

plt.plot(senal_filtrada,label="Señal filtrada")
plt.plot(senal_original,label="Señal Original")
plt.legend()
plt.show()