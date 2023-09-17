from pydub import AudioSegment
#Codigo simple para cambiar audio de stereo a mono
sound = AudioSegment.from_wav('audio\\scale.wav')
sound = sound.set_channels(1)
sound.export('audio\\scale.wav', format="wav")