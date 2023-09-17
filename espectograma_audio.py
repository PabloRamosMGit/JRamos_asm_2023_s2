import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
import numpy as np
import librosa.display
#Audios
audio_librosa = 'audio\\scale_stereo.wav'
audio_2 = 'audio\\violin_c.wav'
audio_3 = 'audio\\piano_c.wav'

scale, sr = librosa.load(audio_librosa)

scale2, sr2 = librosa.load(audio_2)

scale3, sr3 = librosa.load(audio_3)

sample_rate, samples = wavfile.read('audio\\scale_mono.wav')

#Calcula el tiempo que dura el audio
time = np.arange(len(samples)) / sample_rate
# Plot 2D the la señal de audio
plt.figure()
plt.plot(time, samples)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Audio Signal 2D')
plt.show()

frequencies, times, spectrogram = signal.spectrogram(samples, fs=sample_rate) #Espectrograma usando signal
log_spec = librosa.power_to_db(spectrogram)
#Espectrogram de Mel
mel_spectrogram = librosa.feature.melspectrogram(y=scale, sr=sr, n_fft=2048, hop_length=512, n_mels=90)
log_mel_spectrogram = librosa.power_to_db(mel_spectrogram)
librosa.display.specshow(log_mel_spectrogram,x_axis="time",y_axis="mel",sr=sr)
plt.colorbar(format="%+2.f")
plt.title('Mel Spectrogram')
plt.show()

#Sin escala logaritmica
plt.pcolormesh(times, frequencies, spectrogram, shading='gouraud')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.colorbar()
plt.title('Spectrogram without logarithmic scale')
plt.show()

#Con escala logaritmica
plt.pcolormesh(times, frequencies, log_spec, shading='gouraud')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.colorbar(label='Power/Frequency (dB/Hz)')
plt.title('Spectrogram with logarithmic scale')
plt.show()

#Espectrogram de Mel con violin tocando la nota C
mel_spectrogram2 = librosa.feature.melspectrogram(y=scale2, sr=sr2, n_fft=2048, hop_length=512, n_mels=90)
log_mel_spectrogram2 = librosa.power_to_db(mel_spectrogram2)
librosa.display.specshow(log_mel_spectrogram2,x_axis="time",y_axis="mel",sr=sr)
plt.colorbar(format="%+2.f")
plt.title('Violín')
plt.show()

#Espectrogram de Mel con piano tocando la nota C
mel_spectrogram3 = librosa.feature.melspectrogram(y=scale3, sr=sr3, n_fft=2048, hop_length=512, n_mels=90)
log_mel_spectrogram3 = librosa.power_to_db(mel_spectrogram3)
librosa.display.specshow(log_mel_spectrogram3,x_axis="time",y_axis="mel",sr=sr)
plt.colorbar(format="%+2.f")
plt.title('Piano')
plt.show()



