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

def senoideE(x):
    return (2/9*np.pi) * np.sin(9*x)

def senoideF(x):
    return (2/11*np.pi) * np.sin(11*x)

def senoideG(x):
    return (2/13*np.pi) * np.sin(13*x)

def senoideH(x):
    return (2/15*np.pi) * np.sin(15*x)

def senoideI(x):
    return (2/17*np.pi) * np.sin(17*x)


def senoide_sum_signal(A, B, C, D):
    return (A + B + C + D)

def senoide_sum_signal2(A, B, C, D,E,F,G,H,I):
    return (A + B + C + D + E + F + G + H + I)


#Graph plot
#---------------------------------------------------------------------------
def graph_plot_individual(x_limit,y_a,y_b,y_c,y_d, titulo):
    fig = plt.figure(figsize=(20, 8))

    # Axis for carrier and modulated field - unique plot
    ax = plt.subplot(1, 1, 1)
    p1 = ax.plot(t, y_a, '0.1', label='A')
    p2 = ax.plot(t, y_b, 'r', label='B')
    p3 = ax.plot(t, y_c, 'g', label='C')
    p4 = ax.plot(t, y_d, 'b', label='D')
    ax.set_xlabel('t(s)')
    ax.grid(True)
    ax.set_ylabel('Amplitude')
    ax.set_title(titulo)
    ax.set_xlim(len(x_limit))


    # Legend
    plots = p1 + p2 + p3 + p4
    labs = [lab.get_label() for lab in plots]
    ax.legend(plots, labs, loc=1, fontsize=10)

    # Showing and save the figure
    plt.savefig(titulo + ".png")
    plt.show()

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
    t2 = (0, 1, 500) # 500 números, de 0 a 0.5 -> 1 kHz de amostragem
    T = t2[1] - t2[0]  # 0.001 -> 1/T = 1000
    N = s.size
    #f = np.linspace(50, N)
    # fornece os componentes de frequência correspondentes aos dados
    f = np.fft.fftfreq(len(s), T)
    frequencias = f[:N // 2]
    amplitudes = np.abs(fft)[:N // 2] * 1 / N
    plt.title("Dominio da Frequência para a soma dos sinais")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.xlabel("Frequência (Hz)")
    plt.bar(frequencias, amplitudes, width=0.01)
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
    #time domain
    x = t
    x_limit = [0,10]
    A = senoideA(x)
    B = senoideB(x)
    C = senoideC(x)
    D = senoideD(x)
    E = senoideE(x)
    F = senoideF(x)
    G = senoideG(x)
    H = senoideH(x)
    I = senoideI(x)
    sum_signal = senoide_sum_signal(A, B, C, D)
    sum_signal_2 = senoide_sum_signal2(A, B, C, D, E, F,G,H,I)
    graph_plot_individual(x_limit, A, B, C, D, "Sinais individuais")
    graph_plot_sum(x,sum_signal, 'Sinais somados')
    graph_plot_sum(x,sum_signal_2, 'Sinais somados - Gráfico 2')

    #frequency domain
    senoide_sum_frequency(sum_signal)


if __name__ == '__main__':
    test_senode()