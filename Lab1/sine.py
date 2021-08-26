import numpy as np
import pylab as plt
k=[5*x for x in range(1,11)]
fig,axs=plt.subplots(5,2)
for i in range(10):
    t=np.linspace(0,0.1,k[i])
    m=np.sin(2*np.pi*8*10*t)
    plt.subplots_adjust(hspace = 1)
    axs[i//2,i%2].plot(t,m)
    axs[i//2,i%2].set_xlabel('time')
    axs[i//2,i%2].set_ylabel('amplitude')
    axs[i//2,i%2].set_title(f'Sampled at {k[i]/0.1}Hz')

plt.suptitle('Signal of 80Hz')
plt.show()
