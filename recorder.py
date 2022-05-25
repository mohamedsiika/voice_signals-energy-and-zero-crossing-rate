from scipy.io import wavfile
import sounddevice as sd


class recording:
    def __init__(self, fs=44100, duration=3):
        self.fs = fs
        self.duration = duration

    def start_recording(self):
        self.record = sd.rec(self.fs * self.duration, samplerate=self.fs, channels=2)
        print('you are recording Now for', self.duration, 'seconds...')
        sd.wait()
        wavfile.write('voice.wav', self.fs, self.record)  # Save as WAV file
