clc;
clear all;

fileID=fopen('text_signal.txt');

a=fread(fileID);
disp(size(a));
m=dec2bin(a);
m=reshape(m,[],1)
%disp(m(1:15));
fclose(fileID);