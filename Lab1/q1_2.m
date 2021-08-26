clc;
clear all;
mat=imread('Lenna.png');
image(mat)
mat_reshape=reshape(mat,1,[]);
bin_mat=dec2bin(mat_reshape);
bin_mat=reshape(bin_mat,[],1);
