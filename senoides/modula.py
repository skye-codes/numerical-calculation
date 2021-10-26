import matplotlib.pyplot as plt
from numpy import sin, cos
import numpy as np
from scipy.fftpack import fft

# Inputs
# -------------------------------------------------------------------------------------------

t = np.linspace(0,10,20000)                                 # Tempo
E0 = 6                                                      # tensão de pico da portadora
noise = np.random.normal(scale = 0.01, size = len(t))       # ruido frequencia portadora
fc = 750                                             # frequência portadora
phi_c = 0                                                   # Fase campo
fm = 40  + noise                                                   # Frequência modular
m = 2                                                       # Indice de modulação(Vp)
phi_m = 0                                                   # Fase da modulação
x_limit = [-0.01,0.08]

# --------------------------------------------------------------------------------------------
# Carrier field
def carrier_field():
   return E0*np.cos(fc*2*np.pi*t + phi_c)


# Signal
def signal_in():
    return m*sin(fm*2*np.pi*t + phi_m)


# Phase modulated field
def modulated_field():
    return E0*np.cos(fc*2*np.pi*t + phi_c)*(1 - (m/2)*(1-np.sin(fm*2*np.pi*t+phi_m) ))

def noise_plot():
    return E0 * np.cos(noise * 2 * np.pi * t + phi_c) * (1 - (m / 2) * (1 - np.sin(fm * 2 * np.pi * t + phi_m)))


# Plotting
# ----------------------------------------------------------------------------------------------
def graph_plot(t, E, x, E_m, titulo, x_limit):
    fig = plt.figure(figsize=(20,8))

    # Axis for carrier and modulated field - unique plot
    ax = plt.subplot(1,1,1)
    p1 = ax.plot(t,E,'0.7', label='$\mathrm{Portadora}\ E_c(t)$')
    p2 = ax.plot(t,E_m,'r',label='$\mathrm{Modulação AM DSB}\ E_m(t)$')
    ax.set_xlabel('t(s)')
    ax.set_ylabel('E(t)')
    ax.set_title(titulo)
    ax.set_xlim(x_limit)

    # Second y-axis for signal
    ax2 = ax.twinx()
    p3 = ax2.plot(t,x,'b', label='$\mathrm{Sinal}\ x(t)$')
    ax2.set_ylabel('x(t)')

    # Legend
    plots = p1+p2+p3
    labs = [lab.get_label() for lab in plots]
    ax.legend(plots, labs, loc='upper right', bbox_to_anchor=(1.1, 1.15), fontsize=10)

    # Showing and save the figure
    plt.savefig(titulo + ".png")
    plt.show()

#plot noise and modulation
def graph_plot_noise (t, E, x, E_m, titulo, x_limit, noise):
    fig = plt.figure(figsize=(20, 8))

    # Axis for carrier and modulated field - unique plot
    ax = plt.subplot(1, 1, 1)
    p1 = ax.plot(t, noise, 'green', label='$\mathrm{Ruido}\ $')
    p2 = ax.plot(t,E,'0.7', label='$\mathrm{Portadora}\ E_c(t)$')
    p3 = ax.plot(t, E_m, 'r', label='$\mathrm{Modulação AM DSB}\ E_m(t)$')
    ax.set_xlabel('t(s)')
    ax.set_ylabel('E(t)')
    ax.set_title(titulo)
    ax.set_xlim(x_limit)

    # Second y-axis for signal
    ax2 = ax.twinx()
    p4 = ax2.plot(t, x, 'b', label='$\mathrm{Sinal}\ x(t)$')
    ax2.set_ylabel('x(t)')

    # Legend
    plots = p1 + p2 + p3 + p4
    labs = [lab.get_label() for lab in plots]
    ax.legend(plots, labs, loc='upper right', bbox_to_anchor=(1.1, 1.15), fontsize=10)

    # Showing and save the figure
    plt.savefig(titulo + ".png")
    plt.show()


#graph plot 2
def graph_plot2(t, E, x, E_m, titulo, x_limit):
    fig = plt.figure(figsize=(20,10))

    # Axis for carrier and modulated field - unique plot
    fig, ax = plt.subplots(3, 1)
    p1 = ax[0].plot(t, x, 'b', label='$\mathrm{Sinal}\ x(t)$')
    ax[0].set_title(titulo)
    ax[0].set_ylabel('X(t)')
    p2 = ax[1].plot(t,E,'0.7', label='$\mathrm{Portadora}\ E_c(t)$')
    p3 = ax[2].plot(t,E_m,'r',label='$\mathrm{Modulação AM DSB}\ E_m(t)$')
    ax[1].set_ylabel('e(t)')
    ax[2].set_xlabel('t')
    ax[0].set_xlim(x_limit)
    ax[1].set_xlim(x_limit)
    ax[2].set_xlim(x_limit)

    # Legend
    plots = p1+p2+p3
    labs = [lab.get_label() for lab in plots]
    ax[0].legend(plots, labs, loc=1, bbox_to_anchor=(1.13, 1.6), fontsize=8)

    # Showing and save the figure
    plt.savefig(titulo + ".png")
    plt.show()

def graph_plot_spectral(fr, X, titulo):
    fig =  plt.figure(figsize=(20, 8))
    p1 = plt.stem(fr, X, 'r')
    plt.xlabel('Frequência(Hz)')
    plt.ylabel('Magnitude')
    plt.title(titulo)
    plt.xlim(x_limit)

    # Showing and save the figure
    plt.savefig(titulo + ".png")
    plt.show()

#Test
# ----------------------------------------------------------------------------------------------
def test_dsb():
    E = carrier_field()
    x = signal_in()
    E_m = modulated_field()
    noise = noise_plot()

    graph_plot(t, E, x, E_m, "Modulação AM-DSB com sinal de informação de 40 Hz com 2Vp", x_limit)
    graph_plot_noise(t, E, x, E_m, "Modulação AM-DSB com sinal de informação de 40 Hz com 4Vp e ruído", x_limit, noise)
    graph_plot2(t, E, x, E_m, "Modulação AM-DSB", x_limit)
if __name__ == '__main__':
    test_dsb()
