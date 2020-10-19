import math
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

#fuzil escolhido: AK-107
#velocide de disparo = 900 m/s
#calibre  	5.45×39mm
# massa = 3,8 Kg
#https://pt.wikipedia.org/wiki/AK-107
 #consts
velocidade_inicial = 900
m = 0.0038 #massa projetil
area = 0.25 * math.pi * 0.00545
b = 0.5 * area * 1.25 * 0.5
g = 9.81
n_maximo=1000


def main():
    print("\n______________________EDO - dispado de Fuzíl de assalto________________________")
    print("#################################################################################")
    print("#################################################################################")
    print("_________________________________________________________________________________\n")


def radianos(x):
    return x * math.pi / 180

def angulo():
    ang_inicial = float(input('Digite o Ângulo de disparo em graus: '))
    ang = radianos(ang_inicial)
    return calcula(ang_inicial,ang)

def calcula(ang_inicial, ang):

    passo = 0.001
    n = 0
    altura = 0
    distancia = 0

    x = np.empty(n_maximo)
    y = np.empty(n_maximo)
    dx = np.empty(n_maximo)
    dy = np.empty(n_maximo)
    energiaX = np.empty(n_maximo)
    energiay = np.empty(n_maximo)
    vx = np.empty(n_maximo)
    vy = np.empty(n_maximo)

    vx[n] = velocidade_inicial * math.cos(ang)
    vy[n] = velocidade_inicial * math.sin(ang)

    energiaX[n] = m *0.5 * vx[n] **2
    energiay[n] = m *0.5 * vy[n] **2

    x[0] = vx[n] * passo
    y[0] = vy[n] * passo

    dx[0] = x[n] - distancia
    dy[0] = y[n] - altura

    altura = y[n]
    distancia = x[n]

    ang = math.atan((dy[n])/(dx[n]))
    alturamax= 0

    n=1

    while n < n_maximo:
        if vy[n-1] < 0.0001:
            break
        if altura < 0.001:
            break

        energiaX[n] = energiaX[n-1] - b * vx[n-1]**2
        energiay[n] = energiay[n-1] - b * vy[n-1]**2

        if energiaX[n] < 0 and m*0.5 + b* dx[n-1] > 0:
            break
        if energiaX[n] > 0 and (m*0.5 + b* dx[n-1]) < 0:
            dx[n-1] = math.fabs(dx[n-1])

        vx[n]=(energiaX[n]/(m*0.5 + b* dx[n-1]))**(1/2)

        if((energiay[n]) < 0 and (m*0.5 + b* dy[n-1]) > 0):
            break
        if(energiay[n]) > 0 and (m*0.5 + b* dy[n-1]) < 0:
            dy[n-1] = math.fabs(dy[n-1])

        vy[n] = ((energiay[n])/(m*0.5 + b* dy[n-1]))**(1/2)

        x[n] = x[n-1] + vx[n-1] * passo
        y[n] = y[n-1] + vy[n-1] * passo

        distancia = x[n]
        altura = y[n]

        dx[n] = x[n] - x[n-1]
        dy[n] = y[n] - y[n-1]

        ang = math.atan(dy[n]/dx[n])
        print("Tempo: {:.2} s ---- Velocidade em X: {:.5} ---- Velocidade em Y: {:.5} ---- Altura: {:.5} ---- Distância: {:.5}".format(n*passo,vx[n],vy[n],altura,distancia))
        n = n + 1

    alturaMax = np.amax(y)
    print("\n\n______________________________________________________________________________________________________________________________________")
    print("Para um ângulo de {}º ---->  Alcance máximo: {:.5} m ----> Altura máxima: {:.5} m ----> Em {} s".format(ang_inicial,np.amax(y),alturaMax,n*passo))
    print("______________________________________________________________________________________________________________________________________")
    grafico(vy)



def grafico(x):
  print("\nCriando gráfico...")
  fig = plt.figure(figsize=(10, 8))
  ax = fig.add_subplot(111)

  ax.set(xlabel='tempo (s)', ylabel='velocidade (m/s)',
       title='Decaimento da velocidade da bala')

  plt.grid(True)
  plt.xscale("symlog")
  ax.plot(x, color = 'orange')
  fig.savefig('grafico_disparo.png')
  print("Grafico feito com sucesso! Arquivo em: grafico_disparo.png\n\n\n")

if __name__ == "__main__":
    main()
    angulo()

