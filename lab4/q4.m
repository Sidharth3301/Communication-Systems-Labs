clc; clear all; close all;
N = 8;
fs = 10*N;  % 10 times the maximum frequency component in Hertz.
for T = 0:1:29
    t = 0:1/fs:1-1/fs;
    t = t+T;
    m = 2*N*sinc(2*N*t);
    x = hilbert(m);
    
    mf = fft(x)/fs;
    mf_abs_sorted = fftshift(abs(mf));
    freq_axis = linspace(-fs/2, fs/2, length(mf));
    
    figure(1);
    subplot(2,1,1);
    plot(t,real(x),'g',t,imag(x),'red');hold on;
    title('Time Domain');
    xlabel('Time in seconds');
    ylabel('Amplitude');
    legend('Realpart of x(t))','Imaginary part of x(t)');

    subplot(2,1,2);
    plot(freq_axis,mf_abs_sorted);hold on;
    title('Frequency Domain');
    ylabel('Frequency in Hertz')
    pause(0.5);
end