clc;close all;
no_symbols = 30;
bit_rate = 1;
t_final = no_symbols/bit_rate;
N = 6;
fs = 1e3;
t = 0:1/fs:t_final-1/fs;

U = randi([1 5], 1, no_symbols);
Uf = kron(U, ones(1, fs/bit_rate));

y = Uf.*cos(2*pi*t*N);
figure;
plot(t, y);