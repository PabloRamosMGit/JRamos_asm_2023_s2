from pydub import AudioSegment
sound = AudioSegment.from_wav('audio\\scale.wav')
sound = sound.set_channels(1)
sound.export('audio\\scale.wav', format="wav")