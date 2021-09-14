clear all;
close all;
clc;
duration_signal=29;
A=1;
t_start=ones(1,4);
%tstop=ones(1,4);
freq=8;
N1=8;
fs=4*freq;
ts=1/fs;
t1=0:ts:30;
rect=@(T,t)(abs(t)<(T/2));
m1=cos(2*pi*freq*t1);
m2=2*N1*sinc(2*N1*t1);
m3=rect(N1,t1);
[y,Fs]=audioread('file_example_WAV_1MG.wav');
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
    
    fs=4*freq;
    ts=1/fs;
    t=0:ts:1;
    U=randi(4);
    %m_t=U*cos(2*pi*freq*t);  
    if U==1
        m_t=m1(t_start(1):t_start(1)+fs+1);
        t_start(1)=t_start(1)+fs;
    elseif(U==2)
        m_t=m2(t_start(2):t_start(2)+fs+1);
        t_start(2)=t_start(2)+fs;
    elseif (U==3)
        m_t=m3(t_start(3):t_start(3)+fs+1);
        t_start(3)=t_start(3)+fs;
    else
        m_t=y(t_start(4):t_start(4)+Fs+1);
        t_start(4)=t_start(4)+Fs;
        fs=Fs;
    end
    N=length(m_t);
    m_f= fft(m_t,N)/fs;
    freqaxis=linspace(-100,100, N);
    figure(1)
    
    hold all  %%% keeps the previous plots and everytime changes the color
    subplot(2,1,1), 
    if U==4
        t2=0+T:1/fs:1+T;
        plot(t2,m_t(1:size(t2,2)));
    else
        plot(t+T,m_t(1:size(t,2)));
    end
    
    xlabel('time')
    ylabel('amplitude')
    title('Realtime signal: time-domain');
    grid on
    axis([0  inf -5 5])   %%% first two are limits for x-axis, the other two are limits for y-axis: observe why 0 inf , and -5 5 are used here.
    hold on     %%% keeps the previous plots 
    subplot(2,1,2), plot(freqaxis,fftshift(abs(m_f)))
    xlabel('frequency (Hz)')
    ylabel('Magnitude')
     title('Realtime signal: freq domain');
    grid on
    axis([-inf inf 0 3])  %%% first two are limits for x-axis, the other two are limits for y-axis: observe why -inf inf , and 0 3 are used here. 



    pause(0.5)  %%%%% pauses for 2 seconds and then go for next loop increment.
end