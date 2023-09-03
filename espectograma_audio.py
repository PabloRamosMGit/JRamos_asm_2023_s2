import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
import numpy as np
import librosa.display

audio_librosa = 'audio\\scale_stereo.wav'
scale, sr = librosa.load(audio_librosa)
sample_rate, samples = wavfile.read('audio\\scale_mono.wav')

# Calculate the time in seconds for each sample
time = np.arange(len(samples)) / sample_rate
# Plot the audio signal with time on the x-axis
plt.figure()
plt.plot(time, samples)
# Label the axes and title
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Audio Signal over Time')
plt.show()

frequencies, times, spectrogram = signal.spectrogram(samples, fs=sample_rate)


mel_spectrogram = librosa.feature.melspectrogram(y=scale, sr=sr, n_fft=2048, hop_length=512, n_mels=90)
log_mel_spectrogram = librosa.power_to_db(mel_spectrogram)
librosa.display.specshow(log_mel_spectrogram,x_axis="time",y_axis="mel",sr=sr)
plt.colorbar(format="%+2.f")
plt.show()

#Sin escala logaritmica
plt.pcolormesh(times, frequencies, spectrogram, shading='gouraud')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.colorbar(label='Power/Frequency (dB/Hz)')
plt.show()

#Con escala logaritmica pero aun la frecuencia no se logra ver bien
plt.pcolormesh(times, frequencies, 10*np.log10(spectrogram), shading='gouraud')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.colorbar(label='Power/Frequency (dB/Hz)')
plt.show()



