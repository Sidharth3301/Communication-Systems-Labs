audio = fopen('file_example_WAV_1MG.wav');
audio_data = fread(audio,'ubit1');

audio_binary = dec2bin(audio_data);

audio_size = size(audio_data);
disp = reshape(audio_binary',1,[]);
fclose(audio);