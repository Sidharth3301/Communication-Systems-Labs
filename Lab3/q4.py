import numpy as np
import pylab as plt
from  numpy.fft import fft
def rect(x,T):
    return np.where(np.logical_and(x<T,x>-T),1,0)

fs=200
ts=1/fs
start=-3
stop=3
t=np.arange(start,stop,ts)
duration=[0.1,1,2] # Width of the rect signal = 5 sec
bandwidth=10  

#m=rect(t,duration)  # Rect signal message
def getfft(m):
    channel=2*bandwidth*np.sinc(2*bandwidth*t)
    y_t=np.convolve(channel,m,mode='same')
   # y_t=y_t/(duration*np.max(channel)) #normalising the received signal
    hf = fft(y_t)/fs

    N=len(hf)
    freq_axis = np.linspace(-fs/2,fs/2 , N)  ###extremely important to sample freq
    hf_abs=np.abs(hf)
    hf_abs_sorted=np.fft.fftshift(hf_abs)
    return freq_axis,y_t, hf_abs_sorted

hf_abs_sorted=[[] for x in duration]
freq_axis=[[] for x in duration]
y_t=[[] for x in duration]
m=[[] for x in duration]
for i,j in enumerate(duration):
    m[i]=rect(t,j)
    freq_axis[i],y_t[i],hf_abs_sorted[i]=getfft(m[i])
fig,axs=plt.subplots (3,1)
fig1,axs1=plt.subplots (3,1)
fig2,axs2=plt.subplots (3,1)
fig.subplots_adjust(hspace = 1)
fig1.subplots_adjust(hspace = 1)
fig2.subplots_adjust(hspace = 1)
axs[0].plot(t,m[0])
axs[0].set_title('Message signal')
axs[0].set_xlabel('time')
axs[0].set_ylabel('amplitude')

axs[1].plot(t,y_t[0])
axs[1].set_title('received signal-Time domain')
axs[1].set_xlabel('time')
axs[1].set_ylabel('amplitude')
axs[2].plot(freq_axis[0],hf_abs_sorted[0])
axs[2].set_title('received signal-Frequency domain')
axs[2].set_xlabel('freq')
axs[2].set_ylabel('amplitude')
fig.suptitle('Duration of message signal=0.1s')
axs1[0].plot(t,m[1])
axs1[0].set_title('Message signal')
axs1[0].set_xlabel('time')
axs1[0].set_ylabel('amplitude')

axs1[1].plot(t,y_t[1])
axs1[1].set_title('received signal-Time domain')
axs1[1].set_xlabel('time')
axs1[1].set_ylabel('amplitude')
axs1[2].plot(freq_axis[1],hf_abs_sorted[1])
axs1[2].set_title('received signal-Frequency domain')
axs1[2].set_xlabel('freq')
axs1[2].set_ylabel('amplitude')
fig1.suptitle('Duration of message signal=1s')
axs2[0].plot(t,m[2])
axs2[0].set_title('Message signal')
axs2[0].set_xlabel('time')
axs2[0].set_ylabel('amplitude')

axs2[1].plot(t,y_t[2])
axs2[1].set_title('received signal-Time domain')
axs2[1].set_xlabel('time')
axs2[1].set_ylabel('amplitude')
axs2[2].plot(freq_axis[2],hf_abs_sorted[2])
axs2[2].set_title('received signal-Frequency domain')
axs2[2].set_xlabel('freq')
axs2[2].set_ylabel('amplitude')
fig2.suptitle('Duration of message signal=2s')
plt.show()