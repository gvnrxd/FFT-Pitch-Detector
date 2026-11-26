# FFT Pitch Detector

A Python desktop app for visualizing WAV audio and exploring how the Fast Fourier Transform (FFT) can estimate pitch. The current version plots mono, stereo, and multichannel waveforms. The next milestone is to display a frequency spectrum and estimate the pitch of a single note.

## What it does today

- Opens a desktop file picker for selecting a WAV file.
- Prints the clip duration, channel count, and number of samples per channel.
- Plots amplitude over time with a labeled trace for each channel.
- Lets you zoom and pan to inspect individual cycles or compare channels.

## Getting started

### Ubuntu and WSL

Clone or download the repository and open a terminal in the project folder. Install Python, virtual environment support, and Tk for the file picker and plot window. If you're using WSL, make sure it can open Linux GUI apps.

```bash
sudo apt install python3 python3-venv python3-tk
```

Create a virtual environment and install the Python dependencies.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Start the app from the activated environment.

```bash
python main.py
```

Choose a supported WAV file in the picker. A **16-bit PCM WAV** is a good first test. Some files with a `.wav` extension use encodings that SciPy's WAV reader does not support, such as A-law.

## Try a 440 Hz tone

Open `sine-wave-440-hz.wav` if it's included in your checkout, or select another pure 440 Hz tone. Zoom in to about **10 milliseconds** and compare two neighboring crests. They should be about **2.27 milliseconds apart**, since a 440 Hz tone completes 440 cycles per second.

For a stereo test, use a WAV with different tones on the left and right. A 440 Hz left channel and an 880 Hz right channel should show the right waveform cycling twice as fast over the same time interval.

## Dependencies

| Package | Role |
| --- | --- |
| Tkinter | Opens the WAV file picker. |
| SciPy | Reads the sample rate and audio samples from the WAV file. |
| NumPy | Handles the sample arrays and builds the time axis. |
| Matplotlib | Displays the waveform and provides zoom and pan controls. |

## Next milestone

Compute the **discrete Fourier transform (DFT)** with NumPy's **fast Fourier transform (FFT)**, plot magnitude against frequency, and estimate the pitch of a clean tone. The 440 Hz test tone should produce a peak near **440 Hz** in that spectrum.
