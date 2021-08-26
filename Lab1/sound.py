import numpy as np
import simpleaudio as sa

frequency1 = 440 #two frequencies for two notes
frequency2= 500  
fs = 44100  # 44100 samples per second
seconds = 2 # Note duration of 3 seconds

# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * fs, False)

# Generate two sine waves 
note1 = np.sin(frequency1 * t * 2 * np.pi)  #440hz
note2 =  np.sin(frequency2 * t * 2 * np.pi)  #500hz
note= note1+note2
# Ensure that highest value is in 16-bit range
audio = note * (2**15 - 1) / np.max(np.abs(note))
# Convert to 16-bit data
audio = audio.astype(np.int16)

# Start playback
play_obj = sa.play_buffer(audio, 1, 2, fs) #stands for 1 channel, 2 bytes per channel input, sampling frequency

# Wait for playback to finish before exiting
play_obj.wait_done()