import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import librosa.display
# Definir una función para generar un tono seno
def generate_sine_wave(frequency, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = np.sin(2 * np.pi * frequency * t)
    return t, signal

# Generar un tono seno a 5 Hz durante 2 segundos
sample_rate = 44100  # Tasa de muestreo en Hz
duration = 2  # Duración en segundos
frequency = 1000  # Frecuencia en Hz
t, sine_wave = generate_sine_wave(frequency, duration, sample_rate)

# Agregar ruido gaussiano a la señal
noise = np.random.normal(0, 0.1, len(t))  # Media 0, desviación estándar 0.5
noisy_signal = sine_wave + noise

# Aplicar un filtro pasa-bajos para eliminar el ruido
cutoff_frequency = 1000  # Frecuencia de corte en Hz
b, a = signal.butter(4, cutoff_frequency / (sample_rate / 2), 'low')
filtered_signal = signal.filtfilt(b, a, noisy_signal)


frequencies, times, spectrogram = signal.spectrogram(filtered_signal, fs=sample_rate)
log_spec = librosa.power_to_db(spectrogram)

plt.pcolormesh(times, frequencies, log_spec, shading='gouraud')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.colorbar()
plt.title('Espectrograma Señal Reconstruida')
plt.show()

frequencies2, times2, spectrogram2 = signal.spectrogram(sine_wave, fs=sample_rate)
log_spec2 = librosa.power_to_db(spectrogram2)

plt.pcolormesh(times2, frequencies2, log_spec2, shading='gouraud')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.colorbar()
plt.title('Espectrograma Señal Original')
plt.show()




# Graficar las señales
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(t, sine_wave)
plt.title('Tono Seno Original')

plt.subplot(3, 1, 2)
plt.plot(t, noisy_signal)
plt.title('Tono Seno con Ruido Gaussiano')

plt.subplot(3, 1, 3)
plt.plot(t, filtered_signal)
plt.title('Señal Filtrada')
plt.xlabel('Tiempo (s)')

plt.tight_layout()
plt.show()
