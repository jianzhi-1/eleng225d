import librosa # audio analysis
import IPython.display as ipd

wav, sr = librosa.load("file.mp3")
# sr = sampling rate (22050 for lower-quality audio files, the dimension of the array needs to be divided by sr to be in dimension of time)
# wav = np.array (audio file is converted to time series), supports multichannel

# Plotting an audio wave
def plot_audio(wav, sr, max_len=None, filename=None):
    wav = wav.copy()
    if max_len is not None:
        wav = wav[:int(max_len*sr)]
    plt.figure(figsize=(12, 8))
    plt.plot(np.arange(len(wav))/sr, wav)
    plt.xlabel("Time / s")
    plt.ylabel("Amplitude / unit")
    if filename is None: 
        plt.title("Plot of Amplitude against Time")
    else:
        plt.title(f"Plot of Amplitude against Time - {filename}")
    plt.show()

ipd.Audio(wav, rate=sr)

# Mel Spectrogram
def plot_mel_spectrogram(wav, sr, n_mels=80, fmax=4096):
    fig, ax = plt.subplots()
    M = librosa.feature.melspectrogram(y=wav, sr=sr, n_mels=n_mels, fmax=fmax, n_fft=2048)
    M_db = librosa.power_to_db(M, ref=np.max)
    img = librosa.display.specshow(M_db, y_axis='mel', x_axis='time', ax=ax, fmax=fmax)

# Plot everything
def plot_all(wav, sr, max_len=None, filename=None, n_mels=80, fmax=4096):
    fig, ax = plt.subplots(2)

    wav = wav.copy()
    if max_len is not None:
        wav = wav[:int(max_len*sr)]
    ax[0].plot(np.arange(len(wav))/sr, wav)
    ax[0].set_xlabel("Time / s")
    ax[0].set_ylabel("Amplitude / unit")
    if filename is None: 
        ax[0].set_title("Plot of Amplitude against Time")
    else:
        ax[0].set_title(f"Plot of Amplitude against Time - {filename}")

    M = librosa.feature.melspectrogram(y=wav, sr=sr, n_mels=n_mels, fmax=fmax, n_fft=2048)
    M_db = librosa.power_to_db(M, ref=np.max)
    img = librosa.display.specshow(M_db, y_axis='mel', x_axis='time', ax=ax[1], fmax=fmax)

# Short time Fourier Transform (STFT)
librosa.stft(y[:n_fft], hop_length = n_fft+1)

# !ls ./drive/MyDrive/225dhw1


