import librosa # audio analysis
import IPython.display as ipd

wav, sr = librosa.load("file.mp3")
# sr = sampling rate
# wav = np.array (audio file is converted to time series), supports multichannel

# Mel Spectrogram
n_mels = 80
fmax = 4096
fig, ax = plt.subplots()
M = librosa.feature.melspectrogram(y=wav, sr=sr, n_mels=n_mels, fmax=fmax, n_fft=2048)
M_db = librosa.power_to_db(M, ref=np.max)
img = librosa.display.specshow(M_db, y_axis='mel', x_axis='time', ax=ax, fmax=fmax)
