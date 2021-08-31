% (Adjust parameters as needed.)
numberOfSeconds = 1
samplingRate = 7500 % Samples per second.
numberOfSamples = samplingRate * numberOfSeconds
t = linspace(0, numberOfSeconds, numberOfSamples);
% Get f:
f =50 + sin(t); 
% Get v:
v = 240 * sin(2*pi*f .* t);
% Plot:
plot(t, v);
% Enlarge figure to full screen.
set(gcf, 'units','normalized','outerposition',[0 0 1 1]);
