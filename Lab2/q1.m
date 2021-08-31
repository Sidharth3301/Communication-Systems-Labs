clc;
close all;
B=13;
f=13;%B=N+5
fs=4*f;
tmin=-1;
tmax=1;
t=tmin:(1/fs):tmax;
m = 2*B*sinc(2*B*t);
subplot(2,1,1);
plot(t,m);ylabel('amplitude');xlabel('time');title('sinc waveform');
subplot(2,1,2);
stem(t,m);ylabel('amplitude');xlabel('time');title('Discretised sinc pulse');
%plot(t2,26 * sin(2*pi*f .*t)./(2*pi*f .*t));ylim([-10 10]);
