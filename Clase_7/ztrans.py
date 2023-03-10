import scipy.signal as signal
from pylab import *
import matplotlib.pyplot as plt
import numpy as np

def mfreqz(b,a=1):
    w,h = signal.freqz(b,a, worN=1024)
    w=w[1:]
    h=h[1:]
    fig = plt.figure(figsize=(15, 9))
    plt.title('Frequency response')
    ax1 = fig.add_subplot(111)    
    plt.plot(w, 20 * np.log10(abs(h)), 'b')
    plt.ylabel('Amplitude [dB]', color='b')
    plt.xlabel('Frequency [rad/sample]')    
    ax2 = ax1.twinx()
    angles = np.unwrap(np.angle(h))
    plt.plot(w, angles, 'g')
    plt.ylabel('Angle (radians)', color='g')
    plt.grid()
    plt.axis('tight')
    plt.show()
def impz(b,a=1):
    l = len(b)
    impulse = repeat(0.,l); impulse[0] =1.
    x = arange(0,l)
    response = signal.lfilter(b,a,impulse)
    subplot(211)
    stem(x, response)
    ylabel('Amplitude')
    xlabel(r'n (samples)')
    title(r'Impulse response')
    subplot(212)
    step = cumsum(response)
    stem(x, step)
    ylabel('Amplitude')
    xlabel(r'n (samples)')
    title(r'Step response')
    subplots_adjust(hspace=0.5)
    show()
def zeropoles(b, a=1):
    w,h = signal.freqz(b,a)
    sys1=signal.lti(b, a)
    ang=np.arange(0.0,2*np.pi,0.01)
    xp=np.cos(ang)
    yp=np.sin(ang)
    plot(xp,yp,'--') #circunferencia unitaria
    plot(sys1.zeros.real, sys1.zeros.imag, 'o')
    plot(sys1.poles.real, sys1.poles.imag, 'x')
    show()
    
