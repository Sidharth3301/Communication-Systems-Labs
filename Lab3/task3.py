import numpy as np
import pylab as plt
from  numpy.fft import fft
def getfft(bandwidth=10,start=-2,stop=2,ts=(1/100)):
    
    t=np.arange(start,stop,ts)
    channel=2*bandwidth*np.sinc(2*bandwidth*t)
    rec_signal=np.convolve(channel,m)
    hf = fft(rec_signal)/fs
    N=len(hf)
    freq_axis = np.linspace(-fs/2, fs/2, N)  ###extremely important to sample freq
    hf_abs=np.abs(hf)
    hf_abs_sorted=np.fft.fftshift(hf_abs)
    return freq_axis,hf_abs_sorted
f1=5
fm=20   #used 20Hz sinc signal, whose bandwidth is also 20 Hz
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
for i,j in enumerate(bw):
    freq_axis[i],hf_abs[i]=getfft(bandwidth=j,start=start,stop=stop,ts=ts)
    received[i]=np.fft.ifftshift((np.fft.ifft(hf_abs[i])))
# k=[5*x for x in range(1,11)]

#plt.plot(t,m)
fig1,axs=plt.subplots(2,2)
fig2,ax=plt.subplots(2,2)
N=(stop-start)*fs
for i in range(len(bw)):
    plt.subplots_adjust(hspace = 1)
    axs[i//2,i%2].plot(freq_axis[i],hf_abs[i])
    axs[i//2,i%2].set_xlabel('time')
    axs[i//2,i%2].set_ylabel('amplitude')
    axs[i//2,i%2].set_title(f'bandwidth of channel={bw[i]}Hz')
    #plt.subplots_adjust(hspace = 1)
    ax[i//2,i%2].plot(t,received[i][int(N/2):int(3*N/2)],label='reconstruct')
    ax[i//2,i%2].plot(t,m,label='original')
    ax[i//2,i%2].set_xlabel('time')
    ax[i//2,i%2].set_ylabel('amplitude')
    ax[i//2,i%2].set_title(f'reconstruction: bandwidth of channel={bw[i]}Hz')
    ax[i//2,i%2].legend()
plt.show()
