import matplotlib.pyplot as plt
from numpy import sin, cos
import numpy as np
from scipy.fftpack import fft


#time range
#---------------------------------------------------------------------------
t = np.linspace(0,10,500)


#Senoides
#---------------------------------------------------------------------------
def senoideA(x):
    return (1/2) + (2/np.pi) * np.sin(x)

def senoideB(x):
    return (2/3*np.pi) * np.sin(3*x)

def senoideC(x):
    return (2/5*np.pi) * np.sin(5*x)

def senoideD(x):
    return (2/7*np.pi) * np.sin(7*x)

def senoide_sum_signal(A, B, C, D):
    return (A + B + C + D)


#Graph plot
def graph_plot_sum(x, y, titulo):
    fig = plt.figure(figsize=(15, 8))
    plt.title(titulo)
    plt.grid(True)
    plt.xlabel('t(s)')
    plt.ylabel("Amplitude")
    plt.plot(x,y)
    # Showing and save the figure
    plt.savefig(titulo + ".png")
    plt.show()


def graph_plot_frequency(x, y, titulo):
    fig = plt.figure(figsize=(15, 8))
    plt.title(titulo)
    plt.grid(True)
    plt.xlabel('Frequência(Hz)')
    plt.ylabel("Amplitude")
    plt.plot(x,y)
    # Showing and save the figure
    plt.savefig(titulo + ".png")
    plt.show()

#Frequency domain
#---------------------------------------------------------------------------
def senoide_sum_frequency(s):
    fft = np.fft.fft(s)

    T = t[1] - t[0]  # 0.001 -> 1/T = 1000
    N = s.size
    f = np.linspace(0, 1 / T, N)
    # fornece os componentes de frequência correspondentes aos dados
    f = np.fft.fftfreq(len(s), T)
    frequencias = f[:N // 2]
    amplitudes = np.abs(fft)[:N // 2] * 1 / N
    plt.title("Dominio da Frequência para a soma dos sinais")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.xlabel("Frequência (Hz)")
    plt.bar(frequencias, amplitudes, width=0.1)
    # plt.specgram(s, NFFT=N - 1, Fs=1 / T, scale='linear', scale_by_freq=False)
    # plt.colorbar()
    # plt.ylabel('Frequência (Hz)')
    # plt.xlabel('Tempo (s)')
    # plt.savefig('fft_spectrogram.png')
    plt.savefig('fft_freq.png')
    plt.show()
    plt.close()


#tests
#---------------------------------------------------------------------------
def test_senode():
    # time domain
    x = t
    x_limit = [0, 10]
    A = senoideA(x)
    B = senoideB(x)
    C = senoideC(x)
    D = senoideD(x)
    sum_signal = senoide_sum_signal(A, B, C, D)
    graph_plot_sum(x, sum_signal, 'Sinais somados')

    #frequency domain
    senoide_sum_frequency(sum_signal)


if __name__ == '__main__':
    test_senode()