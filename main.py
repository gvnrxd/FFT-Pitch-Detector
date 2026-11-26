from tkinter import filedialog

import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

# import sounddevice as sd


wav_fname = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])

samplerate, data = wavfile.read(wav_fname)
mono = None
channelSize = data.shape[1] if len(data.shape) > 1 else len(data.shape)
print(channelSize)

if channelSize == 1:
    print("Mono")
elif channelSize == 2:
    print("Stereo")
else:
    print("Multichannel")

print(f"{data.shape[0]} samples per channel, {channelSize} channels")

length = data.shape[0] / samplerate
print(f"File is {length:.2f}s long")

time = np.linspace(0.0, length, data.shape[0])

if channelSize == 1:
    plt.plot(time, data, label="Mono")
elif channelSize == 2:
    plt.plot(time, data[:, 0], label="Left channel")
    plt.plot(time, data[:, 1], label="Right channel")
else:
    for channel in range(channelSize):
        plt.plot(time, data[:, channel], label={f"Channel: {channel}"})


plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

plt.tight_layout(pad=1.5, rect=(0.05, 0, 0.95, 1))
plt.gcf().canvas.manager.set_window_title("FFT Pitch Detector")

plt.xlim(0, length)
plt.show()
