import numpy as np
import pylab as plt
from  numpy.fft import fft
def getfft(m,bandwidth=10,start=-2,stop=2,ts=(1/100)):
    
    t=np.arange(start,stop,ts)
    fs=1/ts
    channel=2*bandwidth*np.sinc(2*bandwidth*t)
    rec_signal=np.convolve(channel,m)
    hf = fft(rec_signal)/fs
    N=len(hf)
    freq_axis = np.linspace(-0.5,0.5 , N)  ###extremely important to sample freq
    hf_abs=np.abs(hf)
    hf_abs_sorted=np.fft.fftshift(hf_abs)
    return freq_axis,hf_abs_sorted
def rect(x,T):
    return np.where(np.logical_and(x<T,x>-T),1,0)

f1=5
fm=20   #used 20Hz sinc signal, whose bandwidth is also 20 Hz
fs=100
ts=1/fs
start=-10
stop=10
t=np.arange(start,stop,ts)
duration=[5,6,7,8]
msg=[[] for i in t]
for i,j in enumerate(duration):
    msg[i]=rect(t,j)#2*fm*np.sinc(2*fm*t)#np.sin(2*np.pi*f1*t)+np.sin(2*np.pi*f2*t)
#bw=[2,5,9,15]
freq_axis=[[] for x in duration]
hf_abs=[[] for x in duration]
received=[[] for x in duration]
for i,j in enumerate(duration):
    freq_axis[i],hf_abs[i]=getfft(msg[i],bandwidth=j,start=start,stop=stop,ts=ts)
    received[i]=np.fft.ifftshift((np.fft.ifft(hf_abs[i])))

#plt.plot(t,m)
fig1,axs=plt.subplots(2,2)
fig2,ax=plt.subplots(2,2)
# fig3,(ax1,ax2)=plt.subplots(2,1)
# ax1.plot(t,msg)

N=(stop-start)*fs

# msg_fft=np.fft.fft(msg)
# n=len(msg_fft)
# f_space=np.linspace(-2,2,n)
# ax2.plot(f_space,np.fft.fftshift(np.abs(msg_fft/fs)))
for i in range(len(duration)):
    plt.subplots_adjust(hspace = 1)
    axs[i//2,i%2].plot(freq_axis[i],hf_abs[i])
    axs[i//2,i%2].set_xlabel('freq')
    axs[i//2,i%2].set_ylabel('amplitude')
    axs[i//2,i%2].set_title(f'Duration of Rect signal={duration[i]}sec')
    #plt.subplots_adjust(hspace = 1)
    ax[i//2,i%2].plot(t,received[i][int(N/2):int(3*N/2)],label='reconstruct')
    ax[i//2,i%2].plot(t,msg[i],label='original')
    ax[i//2,i%2].set_xlabel('time')
    ax[i//2,i%2].set_ylabel('amplitude')
    ax[i//2,i%2].set_title(f'reconstruction: Duration of signal={duration[i]}sec')
    ax[i//2,i%2].legend()
plt.show()
