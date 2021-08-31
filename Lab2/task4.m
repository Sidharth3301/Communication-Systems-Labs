clc;
clear;
f1=440;
f2=480;
fs=10000;
t=0:(1/fs):2;
note1=0.1*sin(2*pi*f1.*t);
note2=0.1*sin(2*pi*f2.*t);
while(1)
    sound(note1+note2,fs);
    pause(6);
end

   
