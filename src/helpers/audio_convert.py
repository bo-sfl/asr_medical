import librosa
import soundfile as sf


def load_raw(path):
    """
    Load audio file and convert to 16kHZ sample rate, mono-channel
    path: absolute path of file to load
    """
    y, s = librosa.load(path, sr=16000)
    y=librosa.to_mono(y)
    return y

def write_wav(path, data):
    """
    Write as a proper .wav file
    path: absolute path with filename
    data: numpy array
    """
    sf.write(path, format='wav', data=data, samplerate=16000)
    return
