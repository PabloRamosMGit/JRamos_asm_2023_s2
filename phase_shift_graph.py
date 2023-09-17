import numpy as np
import matplotlib.pyplot as plt

# Frecuencias original y deseada en Hz
frecuencia_original = 1000  # Hz
# Calcular la fase requerida para el cambio de frecuencia
fase_requerida = np.pi  # 180 grados o π radianes
fase_shift = (np.pi/4)
fase_shift_2 = (np.pi/3)
fase_shift_3 = (np.pi/4)
duracion = 5.0/frecuencia_original # Duración de la señal en segundos
sample_rate = 44100  # Tasa de muestreo en Hz

t = np.linspace(0, duracion, int(sample_rate * duracion), endpoint=False)

audio_original = np.sin(2 * np.pi * frecuencia_original * t)

audio_fase_modificada_1= -audio_original #Inversion de fase, 180

audio_fase_modificada_2 = np.sin(2 * np.pi * frecuencia_original * t+ fase_shift) #Un desfase 45 grados

audio_fase_modificada_3 = -(np.sin(2 * np.pi * frecuencia_original * t+ fase_shift_2)) #Un desfase 60  grados e inversion

audio_fase_modificada_4 = -(np.sin(2 * np.pi * frecuencia_original * t+ fase_shift_3)) #Un desfase 90 grados e inversion


audio_result_1= audio_original + audio_fase_modificada_1

audio_result_2= audio_original + audio_fase_modificada_2

audio_result_3= audio_original + audio_fase_modificada_3

audio_result_4= audio_original + audio_fase_modificada_4

plt.figure(figsize=(10, 4))
plt.plot(t, audio_original, label='Seno original')
plt.plot(t, audio_fase_modificada_4, label='Seno con cambio de fase')
plt.plot(t, audio_result_4, label='Seno resultante')
plt.title('Manipulación de Fase')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()
plt.show()

