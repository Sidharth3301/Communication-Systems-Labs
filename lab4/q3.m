clear all;
close all;
clc;
duration_signal=29;
A=1;
for T = 0:duration_signal  %%%% Duration 30 seconds with interval of 1 sec.
    if T==0
    display('Transmission Started')
     display (T)
    elseif (T==duration_signal) 
        display('Transmission ends: see the final result')
     display (T)
    else
            display('Transmission in progress: please wait')
     display (T)
    end 
    freq=8;
    N=8;
    fs=4*freq;
    ts=1/fs;
     t=0:ts:1;
    f=10+mod(randi(100,1,2),90);
    U=randi(5);
    bw=50 ;%bandwidth=50Hz
    m_t= N*cos(2*pi*f(1)*t)+N*cos(2*pi*f(2)*t);
    channel=2*bw*sinc(2*bw*t);
    y=conv(m_t,channel,'same');
    N1=length(y);
    m_f= fft(y,N1)/fs;
    freqaxis=linspace(-fs/2,fs/2, N1); 
    figure(1)

    hold all  %%% keeps the previous plots and everytime changes the color
    subplot(2,1,1), plot(t+T,y);
    xlabel('time')
    ylabel('amplitude')
    
    title('Realtime signal: time-domain');
    grid on
    axis([0  inf -8 8])   %%% first two are limits for x-axis, the other two are limits for y-axis: observe why 0 inf , and -5 5 are used here.
    hold on     %%% keeps the previous plots 
    subplot(2,1,2);
    plot(freqaxis,fftshift(abs(m_f)));
      xlabel('frequency (Hz)')
    ylabel('Magnitude')
    title('Realtime signal: freq domain');
    grid on
    axis([-inf inf 0 100])  %%% first two are limits for x-axis, the other two are limits for y-axis: observe why -inf inf , and 0 3 are used here. 
    pause(0.5)  %%%%% pauses for 2 seconds and then go for next loop increment.
end