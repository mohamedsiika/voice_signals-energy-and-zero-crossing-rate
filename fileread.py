from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt


class read:
    def __init__(self):
        self.rate, self.data = wavfile.read('voice.wav')
        self.framing()
        self.plot_total_wave()
        print(self.rate)

    def framing(self):
        self.frame_size = int(0.01 * self.rate)
        self.overlap=2
        self.frames = []
        self.E = []
        self.ZCR = []
        self.energy = 0
        self.counter = 0
        for i in range(0, len(self.data), self.frame_size-self.overlap):
            self.frames.append(self.data[i:i + self.frame_size])


        for i in range(len(self.frames)):
            for j in range(len(self.frames[i])):
                self.energy = self.energy + pow(self.frames[i][j], 2)

                if (len(self.frames[i]) - j > 1):  # Not the last index
                    if (self.frames[i][j][0] * self.frames[i][j + 1][0] ) < 0:  # The product is negative then it crossed the zero
                        self.counter += 1
            self.ZCR.append(self.counter)
            self.E.append(self.energy)
            self.energy = 0
            self.counter = 0


    def plot_total_wave(self):
        times = np.arange(len(self.data)) / float(self.rate)

        plt.figure(figsize=(30, 4))
        plt.fill_between(times, self.data[:, 0], color='cyan')
        plt.xlim(times[0], times[-1])
        plt.xlabel('time (s)')
        plt.ylabel('amplitude')
        plt.show()

    def plot_frame(self, framenumber):
        times = np.arange(self.frame_size) / float(self.rate)

        plt.figure(figsize=(30, 4))
        plt.fill_between(times, self.frames[framenumber][:, 0], color='cyan')
        plt.xlim(times[0], times[-1])
        plt.xlabel('time (s)')
        plt.ylabel('amplitude')
        plt.show()

    def plot_energy(self):
            times = np.arange(len(self.E))
            self.E=np.array(self.E)
            plt.figure(figsize=(30, 4))
            plt.fill_between(times, self.E[:, 0], color='cyan')
            plt.xlim(times[0], times[-1])
            plt.xlabel('time (s)')
            plt.ylabel('amplitude')
            plt.show()
    def plot_ZCR(self):
            times = np.arange(len(self.E))
            plt.figure(figsize=(30, 4))
            plt.fill_between(times, self.ZCR, color='cyan')
            plt.xlim(times[0], times[-1])
            plt.xlabel('time (s)')
            plt.ylabel('amplitude')
            plt.show()




