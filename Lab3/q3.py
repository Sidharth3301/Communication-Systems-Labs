import numpy as np
import matplotlib.pyplot as plt
from  numpy.fft import fft
def getfft(bandwidth=10,start=-2,stop=2,ts=(1/100)):
    
    t=np.arange(start,stop,ts)
    channel=2*bandwidth*np.sinc(2*bandwidth*t)
    rec_signal=np.convolve(channel,m,mode='same')
    hf = fft(rec_signal)/fs
    N=len(hf)
    freq_axis = np.linspace(-fs/2, fs/2, N)  ###extremely important to sample freq
    hf_abs=np.abs(hf)
    hf_abs_sorted=np.fft.fftshift(hf_abs)
    return freq_axis,rec_signal,hf_abs_sorted
fm=20 # 20Hz is the Bandwidth chosen for the sinc pulse (in freq domain)
fs=100
ts=1/fs
start=-1
stop=1
t=np.arange(start,stop,ts)
m=2*fm*np.sinc(2*fm*t)#np.sin(2*np.pi*f1*t)+np.sin(2*np.pi*f2*t)
bw=[10,15,20,50]
freq_axis=[[] for x in bw]
hf_abs=[[] for x in bw]
received=[[] for x in bw]
y_t=[[] for x in bw]
for i,j in enumerate(bw):
    freq_axis[i],y_t[i],hf_abs[i]=getfft(bandwidth=j,start=start,stop=stop,ts=ts)

plt.plot(t,m)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.title('Message Signal')
N=2*(stop-start)*fs
fig,axs=plt.subplots(2,2)
fig2,ax=plt.subplots(2,2)
t2=np.linspace(2*start,2*stop,N)
for i in range(len(bw)):
    plt.subplots_adjust(hspace = 1)
    axs[i//2,i%2].plot(freq_axis[i],hf_abs[i])
    axs[i//2,i%2].set_xlabel('freq')
    axs[i//2,i%2].set_ylabel('amplitude')
    axs[i//2,i%2].set_title(f'bandwidth of channel={bw[i]}Hz')
    ax[i//2,i%2].plot(t,y_t[i])
    ax[i//2,i%2].set_xlabel('time')
    ax[i//2,i%2].set_ylabel('amplitude')
    ax[i//2,i%2].set_title(f'Received Signal: bandwidth of channel={bw[i]}Hz')
plt.show()