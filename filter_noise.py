#This function generates a noisy sine wave based on the frequency, amplitude
#time range and spacing, and noise modulator(how "loud" the noise is). 
def generate_noisy_sine_wave(freq,amp,time,noise):
    import random
    sine_wave = map(lambda x: amp*math.sin(x*freq*2*np.pi)\
    +random.choice(noise),time)
    return sine_wave

#This function generates a regular sine wave based on the frequency, amplitude
#time range and spacing.
def generate_sine_wave(freq,amp,time):
    sine_wave = map(lambda x: amp*math.sin(x*freq*2*np.pi),time)
    return sine_wave

#This function filters a signal using a Moving Average filter.
def moving_average_filter(wave):
    new_wave = map(lambda x: (wave[x]+wave[x-1]+wave[x-2])/3,range(0,len(wave)))
    return new_wave


#Example########
import math
import numpy as np
import matplotlib

freq = 1
amp = 1
noise = 0.3*np.linspace(-1,1,1000)
time = np.linspace(0,3,1000)
alpha = 0 #Currently unused but there for expansion of filtering methods
#y = [math.sin(i*freq*2*np.pi) for i in time]
noisy_sine = generate_noisy_sine_wave(freq,amp,time,noise)
sine = generate_sine_wave(freq,amp,time)
filtered_sine = moving_average_filter(noisy_sine)

matplotlib.pyplot.plot(time,noisy_sine,'.')
matplotlib.pyplot.plot(time,filtered_sine)
matplotlib.pyplot.plot(time,sine)