import numpy as np
import matplotlib.pyplot as plt
from  numpy.fft import fft
start_time=-2
stop_time=2
fm = 10    # Maximum frequency component in Hertz for the given spectrum
fs=10*fm
ts=1/fs
time = np.arange(start_time,stop_time,ts)
h_t = 0.2*np.sinc(2*fm*time)    ###  np.sin(2*fm*np.pi*time) for sinewave
hf = fft(h_t)/fs
N=len(hf)
freq_axis = np.linspace(-fs/2, fs/2, N)  ###extremely important to sample freq
hf_abs=np.abs(hf)
hf_abs_sorted=np.fft.fftshift(hf_abs)   ##### for increasing freq samples
fig,axs=plt.subplots(2)
plt.subplots_adjust(hspace = 1)
axs[0].plot(time,h_t)
axs[0].set_title('Time Domain')
axs[0].set_xlabel('time')
axs[0].set_ylabel('Amplitude')
axs[1].plot(freq_axis,hf_abs_sorted)
axs[1].set_title('Freq Domain')
axs[1].set_xlabel('Freq')
axs[1].set_ylabel('Amplitude')
plt.suptitle('Band Limited System for Channel Model')
plt.show()