clc;
close;
clear;
symbols=double(['s' 'a' 'h' 'i' 'r' ' ' 'd' 't' 'n']); %decomposed my name into ascii coded symbols
probs=[.133 .133 .133 .133 .133 .133 .066 .066 .07]; %adjusted for sum of probability to be 1
[dict,avglen] = huffmandict(symbols,probs);
inputsig=['sidharth s nair'];
code=huffmanenco(double(inputsig),dict);
disp(char(huffmandeco(code,dict)));