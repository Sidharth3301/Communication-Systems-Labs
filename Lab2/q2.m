clc;
close all;
d_min=10e-3;
d_max=5000e-3;
d_step=500e-3;
f1=4e3;  %Hz
f2=4e6;
f3=4e9;
% for wire type=0.4mm
data=struct;
data.r_oc = 280;
data.a_c= 0.0969;
data.L_o = 587.3e-6;
data.L_inf = 426e-6;
data.b = 1.385;
data.fm = 745900;
data.c_inf = 50e-9;
data.c_0 = 0;
data.c_e = 1;
data.g_0 = 0;
data.g_e = 1;
t=d_min:d_step:d_max;
H1=zeros(length(t),1);
H2=zeros(length(t),1);
H3=zeros(length(t),1);
for i=1:length(t)
    H1(i)=10*log10(channel_gain(f1,t(i),data));
    H2(i)=10*log10(channel_gain(f2,t(i),data));
    H3(i)=10*log10(channel_gain(f3,t(i),data));
end
figure(1);
plot(t,H1);hold off;title('channel gain for f=4KHz');xlabel('distance(km)');ylabel('db');
figure(2);
plot(t,H2);title('channel gain for f=4Mhz');xlabel('distance(km)');ylabel('db');
figure(3)
plot(t,H3);%legend('f=4khz','f=4mhz','f=4ghz');
title('channel gain for f=4Ghz');xlabel('distance(km)');ylabel('db');
fig1=figure;
plot(t,H1);hold on;ylim([-1000 100]);plot(t,H2);plot(t,H3);title('channel gain magnitude');xlabel('distance(km)');ylabel('db');legend('f=4khz','f=4mhz','f=4ghz');

function gain = channel_gain(x,d,data)
    gain=abs(exp(-1*gamma(x,d,data)*d));
end

function gamma = gamma(x,d,data)
    gamma = sqrt((resistance(x,d,data)+1i*omega(x)*inductance(x,d,data))*(conductance(x,d,data)+1i*omega(x)*capacitance(x,d,data)));
end

function omega = omega(x)
    omega = 2*pi*x;
end

function cond = conductance(x,d,data)
    cond = data.g_0*d*x^(data.g_e); 
end
function res = resistance(x,d,data)
    res = (((data.r_oc)^4 +(data.a_c)*x^2)*d)^(1/4); 
end
function ind = inductance(x,d,data)
    ind = (data.L_o*d+(data.L_inf*d*(x/data.fm)^data.b))/(1+(x/data.fm)^data.b); 
end
function cap = capacitance(x,d,data)
    cap = (data.c_inf*d+data.c_0*d*x^(-data.c_e)); 
end