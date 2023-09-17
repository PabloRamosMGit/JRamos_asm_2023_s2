import numpy as np
import soundfile as sf

# Load an audio file
audio, sample_rate = sf.read('audio\\scale_stereo.wav')

# Specify the phase shift angle (in radians)
phase_shift = 3*(np.pi)/4  # 45 degrees

# Apply the phase shift
audio_shifted = audio * np.exp(1 * phase_shift)

try:
    sf.write('audio\\scale_phase_shift_2.wav.wav', audio_shifted, sample_rate)
    print("Output audio saved successfully.")
except Exception as e:
    print(f"Error: {e}")