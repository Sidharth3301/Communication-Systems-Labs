clc;
clear all;

mat=audioread('file_example_WAV_1MG.wav');
mat_new=mat(:,1)/max(mat(:,1));  %normalizing to avoid floating point literals which arent properly converted by dec2bin
mat_new=mat_new+1;
%sound(mat,8192);
subplot(2,1,1);

plot(mat(:,1));xlabel('Time steps');ylabel('Sound Amplitude');
title('Left channel audio signal');
subplot(2,1,2);

plot(mat(:,2));xlabel('Time steps');ylabel('Sound Amplitude');
title('Right channel audio signal');
bin_mat=dec2bin(mat_new(:,1));
reshaped_bin_mat=reshape(bin_mat,1,[]);
%Sample of audio bitstream
%disp(reshaped_bin_mat(1:10));
disp(size(reshaped_bin_mat));
