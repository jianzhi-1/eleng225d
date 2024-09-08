import librosa # audio analysis
import IPython.display as ipd

wav, sr = librosa.load("file.mp3")
# sr = sampling rate (22050 for lower-quality audio files, the dimension of the array needs to be divided by sr to be in dimension of time)
# wav = np.array (audio file is converted to time series), supports multichannel

# Plotting an audio wave
def plot(wav, sr):
    plt.figure(figsize=(12, 8))
    plt.plot(np.arange(len(wav))/sr, wav)
    plt.xlabel("Time / s")
    plt.ylabel("Amplitude / unit")
    plt.title("Plot of Amplitude against Time")
    plt.show()

# Mel Spectrogram
n_mels = 80
fmax = 4096
fig, ax = plt.subplots()
M = librosa.feature.melspectrogram(y=wav, sr=sr, n_mels=n_mels, fmax=fmax, n_fft=2048)
M_db = librosa.power_to_db(M, ref=np.max)
img = librosa.display.specshow(M_db, y_axis='mel', x_axis='time', ax=ax, fmax=fmax)
